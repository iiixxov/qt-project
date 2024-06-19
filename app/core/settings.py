import json

from project_settings import USER_SETTINGS_PATH, JSON_INDENT, USER_SETTINGS_TRANSLATE_PATH


class __SettingsMeta(type):
    data: json.load

    def __getitem__(cls, key: str):
        return cls.data[key]

    def __setitem__(cls, key: str, value):
        cls.data[key] = value

    def has(cls, *keys: str):
        try:
            cls.get(*keys)
            return True
        except KeyError:
            return False

    def get(cls, *keys: str):
        data = cls.data
        for key in keys: data = data[key]
        return data

    def set(cls, *keys: str, value):
        data = cls.data
        for key in keys[:-1]: data = data[key]
        data[keys[-1]] = value

    def save(cls):
        with open(USER_SETTINGS_PATH, 'w') as f:
            json.dump(cls.data, f, indent=JSON_INDENT)

    def load(cls):
        with open(USER_SETTINGS_PATH) as f:
            cls.data = json.load(f)

    def to_dict(cls) -> dict:
        return cls.data


class Settings(metaclass=__SettingsMeta):
    with open(USER_SETTINGS_PATH) as f:
        data = json.load(f)


class SettingsTranslate(metaclass=__SettingsMeta):
    with open(USER_SETTINGS_TRANSLATE_PATH) as f:
        data = json.load(f)
