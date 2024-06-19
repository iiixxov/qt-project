from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtWidgets import QMessageBox, QDialog, QVBoxLayout, QLabel, QLineEdit, QDialogButtonBox, QApplication, \
    QWidget


def error_box(text: str):
    QMessageBox(QMessageBox.Icon.Critical, "Ошибка", text).exec()


def info_box(text: str):
    QMessageBox(QMessageBox.Icon.Information, "Инфо", text).exec()


def input_box(*names, password_type=False, re_validator: str, parent: QWidget) -> list[str]:
    dialog = QDialog(parent)
    dialog.setWindowTitle("Ввод данных")
    dialog.setModal(True)
    layout = QVBoxLayout(dialog)
    line_edits = []
    for name in names:
        line_edit = QLineEdit()
        if password_type:
            line_edit.setEchoMode(QLineEdit.EchoMode.Password)
        if re_validator:
            line_edit.setValidator(QRegularExpressionValidator(re_validator))
        layout.addWidget(QLabel(name))
        layout.addWidget(line_edit)
        line_edits.append(line_edit)
    button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
    button_box.setCenterButtons(True)
    layout.addWidget(button_box)
    button_box.accepted.connect(dialog.accept)
    button_box.rejected.connect(dialog.reject)
    if dialog.exec() == QDialog.DialogCode.Accepted:
        return [line_edit.text() for line_edit in line_edits]
    return []


def confirm_box(text):
    msg_box = QMessageBox()
    msg_box.setWindowTitle('Подтвердить?')
    msg_box.setText(text)
    msg_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
    msg_box.setDefaultButton(QMessageBox.StandardButton.No)
    msg_box.button(QMessageBox.StandardButton.Yes).setText("Да")
    msg_box.button(QMessageBox.StandardButton.No).setText("Нет")

    return msg_box.exec() == QMessageBox.StandardButton.Yes


def confirm_decorator(text):
    def decorator(func):
        def wrapper(*args, confirm=True, **kwargs):
            if confirm:
                confirm_box(text) and func(*args, **kwargs)
            else:
                func(*args, **kwargs)
        return wrapper
    return decorator


def response_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            error_box(str(e))
    return wrapper


if __name__ == "__main__":
    app = QApplication([])
    app.exec()
