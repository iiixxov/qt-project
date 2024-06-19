from typing import List

from sqlalchemy import Enum, VARCHAR, Boolean, TIMESTAMP, func, ForeignKey, Integer
from sqlalchemy.orm import mapped_column, Mapped, relationship

from app.core import Database
from app.core.notification import NotificationTypeEnum

notification_enum = Enum(NotificationTypeEnum, schema='core')


class Notification(Database.Model):
    __table_args__ = {"schema": "core", "comment": "Уведомления"}

    type: Mapped[NotificationTypeEnum] = mapped_column(notification_enum, default=NotificationTypeEnum.default)
    created_at = mapped_column(TIMESTAMP, default=func.current_timestamp)
    header: Mapped[str] = mapped_column(VARCHAR, default="")
    body: Mapped[str] = mapped_column(VARCHAR, default="")
    to_user: Mapped[str] = mapped_column(VARCHAR, default="")
    is_impotent: Mapped[bool] = mapped_column(Boolean, default=False)
    is_popup: Mapped[bool] = mapped_column(Boolean, default=False)


class Folder(Database.Model):
    __table_args__ = {"schema": "core", "comment": "Папки"}

    id: Mapped[int] = mapped_column(Integer, primary_key=True, comment="Номер")
    name: Mapped[str] = mapped_column(VARCHAR, default="Новая папка")
    folder_id: Mapped[int] = mapped_column(ForeignKey(id), comment="Номер папки", nullable=True)

    parent_folder: Mapped['Folder'] = relationship('Folder', remote_side=[id], back_populates='children_folders')
    children_folders: Mapped[List['Folder']] = relationship('Folder', back_populates='parent_folder')
