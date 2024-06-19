from typing import List

from sqlalchemy.exc import OperationalError


class Error:
    _instances: List['Error'] = []

    def __init__(self, exception_class: type[Exception], text_like: str, header_text: str):
        self._exception_class = exception_class
        self._text_like = text_like
        self._header_text = header_text

    @property
    def header(self) -> str:
        return self._header_text

    @classmethod
    def register(cls, instance: 'Error'):
        cls._instances.append(instance)

    @classmethod
    def get(cls, exception: Exception) -> 'Error':
        for instance in cls._instances:
            if isinstance(exception, instance._exception_class) and instance._text_like in str(exception):
                return instance

    @classmethod
    def to_str(cls, exception: Exception):
        return f"{cls.get(exception).header}\n\n({exception})"


Error.register(Error(OperationalError, "", "Неудачная попытка входа"))
Error.register(Error(Exception, "", "Ошибка"))
