class Car:

    def __init__(self, make, model, bhp, mph):
        self.make = make
        self.model = model
        self.bhp = bhp
        self.mph = mph

    @property
    def make(self):
        return self.make
    
    @property
    def model(self):
        return self.model
    
    @property
    def bhp(self):
        return self.bhp
    
    @property
    def mph(self):
        return self.mph
    
    @make.setter
    def make(self, m):
        self.make = m
    
    @model.setter
    def model(self, m):
        self.model = m
    
    @bhp.setter
    def bhp(self, b):
        self.bhp = b
    
    @mph.setter
    def mph(self, m):
        self.mph = m