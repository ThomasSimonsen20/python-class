class Person:
    
    def __init__(self, name):
        self.name = name

    def isEmployee(self):
        return False
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            print("Please type a actual name")

class Employee(Person):

    def isEmployee(self):
        return True

class Boss(Employee, Person):
    pass

x = Person("Thomas")
print(x.name, x.isEmployee())

x = Employee("Thomas1")
print(x.name, x.isEmployee())

x = Boss("Thomas2")
print(x.name, x.isEmployee())