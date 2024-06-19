from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QTreeWidgetItem

from app import Bookmark, Folder
from app.core import Database
from .submodules import DataSubmodule
from project_settings import ICONS_PATH, FOLDER_ICON, TABLE_ICON


class DataModuleTreeItem(QTreeWidgetItem):
    def __init__(self, module: DataSubmodule):
        super().__init__()
        self.setIcon(0, QIcon(module.icon_path()))
        self.setText(0, module.visible_name())
        self._module = module

    @property
    def module(self):
        return self._module


class TableTreeItem(DataModuleTreeItem):
    def __init__(self, table: type[Database.Model], module: DataSubmodule):
        super().__init__(module)
        self.setIcon(0, QIcon(ICONS_PATH + TABLE_ICON))
        self.setText(0, table.__table__.comment if table.__table__.comment else table.__table__.name)
        self._table = table

    @property
    def table(self):
        return self._table


class BookmarkTreeItem(DataModuleTreeItem):
    def __init__(self, bookmark: type[Bookmark], module: DataSubmodule):
        super().__init__(module)
        self.setIcon(0, QIcon(ICONS_PATH + bookmark.ICON_PATH))
        self.setText(0, bookmark.__table__.comment if bookmark.__table__.comment else bookmark.__table__.name)
        self._bookmark = bookmark

    @property
    def bookmark(self) -> type[Bookmark]:
        return self._bookmark


class FolderTreeItem(DataModuleTreeItem):
    def __init__(self, folder: Folder, module: DataSubmodule):
        super().__init__(module)
        self.setIcon(0, QIcon(ICONS_PATH + FOLDER_ICON))
        self.setText(0, folder.name)
        self._folder = folder

        self._setup()

    @property
    def bookmark(self) -> type[Bookmark]:
        parent: FolderTreeItem | BookmarkTreeItem | QTreeWidgetItem = self
        while not isinstance((parent := parent.parent()), BookmarkTreeItem): pass
        return parent.bookmark

    @property
    def folder(self):
        return self._folder

    def _setup(self):
        for folder in self._folder.children_folders:
            self.addChild(FolderTreeItem(folder, self.module))
