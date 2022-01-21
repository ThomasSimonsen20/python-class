class Person():
    def __init__(self, name):
        self.name = name

    def isEmployee(self):
        return False
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if type(name) != str:
            print("Cannot set name to non string value")
        else:
            self._name = name
    
class Employee(Person):

    def isEmployee(self):
        return True


class Yes(Employee, Person):
    pass

x = Person("Thomas")
print(x.name, x.isEmployee())

x = Employee("Thomas1")
print(x.name, x.isEmployee())

x = Yes("Thomas3")
print(x.name, x.isEmployee())