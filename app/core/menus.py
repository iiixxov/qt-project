from typing import Any

from PySide6.QtCore import QPoint
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QWidget, QMenu


class ChoiceMenu(QMenu):
    def __init__(self, variants: dict[str: Any], parent: QWidget = None):
        super().__init__(parent)
        self.setup(variants)

    def execute(self, pos: QPoint):
        return a.data() if (a := self.exec(pos)) is not None else None

    def setup(self, variants: dict[str: Any]):
        for key, value in variants.items():
            self.addAction(a := QAction(value, self))
            a.setData(key)
