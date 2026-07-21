# functions are a way to group a set of instructions together
# they are reusable blocks of code

def helloWorld():
    print("hello world")

helloWorld()

def sum(a, b):
    return a + b

result = sum(1, 2)
print(result)

# with optional parameters
def withOptionalParams1(a, b=0):
    return a + b

result = withOptionalParams1(1, 2)
print(result)

result = withOptionalParams1(1)
print(result)

def withOptionalParams2(a, b=0, c=0):
    if type(a) is not int or type(b) is not int or type(c) is not int:
        raise TypeError("a, b, and c must be integers")
    return a + b + c

result = withOptionalParams2(1, 2, 3)
print(result)

result = withOptionalParams2(1, 2)
print(result)


# working with unknown number of parameters, there are two ways to do this
#the first is the unnamed parameter
def sumOfArgs(*args):
    print(type(args))
    print(args)
    total = 0 
    for x in args:
        total += x
    return total

print(sumOfArgs(1, 2, 3, 4, 5))

#the second is the named parameter
def sumOfArgs2(**kwargs):
    print(type(kwargs))
    print(kwargs)
    total = 0
    for val in kwargs.values():
        total += val
    return total

print(sumOfArgs2(a=1, b=2, c=3, d=4, e=5))