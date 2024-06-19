import datetime
from enum import Enum

from PySide6.QtCore import QPoint
from PySide6.QtGui import QRegularExpressionValidator, Qt
from PySide6.QtWidgets import QMenu, QVBoxLayout, QWidget
from sqlalchemy import BinaryExpression, Column, or_

from app.core import Database
from app.core.func import set_completer_from_db
from app.data_module.filter_list_item import FilterListItem
from project_settings import BOOL_VIEW_DICT
from ui.ui_filters import Ui_FilterMenu


class FiltersMenu(QMenu):
    def __init__(self, table: type[Database.Model], parent: QWidget = None):
        super().__init__(parent)
        self._ui = Ui_FilterMenu()
        self._widget = QWidget()
        self._table = table
        self._accepted = False

        self.setup()

    def _get_filters(self):
        return [self._ui.filter_list.item(i) for i in range(self._ui.filter_list.count())]

    def execute(self, pos: QPoint):
        self.exec(pos)
        return (or_(*map(lambda i: i.filter, f)), ' или '.join(map(lambda i: i.text(), f))) \
            if (f := self._get_filters()) else None

    def setup_ui(self):
        ly = QVBoxLayout()
        ly.setContentsMargins(0, 0, 0, 0)
        self.setLayout(ly)
        self._ui.setupUi(self._widget)
        ly.addWidget(self._widget)
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        for col in self._table.__table__.columns:
            self._ui.cmb_column.addItem(col.comment if col.comment else col.name, userData=col)

        self._ui.i_num.setValidator(QRegularExpressionValidator(r"[0-9]+"))

    def accept(self):
        self._accepted = True
        self.close()

    def change_input_filter_type(self):
        col = self._ui.cmb_column.currentData()
        col_type = col.type.python_type

        self._ui.str.setVisible(col_type is str)
        self._ui.num.setVisible(col_type in (int, float))
        self._ui.date.setVisible(col_type in (datetime.date, datetime.datetime))
        self._ui.cmb_enum.setVisible(True)
        self._ui.cmb_enum.clear()

        if col_type is bool:
            for key, value in BOOL_VIEW_DICT.items():
                self._ui.cmb_enum.addItem(value, userData=key)

        elif issubclass(col_type, Enum):
            for enum in col_type:
                self._ui.cmb_enum.addItem(enum.value, userData=enum)

        else:
            self._ui.cmb_enum.setVisible(False)

    def setup_slots(self):
        self._ui.btn_add.clicked.connect(self.add_filter)
        self._ui.i_str.textEdited.connect(
            lambda: set_completer_from_db(self._ui.i_str, self._ui.cmb_column.currentData())
        )
        self._ui.cmb_column.currentIndexChanged.connect(self.change_input_filter_type)
        self._ui.btn_accept.clicked.connect(self.accept)
        self._ui.filter_list.itemClicked.connect(lambda: self._ui.filter_list.takeItem(self._ui.filter_list.currentRow()))

    def _add_filter_item(self, filter_: BinaryExpression, header: str):
        self._ui.filter_list.addItem(i := FilterListItem(filter_, header))
        i.setCheckState(Qt.CheckState.Checked)

    # noinspection PyTypeChecker
    def add_filter(self):
        col: Column = self._ui.cmb_column.currentData()
        col_type = col.type.python_type
        col_name = col.comment if col.comment else col.name

        if col_type is str:
            t: str = self._ui.i_str.text()
            match self._ui.c_str.currentIndex():
                case 0: self._add_filter_item(col.ilike(f"%{t}%"), f"{col_name} содержит '{t}'")
                case 1: self._add_filter_item(col.not_ilike(f"%{t}%"), f"{col_name} не содержит '{t}'")

        elif issubclass(col_type, Enum):
            self._add_filter_item(col == (e := self._ui.cmb_enum.currentData()), f"{col_name}={e.value}")

        elif col_type is bool:
            self._add_filter_item(col == self._ui.cmb_enum.currentData(), f"{col_name}={self._ui.cmb_enum.currentText()}")

        elif col_type in (int, float):
            t: int = int(self._ui.i_num.text())
            match self._ui.c_str.currentIndex():
                case 0: self._add_filter_item(col == t, f"{col_name} равно {t}")
                case 1: self._add_filter_item(col != t, f"{col_name} не равно {t}")
                case 2: self._add_filter_item(col > t, f"{col_name} больше {t}")
                case 3: self._add_filter_item(col < t, f"{col_name} меньше {t}")
                case 4: self._add_filter_item(col <= t, f"{col_name} не больше {t}")
                case 5: self._add_filter_item(col >= t, f"{col_name} не меньше {t}")

        elif col_type is (datetime.date, datetime.datetime):
            t: datetime.date = self._ui.i_date.date().toPython()
            match self._ui.c_str.currentIndex():
                case 0: self._add_filter_item(col == t, f"{col_name} равно {t}")
                case 1: self._add_filter_item(col != t, f"{col_name} не равно {t}")
                case 2: self._add_filter_item(col > t, f"{col_name} больше {t}")
                case 3: self._add_filter_item(col < t, f"{col_name} меньше {t}")
                case 4: self._add_filter_item(col <= t, f"{col_name} не больше {t}")
                case 5: self._add_filter_item(col >= t, f"{col_name} не меньше {t}")

    def setup(self):
        self.setup_ui()
        self.setup_slots()

        self.addAction(" " * 100)
        self._ui.cmb_column.setCurrentIndex(2)
        self._ui.cmb_column.setCurrentIndex(0)
