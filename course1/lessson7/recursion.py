# recursion is a way to call a function from within itself
# it is useful for solving problems that can be broken down into smaller subproblems



def factorial(n):
    if n == 1:
        return 1
    else:
        print(n)
        return n * factorial(n - 1)

print(factorial(5))

# recursion can be used to solve problems that have a base case and a recursive case
# the base case is the simplest case that can be solved directly
# the recursive case is the case that can be broken down into smaller subproblems

def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
print(fibonacci(5))

def addOne(n) : 
    if n >= 9:
       return n + 1
    total = n + 1
    print(total)
    return addOne(total)

result = addOne(0)
print(result)