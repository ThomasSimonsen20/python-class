class Node:
    def __init__(self, data):
            self.data = data
            self.next = None
    
class LinkedList:
    def __init__(self):
            self.head = None
    
    def __len__(self):
        return len(self.head)
    
    def __getitem__(self, key):
        return self.head[key]
    
    def __setitem__(self, key, value):
        self.head[key] = value
    
    def __repr__(self):
        return f'{self.__dict__}'
    
    def __str__(self):
        return self.head
    
    def __add__(self):
        return self.head + self.head.next
    


