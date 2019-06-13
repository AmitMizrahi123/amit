from OOP_Office.employee import Employee
from OOP_Office.office import Office
import pytest
import random


class TestEmployee:
    def test_init(self):
        amit = Employee("amit")
        assert type(amit.name) == str
        assert len(amit.name) == 4

    def test_init_2(self):
        amit = Employee("amit")
        office = Office("toysAreUs")
        docs = amit.work(office)
        assert type(office.documents) == list
        assert len(office.documents) == 10
        for doc in office.documents:
            assert type(doc.employeeName) == str
        with pytest.raises(Exception):
            amit.work(5)
            amit.work([1, 2, 3])
            amit.work({})
            amit.work((1, 2, 3))
