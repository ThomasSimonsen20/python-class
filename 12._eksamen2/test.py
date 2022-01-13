#class er ligesom vi kender i Java, når vi laver metoder i en klasse skal man skrive self med som parameter.
#Skal som min. havde pass inde i en klasse, en klasse må ikke være tom.
#The self parameter is a reference to the current instance of the class, 
# and is used to access variables that belongs to the class.



class Person(object):
       
    # Constructor
    def __init__(self, name):
        self.name = name
   
    # To get name
    #def getName(self):
    #    return self.__name #private virable når man bruger normal getter og setter
   
    # To check if this person is an employee
    def isEmployee(self):
        return False

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if type(name) != str:
            print('Nop no no')
        else:
            self._name = name
   
# Inherited or Subclass (Note Person in bracket)
class Employee(Person):
   
    # Here we return true
    def isEmployee(self):
        return True

class Yes(Employee, Person):
    pass
   
# Driver code
emp = Person("Geek1")  # An Object of Person
print(emp.name, emp.isEmployee())
   
emp = Employee("Geek2") # An Object of Employee
print(emp.name, emp.isEmployee())

emp = Yes("Geek3") # An Object of Yes
print(emp.name, emp.isEmployee())