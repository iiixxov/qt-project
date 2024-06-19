from typing import List, Optional

from PySide6.QtGui import QCursor
from PySide6.QtWidgets import QWidget, QTableWidgetItem
from sqlalchemy import Column

from app import Module
from app.core import Database, Settings
from app.data_module.filter_list_item import FilterListItem
from app.data_module.filters_menu import FiltersMenu
from app.data_module.query_request import QueryRequest
from app.data_module.sql_table_item_class_factory import get_sql_table_item_class
from app.data_module.submodules.data_submodule import DataSubmodule

from app.data_module.tree_items import DataModuleTreeItem
from project_settings import ICONS_PATH
from ui.ui_data import Ui_Form


class DataModule(Module):
    _modules: List[type[DataSubmodule]] = []
    _initialized_modules: List[DataSubmodule] = []

    _ui: Ui_Form

    def __init__(self, parent: QWidget, app):
        self._cur_query: Optional[QueryRequest] = None
        self._cur_max_row_id: int = 0
        self._cur_min_row_id: int = 0

        super().__init__(parent, app)

    @classmethod
    def register_module(cls, module: type[DataSubmodule]):
        cls._modules.append(module)

    @property
    def ui(self):
        return self._ui

    def icon_path(self) -> str:
        return ICONS_PATH + 'search.svg'

    def visible_name(self) -> str:
        return 'Данные'

    def _ui_class(self) -> type:
        return Ui_Form

    def _connect_slots(self):
        self._ui.btn_refresh.clicked.connect(lambda: self.refresh_table())
        self._ui.tbl_table.itemDoubleClicked.connect(lambda i: i.item_double_clicked())
        self._ui.btn_filter.clicked.connect(self.show_filter_popup)
        self._ui.lst_filter.itemClicked.connect(
            lambda: self._ui.lst_filter.takeItem(self._ui.lst_filter.currentRow())
        )
        self._ui.trw_modules.itemClicked.connect(lambda i: self.get_query(i))

        self._ui.btn_left.clicked.connect(self.viewing_move_left)
        self._ui.btn_right.clicked.connect(self.viewing_move_right)
        self._ui.btn_left_left.clicked.connect(self.viewing_move_left_to_max)
        self._ui.btn_right_right.clicked.connect(self.viewing_move_right_to_min)

    def setup(self):
        super().setup()
        self._connect_slots()
        self._ui.splitter.setSizes(Settings['_sizes']['data_sections'])

        for module in self._modules:
            m = module(self._app, self)
            self._initialized_modules.append(m)
            self._ui.trw_modules.addTopLevelItem(mli := DataModuleTreeItem(m))
            for item in m.load():
                mli.addChild(item)

        self.update_table_buttons_view()

    def update_table_buttons_view(self):
        is_not_min_id = self._cur_min_row_id > self.get_min_row_id()
        is_not_max_id = self._cur_max_row_id < self.get_max_row_id()

        self._ui.lbl_rows.setText(f"{self._cur_max_row_id}-{self._cur_min_row_id}")
        self._ui.btn_left.setVisible(is_not_max_id)
        self._ui.btn_left_left.setVisible(is_not_max_id)
        self._ui.btn_right.setVisible(is_not_min_id)
        self._ui.btn_right_right.setVisible(is_not_min_id)

    def get_query(self, item: DataModuleTreeItem):
        self._cur_query = item.module.get_query(item)
        self.refresh_table()

    def viewing_move_left(self):
        self._cur_max_row_id += Settings['tables']['row_limit']
        self.refresh_table()
        self.update_table_buttons_view()

    def viewing_move_left_to_max(self):
        self._cur_max_row_id = self.get_max_row_id()
        self.refresh_table()
        self.update_table_buttons_view()

    def viewing_move_right(self):
        self._cur_max_row_id -= Settings['tables']['row_limit']
        self.refresh_table()
        self.update_table_buttons_view()

    def viewing_move_right_to_min(self):
        step, max_id = Settings['tables']['row_limit'], self.get_max_row_id()
        self._cur_max_row_id = max_id - (step * (max_id // step))
        self.refresh_table()
        self.update_table_buttons_view()

    def get_max_row_id(self):
        if self._cur_query is None or (row := (
                Database.session.query(self._cur_query.model.id)
                        .filter(*self._get_filters(), self._cur_query.filter_)
                        .order_by(self._cur_query.model.id.desc()).first()
        )) is None:
            return 0
        else:
            return row[0]

    def get_min_row_id(self):
        if self._cur_query is None or (row := (
            Database.session.query(self._cur_query.model.id)
                    .filter(*self._get_filters(), self._cur_query.filter_)
                    .order_by(self._cur_query.model.id).first()
        )) is None:
            return 0
        else:
            return row[0]

    def refresh_table(self):
        self._ui.tbl_table.clear()

        if not self._cur_query:
            self._ui.tbl_table.setColumnCount(0)
            self._ui.tbl_table.setRowCount(0)
            self.update_table_buttons_view()

        else:
            self._ui.tbl_table.setColumnCount(len(self.models_columns(self._cur_query.model)))
            self._ui.tbl_table.setRowCount(0)
            self._ui.tbl_table.setHorizontalHeaderLabels(
                [i.comment if i.comment else i.name for i in self._cur_query.model.__table__.columns]
            )
            self.select(self._cur_query, self._cur_max_row_id, Settings['tables']['row_limit'])

    def _get_filters(self):
        return [self._ui.lst_filter.item(i).filter for i in range(self._ui.lst_filter.count())]

    def show_filter_popup(self):
        if (res := FiltersMenu(self._cur_query.model, self._ui.tbl_table).execute(QCursor().pos())) is not None:
            filter_, header = res
            self._ui.lst_filter.addItem(FilterListItem(filter_, header))

    @staticmethod
    def models_columns(model: type[Database.Model]):
        return model.cols_without('id')

    def select(self, query_request: QueryRequest, max_id: int, limit: int):
        ids = []

        for row in reversed(query_request.query.filter(
                query_request.model.id <= max_id, *self._get_filters(), query_request.filter_
        ).order_by(query_request.model.id.desc()).limit(limit).all()):
            row: Database.Model

            self._ui.tbl_table.insertRow(0)
            self._ui.tbl_table.setVerticalHeaderItem(0, QTableWidgetItem(str(row.id)))
            ids.append(row.id)

            for j, column in enumerate(self.models_columns(query_request.model)):
                if column.name == query_request.model.id.name: continue
                self._ui.tbl_table.setItem(0, j, self.make_item(column, row))

        self._cur_max_row_id, self._cur_min_row_id = (max(ids), min(ids)) if ids else (0, 0)

    @staticmethod
    def make_item(column: Column, row: Database.Model):
        return get_sql_table_item_class(column)(row, column)
