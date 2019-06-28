import datetime
from src._internal.telethon_.dialogsource import DialogSource, Dialog_
from typing import Callable


def execute(source: DialogSource, time_limit_days: int = 15,
            filter_: Callable[[Dialog_], bool] = lambda x: True):
    print('Starting archiving chats.', flush=True)

    today = datetime.date.today()
    total_archived = 0

    for dialog in filter(filter_, source.getDialogs()):
        last_message_date = dialog.date.date()

        if (today - last_message_date).days > time_limit_days:
            print('- archiving ' + str(dialog.name.encode('utf-8')),
                  flush=True)
            dialog.archive()
            total_archived += 1

    print('Total ' + str(total_archived) + ' chats archived.')
