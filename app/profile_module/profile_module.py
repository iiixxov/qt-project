from PySide6.QtWidgets import QWidget

from project_settings import ICONS_PATH
from ..core import Database, input_box
from ..core.module import TrayModule
from ui.ui_profile import Ui_Form


class ProfileModule(TrayModule):
    _ui: Ui_Form

    def __init__(self, parent: QWidget, app):
        super().__init__(parent, app)

    def icon_path(self) -> str:
        return ICONS_PATH + 'user-b.svg'

    def _ui_class(self) -> type:
        return Ui_Form

    def change_password(self):
        if r := input_box(
                "Новый пароль\n(Только латинские буквы и цифры)", "Повторите пароль",
                re_validator=r"^[A-Za-z0-9]+$",
                parent=self._widget,
                password_type=True):
            passw, passw_ = r

            if passw != passw_:
                self._app.couch(Exception("Пароли не совпадают"))
                return

            Database.user.change_password(passw)
            Database.session.commit()

    def setup(self):
        super().setup()
        self._button.setText(username := Database.user.name)
        self._ui.lbl_username.setText(username)

        self._ui.btn_change_password.clicked.connect(self.change_password)
