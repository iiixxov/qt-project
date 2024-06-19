from PySide6.QtCore import QTimer
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget

from .. import Notification
from app.core import Settings
from app.core.notification import NOTIFICATION_ICONS
from project_settings import ICONS_PATH
from ui.ui_notification_widget import Ui_NotificationWidget
from ..core.func import clear_layout


class NotificationWidget(QWidget):
    def __init__(self, notification: Notification, parent: QWidget = None):
        super().__init__(parent)
        self._notification = notification
        self._ui = Ui_NotificationWidget()
        self._timer = QTimer()
        self._collapsed: bool = True

        self.setup()

    def mousePressEvent(self, event):
        self._collapsed = not self._collapsed

        if self._collapsed:
            self._ui.lbl_body.setText(f"{self._notification.body[:Settings['notifications']['body_preview']]}...")
        else:
            self._ui.lbl_body.setText(self._notification.body)

        super().mousePressEvent(event)

    def setup(self):
        self._ui.setupUi(self)

        self._ui.lbl_header.setText(self._notification.header)
        self._ui.lbl_body.setText(f"{self._notification.body[:Settings['notifications']['body_preview']]}...")
        self._ui.lbl_time.setText(self._notification.created_at.strftime("%d.%m.%Y %H:%M"))
        self._ui.btn_icon.setIcon(QIcon(ICONS_PATH + NOTIFICATION_ICONS[self._notification.type]))

    def delete_in(self, time: int):
        self._timer.setInterval(time)
        self._timer.timeout.connect(self.deleteLater)
        self._timer.start()

    def deleteLater(self):
        clear_layout(self.layout())
        self._timer.deleteLater()
        super().deleteLater()

    @property
    def notification(self):
        return self._notification
