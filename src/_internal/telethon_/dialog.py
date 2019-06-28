import abc
from datetime import date
from telethon.tl.custom import Dialog


class Dialog_(abc.ABC):
    @abc.abstractmethod
    def lastMessage(self) -> date:
        pass

    @abc.abstractmethod
    def archive(self):
        pass


class TelegramDialog(Dialog_):
    def __init__(self, dialog: Dialog):
        self._dialog = dialog

    def lastMessage(self) -> date:
        return self._dialog.date.date()

    def archive(self):
        self._dialog.archive()
