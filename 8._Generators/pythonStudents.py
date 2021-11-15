 class PythonStudents:
    
    def studentGenerator():
        pass




class Student:

    def __init__(self, name, cpr):
        self.name = name
        self.cpr = cpr

    @property
    def name(self):
             return self.__name

    @name.setter
    def name(self, name):
             self.__name = name.capitalize()

    def __add__(self, student):
             return Student('Anna the daugther', 1234)

    def __str__(self):
             return f'{self.name}, {self.cpr}'

    def __repr__(self):
             return f'{self.__dict__}'