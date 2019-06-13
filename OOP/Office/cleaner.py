from .person import Person


class Cleaner(Person):
    def work(self):
        print(self.name + " is cleaning")