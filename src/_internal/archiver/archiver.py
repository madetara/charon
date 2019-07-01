import datetime
from logging import Logger
from src._internal.telethon_.dialogsource import DialogSource, Dialog_
from typing import Callable


def execute(source: DialogSource,
            log: Logger,
            folder: int = 1,
            time_limit_days: int = 15,
            filter_: Callable[[Dialog_], bool] = lambda x: True):
    log.info('Starting archiving chats.')

    today = datetime.date.today()
    total_archived = 0

    for dialog in filter(filter_, source.getDialogs()):
        last_message_date = dialog.lastMessage()

        if (today - last_message_date).days >= time_limit_days:
            log.info('- moving' + ' ' + dialog.name)
            dialog.archive(folder)
            total_archived += 1

    print('Total ' + str(total_archived) + ' chats moved.')
