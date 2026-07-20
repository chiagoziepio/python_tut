def greeting (name : str , age : int) -> str :
    return f"Hello {name}, you are {age} years old"

def another_fn (name) :
    return {"name" : name}

result = greeting("Alice", 30)
print(result)

print(another_fn("Bob"))
print(greeting(21, "Charlie"))
