import logging
import click
from src._internal.archiver import archiver
from src._internal.telethon_ import dialogsource


@click.group()
def charon():
    """
    Helps you handle old chats by automatically archiving them.
    Requires telegram app_id and api_hash to work
    """
    pass


@charon.command()
@click.option('--id', required=True, type=int, prompt="App id",
              hide_input=True,
              help="Your telegram app-id (DO NOT SHARE)")
@click.option('--hash', required=True, type=str, prompt="Api hash",
              hide_input=True,
              help="Your telegram api-hash (DO NOT SHARE)")
@click.option('-d', '--days', type=int, default=15,
              help="Chat with last message elder than <days> will be archived")
@click.option('-p', is_flag=True,
              help="When active will also archive pinned chats")
def archive(**kwargs):
    """
    Archives chats inactive for specified amount of days
    """
    kwargs['folder'] = 1
    _move_chats(**kwargs)


@charon.command()
@click.option('--id', required=True, type=int, prompt="App id",
              hide_input=True,
              help="Your telegram app-id (DO NOT SHARE)")
@click.option('--hash', required=True, type=str, prompt="Api hash",
              hide_input=True,
              help="Your telegram api-hash (DO NOT SHARE)")
def unarchive(**kwargs):
    """
    Unarchives ALL chats
    """
    kwargs['folder'] = 0
    _move_chats(**kwargs)


def _move_chats(**kwargs):
    folder = kwargs['folder']
    app_id = kwargs['id']
    api_hash = kwargs['hash']
    time_limit_days = kwargs['days'] if 'days' in kwargs else -1
    logging.basicConfig(level=logging.INFO)
    with dialogsource.TelegramDialogSource(app_id, api_hash) as tds:
        try:
            archiver.execute(tds,
                             logging.getLogger("archiver"),
                             folder=folder,
                             time_limit_days=time_limit_days,
                             filter_=_build_filter(**kwargs))
        except ConnectionError as e:
            log = logging.getLogger()
            log.error(
                'Error while trying to establish connection: {0}'.format(e)
            )


def _build_filter(**kwargs):
    if kwargs['folder'] == 0:
        return lambda d: True
    return lambda d: (d.isPinned == kwargs['p']) or kwargs['p']
