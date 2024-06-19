from PySide6.QtWidgets import QLayout, QLayoutItem, QLineEdit, QCompleter
import secrets
from base64 import urlsafe_b64encode as b64e, urlsafe_b64decode as b64d
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from sqlalchemy import Column


backend = default_backend()
iterations = 100_000


def _derive_key(password: bytes, salt: bytes, iters: int = iterations) -> bytes:
    """Derive a secret key from a given password and salt"""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(), length=32, salt=salt,
        iterations=iters, backend=backend)
    return b64e(kdf.derive(password))


def password_encrypt(message: bytes, password: bytes, iters: int = iterations) -> bytes:
    salt = secrets.token_bytes(16)
    key = _derive_key(password, salt, iters)
    return b64e(
        b'%b%b%b' % (
            salt,
            iters.to_bytes(4, 'big'),
            b64d(Fernet(key).encrypt(message)),
        )
    )


def password_decrypt(token: bytes, password: bytes) -> bytes:
    decoded = b64d(token)
    salt, iteration, token = decoded[:16], decoded[16:20], b64e(decoded[20:])
    iters = int.from_bytes(iteration, 'big')
    key = _derive_key(password, salt, iters)
    return Fernet(key).decrypt(token)


def css_vars_to_dict(filepath: str) -> dict[str: str]:
    """ return css :root vars to dict['--var': 'value'] """

    with open(filepath, 'r') as style_file:
        stylesheet = style_file.read()

    values = {}
    if ":root" in stylesheet:
        for line in stylesheet[stylesheet.find('{') + 1: stylesheet.find('}')].split(';')[:-1]:
            var, val = line.replace('\n', '').replace(' ', '').split(':')
            values[var] = val

    return values


def css_format(filepath: str) -> str:
    """ return stylesheet to widgets from scc file:
        replacing :root vars in code """

    with open(filepath, 'r') as style_file:
        stylesheet = style_file.read()

    if ":root" in stylesheet:
        stylesheet = stylesheet[stylesheet.find('}') + 1:]

    for var, val in css_vars_to_dict(filepath).items():
        stylesheet = stylesheet.replace(f"var({var})", val)

    return stylesheet


def clear_layout(layout: QLayout):
    """ delete all children widgets and him widgets later """
    while layout.count():
        item: QLayoutItem = layout.takeAt(0)
        if item.widget():
            item.widget().deleteLater()
        elif item.layout():
            clear_layout(item.layout())


def set_completer_from_db(line: QLineEdit, column: Column):
    from app.core import Database

    completer = QCompleter(
        [text[0] for text in Database.session.query(column).filter(column.ilike(f"%{line.text()}%")).limit(5).distinct()]
    )
    completer.setCompletionMode(QCompleter.CompletionMode.UnfilteredPopupCompletion)
    line.setCompleter(completer)

