class Dog:
    def __init__(self,name,breed,color):
        self.name=name
        self.breed=breed
        self.color=color

    def bark(self):
        return f'{self.name} is a really loud dog'
    
    def birth(self):
        return f"{self.name} is a mix of a sheepdog and poodle thats why she's a {self.breed}"