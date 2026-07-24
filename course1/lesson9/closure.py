# closure is when a nested function has access to variables from an outer function
# this is useful when you want to create a function that has some state
# the state is stored in the variables of the outer function
# the inner function can access the variables of the outer function
# the parent function either return the inner function without invoking it then assign a variable to the outer function when calling it and the variable now holds a reference to the inner function and you can now call the variable as a function
# or  you can invoke the inner function inside the outer function without returning it and then invoke the outer function 

def outerFunction():
    x = 1
    def innerFunction():
        nonlocal x 
        print(x)
        x += 1
    return innerFunction
    # innerFunction()
    # innerFunction()
    # innerFunction()
    # innerFunction()
    # innerFunction()
    # innerFunction()
    # 
fn =outerFunction()
# fn()
# fn()
# fn()
# fn()
# fn()
# fn()
# fn()
# fn()
# fn()

def outerFunction(name :  str, coins:  int):
    def innerFunction():
        nonlocal coins
        coins -= 1
        if coins >  10:
            return name + " you are cheating us. get out of here"
        elif coins >= 1 :
            return name + " you have " + str(coins) + " coins"
        else:
            return name + " you have no coins"
    return innerFunction

result = outerFunction("john", 12)
it = outerFunction("paul", 6)
print(result())
print(result())
print(it())
print(result())
print(result())
print(it())
print(it())
print(result())
print(result())
print(result())
print(it())
print(it())
print(it())
print(it())

