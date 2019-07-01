import abc
from datetime import date
from telethon.tl.custom import Dialog


class Dialog_(abc.ABC):
    @abc.abstractmethod
    def lastMessage(self) -> date:
        pass

    @abc.abstractmethod
    def archive(self, folder: int = 1):
        pass

    @abc.abstractmethod
    def archived(self) -> bool:
        pass

    @abc.abstractproperty
    def name(self) -> str:
        pass

    @abc.abstractproperty
    def isBot(self) -> bool:
        pass

    @abc.abstractproperty
    def isPinned(self) -> bool:
        pass


class TelegramDialog(Dialog_):
    def __init__(self, dialog: Dialog):
        self._dialog = dialog

    def lastMessage(self) -> date:
        return self._dialog.date.date()

    def archive(self, folder: int = 1):
        self._dialog.archive(folder)

    def archived(self) -> bool:
        return self._dialog.archived()

    @property
    def name(self) -> str:
        return self._dialog.name

    @property
    def isBot(self) -> bool:
        return self._dialog.is_user and self._dialog.entity.bot

    @property
    def isPinned(self) -> bool:
        return self._dialog.pinned
