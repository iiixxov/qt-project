from PySide6.QtWidgets import QLabel, QSpacerItem, QSizePolicy, QWidget

from project_settings import ICONS_PATH
from .func import get_settings_edit_widget, get_value
from .settings_item import SettingsItem
from ..core import Settings, func, SettingsTranslate
from ..core.module import Module
from ui.ui_settings import Ui_Form


class SettingsModule(Module):
    _ui: Ui_Form

    def __init__(self, parent: QWidget, app):
        super().__init__(parent, app)
        self._cur_dict: dict[str: get_settings_edit_widget] = {}

    def icon_path(self) -> str:
        return ICONS_PATH + 'settings.svg'

    def visible_name(self) -> str:
        return 'Настройки'

    def _ui_class(self) -> type:
        return Ui_Form

    def setup(self):
        super().setup()
        self._ui.settings_tree.setColumnWidth(0, Settings['_sizes']['settings_tree_section'])

        self._ui.settings_tree.itemClicked.connect(self.make_settings_layout)
        self._ui.btn_save.clicked.connect(self.save)

        self.load_settings()

    def save(self):
        cur_item: SettingsItem = self._ui.settings_tree.currentItem()
        Settings.set(
            *cur_item.keys, value={key: get_value(edit) for key, edit in self._cur_dict.items()}
        )
        Settings.save()

    def load_settings(self):
        self._ui.settings_tree.clear()
        for key, value in Settings.to_dict().items():
            not key.startswith('_') and isinstance(value, dict) and self.add_settings_item(key, value)

    def add_settings_item(self, key: str, value: dict):
        self._ui.settings_tree.addTopLevelItem(item := SettingsItem(key))
        for key, value in value.items():
            not key.startswith('_') and isinstance(value, dict) and self.add_child_settings_item(key, value, item)

    def add_child_settings_item(self, key: str, value: dict, item: SettingsItem):
        item.addChild(new_item := SettingsItem(key))
        for key, value in value.items():
            not key.startswith('_') and isinstance(value, dict) and self.add_child_settings_item(key, value, new_item)

    def make_settings_layout(self, item: SettingsItem):
        settings = Settings.get(*item.keys)

        i = 0
        func.clear_layout(self._ui.settings_layout.layout())
        self._cur_dict.clear()
        for key, value in settings.items():
            if isinstance(value, dict):
                continue

            self._cur_dict[key] = (w := get_settings_edit_widget(value))
            key = '.'.join([*item.keys, key])
            text = SettingsTranslate[key] if SettingsTranslate.has(key) else key

            self._ui.settings_layout.layout().addWidget(QLabel(text), i, 0)
            self._ui.settings_layout.layout().addWidget(w, i, 1)
            i += 1

        self._ui.settings_layout.layout().addItem(
            QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding), i, 1
        )
