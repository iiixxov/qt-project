from abc import abstractmethod
from typing import Sequence

from app import Bookmark, Folder
from app.core import Database
from .data_submodule import DataSubmodule
from app.data_module.tree_items import BookmarkTreeItem, FolderTreeItem
from project_settings import ICONS_PATH
from ..query_request import QueryRequest


class BookmarkSubmodule(DataSubmodule):
    def __init__(self, app, data_module):
        super().__init__(app, data_module)

    def icon_path(self) -> str:
        return ICONS_PATH + 'Bookmark-b.svg'

    def visible_name(self) -> str:
        return "Справочники"

    def load(self) -> Sequence[BookmarkTreeItem]:
        for table in Database.Model.registry.mappers:
            model = table.class_

            if issubclass(model, Bookmark):
                item = BookmarkTreeItem(model, self)
                for folder in Database.session.query(Folder).join(model).filter(Folder.folder_id == None).all():
                    folder: Folder
                    item.addChild(FolderTreeItem(folder, self))

                yield item

    @abstractmethod
    def get_query(self, clicked_item: BookmarkTreeItem | FolderTreeItem) -> QueryRequest:
        if isinstance(clicked_item, (BookmarkTreeItem, FolderTreeItem)):
            Bookmark_: type[Bookmark] = clicked_item.bookmark
            return QueryRequest(
                query=Database.session.query(Bookmark_), model=Bookmark_, filter_=(
                    Bookmark_.folder_id == clicked_item.folder.id if isinstance(clicked_item, FolderTreeItem) else None
                ))
