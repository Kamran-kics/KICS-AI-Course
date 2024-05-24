# function definition
def hello():
    print('hello world')


def sum(a, b): # parameters
    c = a + b
    return c # returned value

# function calling
x = sum(10, 15) # arguments
print(x)

def sum(a = 10, b = 15): # parameters
    x = a + b
    return x # returned value

answer = sum(b = 12, a = 45)
print(answer)

from subtraction import sub
print(sub(23, 45))