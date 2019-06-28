import logging
import click
from src._internal.archiver import archiver
from src._internal.telethon_ import dialogsource


@click.group()
def charon():
    pass


@charon.command()
@click.option('--id', required=True, type=int, prompt="App id",
              # hide_input=True,
              help="Your telegram app-id (DO NOT SHARE)")
@click.option('--hash', required=True, type=str, prompt="Api hash",
              # hide_input=True,
              help="Your telegram api-hash (DO NOT SHARE)")
@click.option('-d', '--days', type=int, default=15,
              help="Chat with last message elder than <days> will be archived")
@click.option('-p', is_flag=True,
              help="When active will also archive pinned chats")
def archive(**kwargs):
    app_id = kwargs['id']
    api_hash = kwargs['hash']
    logging.basicConfig(level=logging.INFO)
    with dialogsource.TelegramDialogSource(app_id, api_hash) as tds:
        try:
            archiver.execute(tds,
                             logging.getLogger("archiver"),
                             time_limit_days=kwargs['days'],
                             filter_=lambda d: (d.isPinned == kwargs['p'])
                             or kwargs['p'])
        except ConnectionError as e:
            log = logging.getLogger()
            log.error(
                'Error while trying to establish connection: {0}'.format(e)
            )
