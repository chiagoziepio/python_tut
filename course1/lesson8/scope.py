#  scope is the region of a program where a variable is valid
# there are two types of scope
# local scope :  variables defined inside a function are only valid inside that function
# global scope :  variables defined outside of a function are valid everywhere
# global variables are accessed using the global keyword
# local variables are accessed using the nonlocal keyword
# if/else, while loops do not create a new scope , they are part of the same scope as the code outside of them. this means that variables defined inside them are also part of the scope that houses the if/else or while loop

# global variables
name = "john" 

def printName():
    # local variables
    age = 30
    print(name)
   
    def printAge():
        # since age is a local variable, to modify it,we need to use the nonlocal keyword. this tells python that we want to access the local variable inside the function . without this keyword, python will create a new local variable that has no relation to the glocal "age" variable
        nonlocal age
        age += 10
        print(age)
    printAge()
# age cant be accessed here because it is defined inside the function
printName()

# to modify a global variable, you need to use the global keyword

def changeName():
    # note: we are doing this because we want use and modify the global "name" variable.  Doing name = "paul" will create a new local variable that has no relatio to the global "name" variable
    global name
    name = "paul" + name
    print(name)

changeName()