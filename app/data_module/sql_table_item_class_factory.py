import datetime
from enum import Enum
from typing import Callable

from PySide6.QtGui import Qt, QCursor
from PySide6.QtWidgets import QTableWidgetItem
from sqlalchemy import Column

from app.core import Database, error_box
from app.core.menus import ChoiceMenu
from project_settings import BOOL_VIEW_DICT


def make_sql_table_item_class(before_in_view: Callable,
                              before_in_model: Callable,
                              editable: bool = True,
                              double_clicked: Callable = None,
                              after_edit_in_model: Callable = None):

    class SQLTableItem(QTableWidgetItem):

        def __init__(self, instance: Database.Model, column: Column):
            super().__init__(before_in_view(instance[column.key]))

            if editable:
                self.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEditable)
            else:
                self.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable)

            self._instance = instance
            self._column = column

        @property
        def instance(self):
            return self._instance

        @property
        def column_(self):
            return self._column

        def item_double_clicked(self):
            if double_clicked:
                double_clicked(self)

        def setData(self, role, value):
            if role == Qt.ItemDataRole.EditRole:
                try:
                    self._instance[self._column.key] = before_in_model(value)
                    value = after_edit_in_model(value) if after_edit_in_model is not None else value
                    Database.session.flush()
                    super().setData(role, value)
                except Exception as e:
                    Database.session.rollback()
                    error_box(str(e))
                Database.session.commit()

    return SQLTableItem


def _enum_item_double_clicked(item: make_sql_table_item_class):
    if (val := ChoiceMenu(
            {enum: enum.value for enum in item.column_.type.python_type}, parent=item.tableWidget()
    ).execute(QCursor().pos())) is not None:
        item.setData(Qt.ItemDataRole.EditRole, val)


def _bool_item_double_clicked(item: make_sql_table_item_class):
    if (val := ChoiceMenu(BOOL_VIEW_DICT, parent=item.tableWidget()).execute(QCursor().pos())) is not None:
        item.setData(Qt.ItemDataRole.EditRole, val)


def number_item_edited(value: str | float | int):
    if not value:
        return None
    elif (fv := float(value.replace(',', '.'))).is_integer():
        return int(fv)
    else:
        return int(value)


def get_sql_table_item_class(col: Column):
    if col.type.python_type is bool:
        return make_sql_table_item_class(
            lambda i: BOOL_VIEW_DICT[i],
            lambda i: i,
            editable=False,
            double_clicked=_bool_item_double_clicked,
            after_edit_in_model= lambda i: BOOL_VIEW_DICT[i]
        )

    if col.type.python_type in (int, float):
        return make_sql_table_item_class(
            lambda i: str(i).replace('.', ','),
            number_item_edited,
            editable=True,
            double_clicked=None
        )

    elif col.type.python_type is datetime.date:
        return make_sql_table_item_class(
            lambda i: i.strftime("%d.%m.%Y"),
            lambda i: datetime.datetime.strptime(i, "%d.%m.%Y"),
            editable=True,
            double_clicked=None
        )

    elif col.type.python_type is datetime.datetime:
        return make_sql_table_item_class(
            lambda i: i.strftime("%d.%m.%Y %H:%M"),
            lambda i: datetime.datetime.strptime(i, "%d.%m.%Y %H:%M"),
            editable=True,
            double_clicked=None
        )

    elif col.type.python_type is str:
        return make_sql_table_item_class(
            str,
            str,
            editable=True,
            double_clicked=None
        )

    elif issubclass(col.type.python_type, Enum):
        return make_sql_table_item_class(
            lambda i: i.value,
            lambda i: i,
            editable=False,
            double_clicked=_enum_item_double_clicked,
            after_edit_in_model=lambda i: i.value
        )

    else:
        return make_sql_table_item_class(
            str,
            str,
            editable=False,
            double_clicked=None
        )
