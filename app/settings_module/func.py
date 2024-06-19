from typing import List

from PySide6 import QtWidgets


def get_settings_edit_widget(value: object):
    if isinstance(value, bool):
        edit = QtWidgets.QCheckBox()
        edit.setChecked(value)
        return edit

    elif isinstance(value, int):
        edit = QtWidgets.QSpinBox()
        edit.setMinimum(-999_999_999)
        edit.setMaximum(999_999_999)
        edit.setValue(value)
        return edit

    elif isinstance(value, float):
        edit = QtWidgets.QDoubleSpinBox()
        edit.setMinimum(-999_999_999)
        edit.setMaximum(999_999_999)
        edit.setValue(value)
        return edit

    elif isinstance(value, str):
        return QtWidgets.QLineEdit(value)


def get_value(widget: get_settings_edit_widget):
    if isinstance(widget, (QtWidgets.QSpinBox, QtWidgets.QDoubleSpinBox)):
        return widget.value()

    elif isinstance(widget, QtWidgets.QLineEdit):
        return widget.text()

    elif isinstance(widget, QtWidgets.QCheckBox):
        return widget.isChecked()

