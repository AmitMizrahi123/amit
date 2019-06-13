from OOP_Office.document import Document
import pytest


class TestDocument:
    def test_init(self):
        amit = Document("amit")
        assert amit.employeeName == "amit"
        assert type(amit.employeeName) is str
        assert len(amit.employeeName) == 4
        with pytest.raises(Exception):
            Document("")
            Document(1)
            Document(())
            Document([])
            Document({})
