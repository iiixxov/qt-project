from abc import abstractmethod
from typing import Optional

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget, QPushButton


class Module:
    def __init__(self, parent: QWidget, app):
        from . import App
        self._ui = self._ui_class()()
        self._widget = QWidget(parent)
        self._app: App = app

        self.setup()

    @abstractmethod
    def icon_path(self) -> str: ...

    @abstractmethod
    def visible_name(self) -> str: ...

    @abstractmethod
    def _ui_class(self) -> type: ...

    @property
    def widget(self):
        return self._widget

    def setup(self):
        self._ui.setupUi(self._widget)
        self._widget.setStyleSheet("")


class TrayModule:
    def __init__(self, parent: QWidget, app):
        from . import App
        self._ui = self._ui_class()()
        self._widget = QWidget(parent)
        self._app: App = app
        self._button: QPushButton = QPushButton()

        self.setup()

    @property
    def tray_button(self):
        return self._button

    @abstractmethod
    def icon_path(self) -> str: ...

    @abstractmethod
    def _ui_class(self) -> type: ...

    @property
    def widget(self):
        return self._widget

    def open(self):
        self._app.ui.r_block.setVisible(True)
        self._app.ui.r_block.setCurrentWidget(self._widget)

    def setup(self):
        self._ui.setupUi(self._widget)
        self._widget.setStyleSheet("")
        self._widget.setObjectName("r_block_tray_widget")

        self._button.setIcon(QIcon(self.icon_path()))
        self._button.clicked.connect(lambda: self._app.show_or_hide_tray(self))
