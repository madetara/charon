from telethon.sync import TelegramClient
from dialogsource import DialogSource
import datetime


def unarchive(api_id, api_hash):
    with TelegramClient('anon', api_id, api_hash) as client:
        for dialog in client.iter_dialogs():
            print('foo', flush=True)
            dialog.archive(folder=0)


def execute(source: DialogSource, timeLimitDays: int = 15):
    print('Starting archiving chats.', flush=True)

    today = datetime.date.today()
    total_archived = 0

    for dialog in source.getDialogs():
        if skip_archiving(dialog):
            continue

        last_message_date = dialog.date.date()

        if (today - last_message_date).days > timeLimitDays:
            print('- archiving ' + str(dialog.name.encode('utf-8')), flush=True)
            dialog.archive()
            total_archived += 1

    print('Total ' + str(total_archived) + ' chats archived.')


def skip_archiving(dialog):
    return dialog.archived or dialog.pinned
