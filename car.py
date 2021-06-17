class Car:
    def __init__(self,model,registration,color,mileage):
        self.model=model
        self.registration=registration
        self.color=color
        self.mileage=mileage

    def speed(self,fast):
        self.fast=fast
        return f'The speed of {self.model} is {self.fast} km/hr' 

    def buy(self):
        return f'I just bought a {self.color} {self.model} and it is beautiful'