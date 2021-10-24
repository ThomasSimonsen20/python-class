
class Bank():
    def __init__(self):
        self.__accounts = []
    
    @property
    def accounts(self):
        return self.__accounts
    
    @accounts.setter
    def accounts(self, acc):
        if type(acc) is int:
            self.__accounts.append(acc)
        elif type(acc) in [tuple, list]:
            for i in acc:
                self.__accounts.append(i)
        

class Account:
    
    def __init__(self, no, cust):
        self.accountNumber = no
        self.cust = cust
    

    def __repr__(self):
        return f'{self.no} : {self.cust}'
class Customer:
    
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return f'{self.name}'