from abc import abstractmethod
from typing import Sequence

from PySide6.QtWidgets import QTreeWidgetItem
from sqlalchemy.orm import Query

from app.data_module.query_request import QueryRequest


class DataSubmodule:
    def __init__(self, app, data_module):
        self._app = app
        self._data_module = data_module

        self.setup()

    @abstractmethod
    def icon_path(self) -> str: ...
    @abstractmethod
    def visible_name(self) -> str: ...

    @abstractmethod
    def load(self) -> Sequence[QTreeWidgetItem]: ...

    @abstractmethod
    def get_query(self, clicked_item: QTreeWidgetItem) -> QueryRequest: ...

    def setup(self):
        pass
