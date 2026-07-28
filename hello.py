def hello_world():
    print("hello world")

hello_world()

def greeting(name):
    print("hi"+name+"!")
greeting("Arhan")

def add (num1,num2):
    print(num1+num2)
add(10,15)

def add(num1,num2):
    return num1+num2
num_sum =add(12,34)
print(num_sum)

def add(num1,num2):
    return num1+num2
def mul(num1,num2):
    return num1*num2
print(mul(add(1,2),add(3,4)))