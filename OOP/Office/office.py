from .manager import Manager
from .cleaner import Cleaner


class Office:
    def __init__(self, name):
        self.name = name
        self.documents = []
        self.managers = []
        self.cleaners = []

    def hireManager(self, name):
        newEmployee = Manager(name)
        self.managers.append(newEmployee)

    def hireCleaner(self, name):
        newEmployee = Cleaner(name)
        self.cleaners.append(newEmployee)
    
    def startWorkDay(self):
        for manager in self.managers:
            manager.work(self)
        for cleaner in self.cleaners:
            cleaner.work()
