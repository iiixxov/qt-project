import datetime
from typing import List

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QWidget
from sqlalchemy import or_

from project_settings import ICONS_PATH
from .notification_widget import NotificationWidget
from .. import Notification
from ..core import Database, Settings, func
from ..core.module import TrayModule
from ui.ui_notifications import Ui_Form


class NotificationsModule(TrayModule):
    _ui: Ui_Form

    def __init__(self, parent: QWidget, app):
        self._last_time: datetime.datetime = datetime.datetime.now()
        self._timer = QTimer()
        self._notifications: List[NotificationWidget] = []

        super().__init__(parent, app)

    def icon_path(self) -> str:
        return ICONS_PATH + 'Notification-b.svg'

    def _ui_class(self) -> type:
        return Ui_Form

    def add_notification(self, notification: Notification):
        widget = NotificationWidget(notification)
        self._notifications.append(widget)
        self._ui.scrollAreaWidget.layout().addWidget(widget)

    def change_view_mode(self, not_is_impotent_only: bool):
        for widget in self._notifications:
            if not widget.notification.is_impotent:
                widget.setVisible(not_is_impotent_only)

    def show_notification(self, notification: Notification):
        pm = Settings['notifications']['popup_margin']

        widget = NotificationWidget(notification, parent=(window := self._app.window))
        widget.setStyleSheet(func.css_format(Settings['notifications']['popup_css_path']))
        widget.setGeometry(
            window.width() - (ww := widget.width()) - pm, window.height() - (wh := widget.height()) - pm, ww, wh
        )
        widget.mousePressEvent = lambda *_: (self.open(), widget.deleteLater())
        widget.show()
        widget.delete_in(Settings['notifications']['popup_show_time'])

    def select_last(self):
        print(self._last_time.strftime('%H:%M:%S'))
        for notification in (Database.session.query(Notification)
                             .filter(
                                Notification.created_at > self._last_time,
                                or_(Notification.to_user == Database.user.name, Notification.to_user == ""),
                             ).order_by(Notification.id).all()):
            notification: Notification
            self._last_time = max([notification.created_at, self._last_time])
            self.add_notification(notification)
            notification.is_popup and self.show_notification(notification)

    def first_select(self):
        for notification in reversed(Database.session.query(Notification)
                                     .filter(
                                         or_(Notification.to_user == Database.user.name, Notification.to_user == ""),
                                         Notification.is_impotent == True
                                     ).order_by(Notification.id.desc())
                                     .limit(Settings['notifications']['init_select_limit']).all()):
            notification: Notification
            self._last_time = max([notification.created_at, self._last_time])
            self.add_notification(notification)

    def setup(self):
        super().setup()
        self._ui.cmb_notification_impotent.currentIndexChanged.connect(self.change_view_mode)

        self.first_select()
        self._timer.timeout.connect(self.select_last)
        self._timer.setInterval(Settings['notifications']['select_interval'])
        self._timer.start()
