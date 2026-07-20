def parent_function(name : str ):
    coin = 3
    def inner_function():
        nonlocal coin
        coin -= 1
        if  coin  >  1 :
           return f"Hello {name}, you have {coin} coins left"
        elif coin == 1 :
            return f"Hello {name}, you have {coin} coin left"
        else:  return f"Hello {name}, you have no coins left"
    return inner_function

tommy = parent_function("Tommy")
sonnia = parent_function("Sonnia")
print(tommy())
print(tommy())
print(tommy())
print(sonnia())
print(sonnia())

