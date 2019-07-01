import logging
from datetime import date, MINYEAR, timedelta
from typing import Iterable
from src._internal.archiver import archiver
from tests.mocks.dialogsource.dialogsource import DialogSourceMock
from tests.mocks.dialog.dialog import DialogMock


class TestArchive(object):
    def _generate_dialogs(self, count: int, date_: date) -> Iterable[DialogMock]:
        for _ in range(count):
            yield DialogMock(date_)

    def test_archive_all_old_dialogs_when_no_filter(self):
        dialog_count = 10

        dialogs = list(self._generate_dialogs(
            dialog_count, date(MINYEAR, 1, 1)))
        tds = DialogSourceMock(dialogs)
        archiver.execute(tds, logging.getLogger("Test"))

        archived = 0
        for dialog in dialogs:
            assert dialog.archived() == True
            archived += 1
        assert archived == dialog_count

    def test_not_archive_new_dialogs(self):
        dialog_count = 10

        dialogs = list(self._generate_dialogs(dialog_count, date.today()))
        tds = DialogSourceMock(dialogs)
        archiver.execute(tds, logging.getLogger("Test"))

        for dialog in dialogs:
            assert dialog.archived() == False

    def test_ignore_old_dialogs_with_filter(self):
        dialog_count = 10

        dialogs = list(self._generate_dialogs(
            dialog_count, date(MINYEAR, 1, 1)))
        tds = DialogSourceMock(dialogs)
        archiver.execute(tds, logging.getLogger(
            "Test"), filter_=lambda x: False)

        for dialog in dialogs:
            assert dialog.archived() == False

    def test_only_archive_old_chats(self):
        dialogs = [
            DialogMock(date.today(), name="new"),
            DialogMock(date(MINYEAR, 1, 1), name="old")
        ]

        tds = DialogSourceMock(dialogs)
        archiver.execute(tds, logging.getLogger("Test"))

        for dialog in dialogs:
            if dialog.archived():
                assert dialog.name == "old"

    def test_day_param_should_matter(self):
        today = date.today()

        _14days_before = today - timedelta(days=14)
        _15days_before = today - timedelta(days=15)
        _16days_before = today - timedelta(days=16)

        dialogs = [
            DialogMock(today, name="new"),
            DialogMock(_14days_before, name="old"),
            DialogMock(_15days_before, name="elder"),
            DialogMock(_16days_before, name="eldest")
        ]

        tds = DialogSourceMock(dialogs)
        archiver.execute(tds, logging.getLogger("Test"), time_limit_days=15)

        total_archived = 0
        for dialog in dialogs:
            if dialog.archived():
                assert dialog.name == "eldest" or dialog.name == "elder"
                total_archived += 1
        assert total_archived == 2
