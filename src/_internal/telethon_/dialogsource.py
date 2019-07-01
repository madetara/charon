import abc
from telethon.sync import TelegramClient
from typing import Iterable
from src._internal.telethon_.dialog import Dialog_, TelegramDialog


class DialogSource(abc.ABC):
    @abc.abstractmethod
    def getDialogs(self) -> Iterable[Dialog_]:
        pass


class TelegramDialogSource(DialogSource):
    def __init__(self, api_id: int, api_hash: str):
        self._client = TelegramClient(
            session=None, api_id=api_id, api_hash=api_hash).start()

    def __enter__(self):
        return self

    def __exit__(self, ecx_type, ecx_value, traceback):
        self._client.log_out()
        self._client.disconnect()

    def getDialogs(self) -> Iterable[Dialog_]:
        for dialog in self._client.iter_dialogs():
            yield TelegramDialog(dialog)
