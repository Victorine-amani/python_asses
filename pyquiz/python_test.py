  
x = [100,110,120,130,140,150]
y=[]
for item in x:
    b=item*5
    y.append(b)
print(y)
 
def divisible_by_three(n):
    for item in range(1,n):
        if item%3==0:
            print(item)

divisible_by_three(40)

def flatten():
    x = [[1,2],[3,4],[5,6]]
    flat_list = []
    for element in x:
        for item in element:
                flat_list.append(item)
    print(flat_list) 
flatten()
    
    

def smallest(numbers):
    print( min(numbers))
   
smallest([4,6,4,8,2,8,9,78,9])

def remove_duplicate(x):
    b=set(x)
    c=list(b)
    print(c)
remove_duplicate(['a','b','a','e','d','b','c','e','f','g','h'])


def divisible_by_seven():
    x=[]
    for item in range(100,200):
        if item%7==0:
            x.append(item)
            print(x)

divisible_by_seven()


def greet():
    students = [{"age": 19, "name": "Eunice"}, 
     {"age": 21, "name": "Agnes"}, 
     {"age": 18, "name": "Teresa"}, 
     {"age": 22, "name": "Asha"}]
    for item in students:
        print(f'Hello {item.get("name")} you were born in the year {2021-item.get("age")}')
        
greet()

class Rectangle:
    def __init__(self,width,length):
        self.width=width
        self.length=length

    def area(self):
        A=self.width*self.length
        print(A)

    def perimeter(self):
        P=2*self.length+2*self.width
        print(P)


rectangle=Rectangle(22,12)
rectangle.area()
rectangle.perimeter()

