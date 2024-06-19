from typing import List

from PySide6.QtWidgets import QTreeWidgetItem

from app.core import SettingsTranslate


class SettingsItem(QTreeWidgetItem):
    def __init__(self, key: str):
        super().__init__()
        self._key = key

        text = SettingsTranslate['.'.join(self.keys)] if SettingsTranslate.has('.'.join(self.keys)) else key
        self.setText(0, text)

    @property
    def key(self):
        return self._key

    @property
    def keys(self) -> list[str]:
        parent_keys: List[str] = [self.key]
        parent: SettingsItem = self

        while isinstance(parent := parent.parent(), SettingsItem):
            parent_keys.append(parent.key)

        return list(reversed(parent_keys))
