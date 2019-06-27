import abc
from telethon.sync import TelegramClient


class DialogSource(abc.ABC):
    @abc.abstractmethod
    def getDialogs(self):
        pass


class TelegramDialogSource(DialogSource):
    def __init__(self, api_id, api_hash):
        self.__client = TelegramClient('anon', api_id, api_hash)

    def __enter__(self):
        return self

    def __exit__(self, ecx_type, ecx_value, traceback):
        self.__client.disconnect()

    def getDialogs(self):
        return self.__client.iter_dialogs()


class MockDialogSource(DialogSource):
    def __init__(self, dialogs: list):
        self.__dialogs = dialogs

    def getDialogs(self):
        return self.__dialogs
