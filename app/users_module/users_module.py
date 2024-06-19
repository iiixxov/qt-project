from project_settings import ICONS_PATH
from ..core.module import Module
from ui.empty_ui import EmptyUi


class UsersModule(Module):
    _ui: EmptyUi

    def icon_path(self) -> str:
        return ICONS_PATH + 'user.svg'

    def visible_name(self) -> str:
        return 'Пользователи'

    def _ui_class(self) -> type:
        return EmptyUi
