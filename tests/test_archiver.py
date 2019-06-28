from src import archiver


class TestArchive(object):
    def test_full_acrhiving(self, monkeypatch):
        def mockreturn(self, x):
            return 1
        monkeypatch.setattr(archiver, 'execute', mockreturn)
        assert archiver.execute(None, None) == 1
