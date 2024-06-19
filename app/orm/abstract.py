from sqlalchemy import VARCHAR, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship, declared_attr

from . import Folder
from app.core import Database
from project_settings import BOOKMARK_ICON, TABLE_ICON


class Bookmark(Database.Model):
    __table_args__ = {"schema": "bookmarks", "comment": "Справочник"}
    __abstract__ = True

    name: Mapped[str] = mapped_column(VARCHAR, default="Новая запись", comment="Заголовок")
    folder_id: Mapped[int] = mapped_column(ForeignKey(Folder.id), nullable=True)

    @declared_attr
    def folder(self) -> Mapped[Folder]:
        return relationship(Folder)

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.__tablename__ = cls.__name__
        if hasattr(cls, '__table_args__'):
            cls.__table_args__['schema'] = 'bookmarks'
        else:
            cls.__table_args__ = {"schema": "bookmarks"}

    ICON_PATH = BOOKMARK_ICON


class Table(Database.Model):
    __table_args__ = {"schema": "tables", "comment": "Таблица"}
    __abstract__ = True

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.__tablename__ = cls.__name__
        if hasattr(cls, '__table_args__'):
            cls.__table_args__['schema'] = 'tables'
        else:
            cls.__table_args__ = {"schema": "tables"}

    ICON_PATH = TABLE_ICON
