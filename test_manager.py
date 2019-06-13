from OOP_Office.manager import Manager
from OOP_Office.office import Office
from OOP_Office.employee import Employee
from OOP_Office.person import Person
from OOP_Office.document import Document


class TestManager:
    def test_1(self):
        assert Person("amit").name is not str
        assert len(Person("amit").name) == 4

    def test_2(self):
        amit = Manager("amit")
        amit.hireEmployee("sima")
        assert Manager("amit").employees is not None
        for employee in Manager("amit").employees:
            assert employee is not str

    def test_3(self):
        office = Office("toysAreUs")
        amit = Employee("amit")
        zohar = Manager("zohar")
        zohar.hireEmployee("sima")
        zohar.hireEmployee("ram")
        zohar.hireEmployee("tom")
        for employee in zohar.employees:
            employee.work(office)
        assert amit.work(office) is not list
        assert Document("sima").employeeName is not str
