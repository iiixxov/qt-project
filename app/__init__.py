from .orm import *
from .core import App, Module


from .data_module import DataModule
from .settings_module import SettingsModule
from .users_module import UsersModule
from .profile_module import ProfileModule
from .notifications_module import NotificationsModule

# main
App.register_module(DataModule)
App.register_module(UsersModule)
App.register_module(SettingsModule)

# tray
App.register_module(ProfileModule)
App.register_module(NotificationsModule)
