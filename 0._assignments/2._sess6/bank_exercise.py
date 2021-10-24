
class Bank():
    def __init__(self):
        self.accounts = []

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