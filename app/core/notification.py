from enum import Enum


class NotificationTypeEnum(Enum):
    default = "Уведомление"
    info = "Инфо"
    error = "Ошибка"
    message = "Сообщение"
    success = "Успех"
    command = "Команда"


NOTIFICATION_ICONS = {
    NotificationTypeEnum.default: "Notification-b.svg",
    NotificationTypeEnum.info: "Info-b.svg",
    NotificationTypeEnum.error: "Cancel-b.svg",
    NotificationTypeEnum.message: "Speech Bubble-b.svg",
    NotificationTypeEnum.success: "Check Mark-b.svg",
    NotificationTypeEnum.command: "script-b.svg"
}
