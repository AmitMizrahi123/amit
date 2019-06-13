from .document import Document
from .person import Person


class Employee(Person): 
    def work(self, office):
        for i in range(0, 10):
            office.documents.append(Document(self.name))
