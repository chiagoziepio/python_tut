#  exceptions are errors that occur during the execution of a program
#  they are raised when an error condition is met
#  they are handled using try and except blocks
#  the try block is used to define the code that might raise an exception
#  the except block is used to define the code that handles the exception
#  the finally block is used to define the code that is always executed, regardless of whether an exception is raised or not


def divide(a, b) :
    try:
        print(x)
    except :
        print("error") 


# divide(10, 0)  


# python returns the error type that happened

def error2():
    try:
        x = 10 / 0
    except ZeroDivisionError:
        print("error occurred because of division by zero")

# error2()

# we can also catch multiple exceptions

def multiError():
    try:
        x = 10 / 0
    except ZeroDivisionError:
        print("error occurred because of division by zero")
    except ValueError:
        print("error occurred because of invalid value")

# multiError()

# we can also raise our own exceptions using the built exception

def raiseError():
    try:
        raise ValueError("this is a custom error message")
    except ValueError as e:
        print(e)


# raiseError()

# if you want something to happen when there is no exception, you can use the else block

def elseBlock():
        try:
            x = 1+1
        except:
            print("error occurred")
        else:
            print("no error occurred")

# elseBlock()

# if you want something to happen regardless of whether an exception is raised or not, you can use the finally block

def finallyBlock():
    try:
     x = 1+1
    except:
        print("error occurred")
    else:
        print("no error occurred")
    finally:
        print("this code is always executed")

# finallyBlock()

# rasing custom exceptions

# generic method

def customGenericException():
    try :
    
        raise Exception("I dont like this")

    except Exception as e:
        print(e)

# customGenericException()


class IdontLikeYourFace(Exception):
    pass

def customOwnedException():
    try :
        raise IdontLikeYourFace("I dont like what you look like")
    except IdontLikeYourFace as e:
        print(e)

customOwnedException()       