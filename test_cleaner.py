from OOP_Office.cleaner import Cleaner


class TestCleaner:
    def test_init(self):
        amit = Cleaner("amit")
        assert type(amit.name) == str
        assert len(amit.name) == 4
        assert amit.work() != "amit is cleaning"
