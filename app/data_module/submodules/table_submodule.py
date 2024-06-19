from typing import Sequence

from app.core import Database
from . import DataSubmodule
from app.data_module.tree_items import TableTreeItem, DataModuleTreeItem
from project_settings import ICONS_PATH
from ..query_request import QueryRequest


class TableSubmodule(DataSubmodule):
    def __init__(self, app, data_module):
        super().__init__(app, data_module)

    def icon_path(self) -> str:
        return ICONS_PATH + 'table-b.svg'

    def visible_name(self) -> str:
        return "Таблицы"

    def load(self) -> Sequence[TableTreeItem]:
        for table in Database.Model.registry.mappers:
            model = table.class_
            yield TableTreeItem(model, self)

    def get_query(self, clicked_item: DataModuleTreeItem) -> QueryRequest:
        if isinstance(clicked_item, TableTreeItem):
            return QueryRequest(
                query=Database.session.query(clicked_item.table),
                model=clicked_item.table,
                filter_=None
            )
