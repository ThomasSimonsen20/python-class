class Person:
    def __init__(self, name):
        self.name = name #Public variable -> property
        self.__age = 23
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        if type(name) != str:
            print('Nop no no')
        else:
            self.name = name

    #den måde vi laver getter og setter i python, da vi ikke skal skrive metode navne?
    #eneste grund til at lave dem her, er hvis man skal lave checks. f.eks. det der if statement.


