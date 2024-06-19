from PySide6.QtWidgets import QListWidgetItem
from sqlalchemy import BinaryExpression


class FilterListItem(QListWidgetItem):
    def __init__(self, filter_: BinaryExpression, header: str):
        super().__init__(header)
        self._filter = filter_

    @property
    def filter(self):
        return self._filter
