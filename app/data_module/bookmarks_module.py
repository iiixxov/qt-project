from PySide6.QtCore import QPoint
from PySide6.QtWidgets import QWidget, QMenu

from project_settings import ICONS_PATH
from ui.ui_folders_tools import Ui_TablesToolBar
from ui.ui_forders import Ui_TableSMWidget
from app.data_module.tree_items import BookmarkTreeItem, FolderTreeItem
from app.data_module import TableSubModule
from app import Bookmark, Folder
from app.core import Database, input_box


class BookmarksSubModule(TableSubModule):
    _tool_ui: Ui_TablesToolBar
    _table_ui: Ui_TableSMWidget

    def __init__(self, parent: QWidget, app, data_module):
        super().__init__(parent, app, data_module)

    def _table_ui_class(self) -> type:
        return Ui_TableSMWidget

    def icon_path(self) -> str:
        return ICONS_PATH + 'Bookmark-b.svg'

    def visible_name(self) -> str:
        return "Справочники"

    def _tool_ui_class(self) -> type:
        return Ui_TablesToolBar

    def setup(self):
        super().setup()

    def _fill(self):
        first_item = None

        for model in self._tables:
            if issubclass(model, Bookmark):
                self._table_ui.trw_folders.addTopLevelItem(it := BookmarkTreeItem(model))

                if first_item is None: first_item = it
                for folder in Database.session.query(Folder).join(Bookmark).filter(Folder.folder_id == None).all():
                    folder: Folder
                    it.addChild(FolderTreeItem(folder))

        self._table_ui.trw_folders.setCurrentItem(first_item)

    def _connect_slots(self):
        self._table_ui.trw_folders.itemClicked.connect(lambda i: self._item_clicked(i))
        self._table_ui.trw_folders.customContextMenuRequested.connect(self.show_tree_context_menu)

    @staticmethod
    def models_columns(model: type[Database.Model]):
        return model.cols_without('id', 'folder_id')

    def change_table_from_bookmark(self, bookmark: type[Bookmark]):
        for i, model in enumerate(self._tables):
            if model is bookmark:
                self.change_table(i)

    def _get_filters(self):
        item = self._table_ui.trw_folders.selectedItems()[0]
        if isinstance(item, FolderTreeItem):
            return [Bookmark.folder_id == item.folder.id]
        else:
            return [Bookmark.folder_id == None]

    def _item_clicked(self, item: BookmarkTreeItem | FolderTreeItem):
        self.change_table_from_bookmark(item.bookmark)

    def show_tree_context_menu(self, pos: QPoint):
        item = self._table_ui.trw_folders.selectedItems()[0]
        menu = QMenu(self._table_widget)

        (menu.addAction("Создать папку")).triggered.connect(self.create_folder)

        if isinstance(item, FolderTreeItem):
            (menu.addAction("Переименовать")).triggered.connect(self.rename_folder)

        menu.exec(self._table_ui.trw_folders.mapToGlobal(pos))

    def create_folder(self):
        if folder_name := input_box('Название папки', parent=self._table_widget):
            folder_name = folder_name[0]
            item = self._table_ui.trw_folders.selectedItems()[0]
            try:
                Database.session.add(item.bookmark(
                    folder=Folder(name=folder_name, folder=item.folder)
                    if isinstance(item, FolderTreeItem) else Folder(name=folder_name)
                ))
                Database.session.flush()
            except Exception as e:
                self._app.couch(e)
                Database.session.rollback()
            Database.session.commit()

    def rename_folder(self):
        if folder_name := input_box('Название папки', parent=self._table_widget):
            folder_name = folder_name[0]
            item: FolderTreeItem = self._table_ui.trw_folders.selectedItems()[0]
            try:
                item.folder.name = folder_name
                Database.session.flush()
            except Exception as e:
                self._app.couch(e)
                Database.session.rollback()
            Database.session.commit()



