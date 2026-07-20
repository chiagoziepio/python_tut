from functions import greeting

# value = 1

# while value < 20 : 
#     print(value)
#     value += 1
# else :
#     print("completed")   


names = ["ann", "john" , "paul"]    

for name in names :
    print(name)


JOHN = "john"
JOHN = "rtyu"

print(JOHN)

value = 1
count = 0
while value:
    count += 1
    print(count)
    if count == 5 :
        break
    else :
        value = 0
        continue
print("out of loop")
print(greeting("Alice" , 30))