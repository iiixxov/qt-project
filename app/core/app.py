import sys
from typing import List, Callable

from PySide6.QtGui import QIcon, QShortcut, QKeySequence
from PySide6.QtWidgets import QMainWindow, QApplication, QListWidgetItem, QDialog, QPushButton
from sqlalchemy import create_engine

from project_settings import CSS_PATH
from ui.ui_main_window import Ui_MainWindow
from . import func, Module, Database, Settings
from .error import Error
from .module import TrayModule


class App:
    _modules: List[type[Module | TrayModule]] = []
    _initialized_modules: List[Module] = []

    @classmethod
    def register_module(cls, module: type[Module | TrayModule]):
        cls._modules.append(module)

    def __init__(self):
        self._app = QApplication()
        self._window = QMainWindow()
        self._ui = Ui_MainWindow()
        self._keys: List[QShortcut] = []

        self.setup()

    @property
    def ui(self) -> Ui_MainWindow:
        return self._ui

    @property
    def window(self):
        return self._window

    def couch(self, exception: Exception):
        print(exception.with_traceback())

    def setup(self):
        self._ui_initialize()
        # self._login()
        Database.init_from_engine(create_engine('postgresql://postgres:1234@localhost/postgres'))
        Database.create_all()
        self._modules_initialize()
        self._connect_slots()
        self._setup_viewing()

    def register_shortcut(self, key_sequence: str, slot: Callable):
        self._keys.append(sc := QShortcut(QKeySequence(key_sequence), self._window))
        sc.activated.connect(slot)

    def _connect_slots(self):
        self._ui.lw_tabs.currentRowChanged.connect(lambda i: self._ui.central_block.setCurrentIndex(i))
        self.register_shortcut('F5', self.reload_stylesheet)

    def _setup_viewing(self):
        self.reload_stylesheet()
        self._ui.lw_tabs.setCurrentRow(0)
        self._ui.r_block.setVisible(False)

    def _ui_initialize(self):
        self._ui.setupUi(self._window)

    def _login(self):
        from ui.ui_login import Ui_LoginDialog

        def try_login():
            user, password = login_ui.inp_user.text(), login_ui.inp_password.text()
            if (error := Database.login(user, password)) is not None:
                login_ui.error_text.setText(Error.to_str(error))
            else:
                Settings['_saved']['db_username'] = user
                Settings.save()
                login_dialog.accept()

        login_dialog = QDialog(self._window)
        login_ui = Ui_LoginDialog()
        login_ui.setupUi(login_dialog)
        login_ui.inp_user.setText(Settings['_saved']['db_username'])

        login_dialog.rejected.connect(sys.exit)
        login_ui.btn_login.clicked.connect(try_login)

        login_dialog.exec()

    def _modules_initialize(self):
        for module in self._modules:
            m = module(self._window, self)
            self._initialized_modules.append(m)

            if issubclass(module, Module):
                self.add_to_menu(m)
            else:
                self.add_to_tray(m)

    def reload_stylesheet(self):
        self._window.setStyleSheet(func.css_format(CSS_PATH))

    def show_or_hide_tray(self, module: TrayModule):
        if self._ui.r_block.currentWidget() is module.widget:
            self._ui.r_block.setVisible(not self._ui.r_block.isVisible())
        else:
            self._ui.r_block.setCurrentWidget(module.widget)
            self._ui.r_block.setVisible(True)

    def add_to_menu(self, module: Module):
        self._ui.lw_tabs.addItem(QListWidgetItem(QIcon(module.icon_path()), module.visible_name()))
        self._ui.central_block.addTab(module.widget, "")

    def add_to_tray(self, module: TrayModule):
        self._ui.t_block.layout().addWidget(module.tray_button)
        self._ui.r_block.addTab(module.widget, "")

    def start(self):
        self._window.show()
        self._app.exec()
