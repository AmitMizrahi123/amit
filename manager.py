from .employee import Employee
from .person import Person


class Manager(Person):
    def __init__(self, name):
        super().__init__(name)
        self.employees = [] 

    def hireEmployee(self, name):
        self.employees.append(Employee(name))

    def ask_employee_to_work(self, office):
        for employee in self.employees:
            employee.work(office)
