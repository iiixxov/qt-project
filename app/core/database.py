from typing import Iterable

from sqlalchemy import create_engine, Integer, MetaData, Table, Column, ForeignKey, literal_column, text, event, DDL
from sqlalchemy.orm import sessionmaker, Session, DeclarativeBase, Mapped, declarative_base, mapped_column

from project_settings import SQL_DIALECT
from . import Settings


class Database:
    engine: create_engine
    session: Session
    Base: DeclarativeBase = declarative_base(metadata=MetaData())

    @classmethod
    def create_secondary_table(cls, parent: str, children: 'Model'):
        return Table(
            f"_Association_{parent}_{children.__name__}",
            cls.Base.metadata,
            Column("left_id", ForeignKey(parent + '.id')),
            Column("right_id", ForeignKey(children.id)),
        )

    @classmethod
    def create_all(cls):
        for mapper in cls.Base.registry.mappers:
            cls_ = mapper.class_
            if issubclass(cls_, cls.Model):
                table_args = getattr(cls_, '__table_args__', None)
                if table_args:
                    schema = table_args.get('schema')
                    if schema:
                        stmt = f"CREATE SCHEMA IF NOT EXISTS {schema}"
                        event.listen(cls.Base.metadata, 'before_create', DDL(stmt))
        cls.Base.metadata.create_all(cls.engine)

    @classmethod
    def login(cls, username: str, password: str) -> Exception:
        try:
            cls.init_from_engine(create_engine(
                f"{SQL_DIALECT}://"
                f"{username}:{password}@"
                f"{Settings['_database']['host']}:{Settings['_database']['port']}/"
                f"{Settings['_database']['db_name']}",
                connect_args=Settings['_database']['connect_args']
            ))
        except Exception as e:
            return e

    @classmethod
    def init_from_engine(cls, engine: create_engine):
        if hasattr(cls, 'session'):
            cls.session.close()
        cls.engine = engine
        cls.session = sessionmaker(bind=cls.engine)()
        cls.engine.connect().close()
        cls.update_comments()
        cls.create_all()
        # noinspection PyTypeChecker
        cls.user = cls.make_user(cls.session.query(literal_column("current_user")).one()[0])

    class Model(Base):
        __abstract__ = True
        __table_args__ = {"schema": "main"}
        id: Mapped[int] = mapped_column(Integer, primary_key=True, comment="Номер")

        def __init_subclass__(cls, **kwargs):
            if not hasattr(cls, '__tablename__'):
                cls.__tablename__ = cls.__name__

        def __getitem__(self, key: str, *keys: str):
            """ instance['field.attached_field'] """
            obj = self
            for attr_name in key.split('.'):
                obj = obj.__getattribute__(attr_name)
            for attr_name in keys:
                obj = obj.__getattribute__(attr_name)
            return obj

        def __setitem__(self, key: str, value):
            """ instance['field.attached_field']  = value"""
            key = key.split('.')
            if len(key) == 1:
                self.__setattr__(key[0], value)
            else:
                self[*key[:-1]].__setattr__(key[-1], value)

        @classmethod
        def update_comments(cls):
            virtual_table = Table(
                cls.__tablename__,
                Database.Base.metadata,
                schema=cls.__table__.schema,
                autoload_with=Database.engine
            )
            cls.__table__.comment = virtual_table.comment
            # noinspection PyTypeChecker
            for col in virtual_table.columns:
                cls.__table__.columns[col.name].comment = col.comment

        @classmethod
        def cols_without(cls, *names: str):
            # noinspection PyTypeChecker
            return [col for col in cls.__table__.columns if col.name not in names]

        def all_instances(self):
            any_ = []
            for d in type(self).__dict__.keys():
                value = self.__getattribute__(d)
                if isinstance(value, Iterable):
                    for i in value:
                        if hasattr(i, 'all_instances'):
                            any_ += [i, *i.all_instances()]
                if hasattr(value, 'all_instances'):
                    any_ += [value, *value.all_instances()]
            return any_

        def get_or_create(self):
            for i in self.all_instances():
                i.get_or_create()
            if self.id is None and (
                    id_ := Database.session.query(type(self).id).filter_by(**{n: v for n, v in self}).first()):
                self.id = id_[0]

    @classmethod
    def update_comments(cls):
        for table in cls.Model.registry.mappers:
            model: cls.Model = table.class_
            model.update_comments()

    class _User:
        def __init__(self, name: str):
            self._name = name

        @property
        def name(self):
            return self._name

        def change_password(self, new_password: str):
            Database.session.execute(
                text(f"ALTER USER \"{self.name}\" WITH PASSWORD :new_password"),
                {'new_password': new_password}
            )

    @classmethod
    def make_user(cls, username: str):
        return cls._User(name=username)

    user: _User
