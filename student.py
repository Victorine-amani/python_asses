#object oriented program

class Student:
    school="AkiraChix"   #class attributes- the value is shared across all objects created with the class
    
    #constructor function
    #when adding a function to a class the first argument is always 'self'
    def __init__(self,name,age):  #instance attributes- each object has it's own value for the instances
        self.name=name
        self.age=age
    def speak(self):
        return f'Hello my name is {self.name}, I am {self.age} years old and I love {self.school}'
    

#class methods add behavior to an object  
#to access the attributes you must use the 'self' keyword to personalize the attribute for that specific object


