#functions are reusable you can invoke as many times as you want to be able to reuse your code in another place

#def intro():
    #code block
    #return an output
#must ident
def hello():
    print("Hello class")

hello()

#function arguments
def hello(name):
    print(f"Hello {name}")

hello("Victorine")

def hello(name, age):
    year=2021-age
    print(f"Hello {name}, you were born in {year}")

hello("Favour",20)

#The return keyword

def add(a,b):
    answer=a+b
    return answer

x=add(10,20)
print(x)

def condition(marks):
    if marks<=50:
        print("fail")
    elif marks ==70:
        print("almost there")
    elif marks==100:
        print("Perfect")

condition(100)

#string formatting
#using the % modulus sign
def call(name):
    print("Hello %a" % name)

call('Victorine')


def factorial(num):
    z=1
    while num>0:
        z*=num
        num-=1
    print(z)
factorial(8)
    