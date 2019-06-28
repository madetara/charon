from src._internal.archiver import archiver
from src._internal.telethon_ import dialogsource


def main():
    with dialogsource.TelegramDialogSource(1, "foo") as tds:
        archiver.execute(tds)
