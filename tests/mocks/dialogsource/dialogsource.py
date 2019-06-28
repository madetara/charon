from typing import List, Iterable
from src._internal.telethon_.dialog import Dialog_
from src._internal.telethon_.dialogsource import DialogSource


class DialogSourceMock(DialogSource):
    def __init__(self, dialogs: List[Dialog_]):
        self._dialogs = dialogs

    def getDialogs(self) -> Iterable[Dialog_]:
        for dialog in self._dialogs:
            yield dialog
