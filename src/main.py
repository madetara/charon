import archiver
import asyncio
from dialogsource import TelegramDialogSource

api_id = 0
api_hash = ""

if __name__ == "__main__":
    with TelegramDialogSource(api_id, api_hash) as dialogs:
        archiver.execute(dialogs)
