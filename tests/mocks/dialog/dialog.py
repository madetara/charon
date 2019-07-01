from datetime import date
from src._internal.telethon_.dialog import Dialog_


class DialogMock(Dialog_):
    def __init__(self,
                 last_message: date,
                 archived: bool = False,
                 bot: bool = False,
                 pinned: bool = False,
                 name: str = "Mocked dialog"):
        self._last_message = last_message
        self._archived = archived
        self._name = name
        self._bot = bot
        self._pinned = pinned

    def lastMessage(self) -> date:
        return self._last_message

    def archive(self, folder: int = 1):
        self._archived = not self._archived

    def archived(self) -> bool:
        return self._archived

    @property
    def name(self) -> str:
        return self._name

    @property
    def isBot(self) -> bool:
        return self._bot

    @property
    def isPinned(self) -> bool:
        return self._pinned
