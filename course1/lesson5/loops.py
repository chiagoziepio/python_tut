#  we have two types of loops
# the while loop :  while a condition is true, do something, else stop

value = 1
# while value < 10: 
#     print(value)

#     value += 1
# else : 
#     print("done")

# using break to exit the loop before the condition is met
# while value < 10: 
#     print(value)
#     if value == 5:
#         break
#     value += 1
# else : 
#     print("done")


# using the contiune keyword

# while value <  10 :
#     value += 1
#     if value == 6:
#         continue 
#         # this stop the current iteration from going forward and start the next one
#     print(value)
# else : 
#     print("done")


# for loop :  it iterates over a sequence of items
names = ["john", "paul", "george", "ringo"]
# for name in names:
#     print(name)

# using break to exit the loop before the condition is met

# for name in names:
#     print(name)
#     if name == "paul":
#         break
# else : 
#     print("done")

# using the contiune keyword
# for name in names:
   
#     if name == "paul":
#         continue 
#         # this stop the current iteration from going forward and start the next one
#     print(name)
# else : 
#     print("done")

# using the range function to create a sequence of numbers
# for i in range(10):
#     print(i)

# # telling the range function where to start and stop
# for i in range(1, 10):
#     print(i)

# telling the range function how to increment
# for i in range(1, 10, 2):
#     print(i)

# making nested loops
for name in names:
    for i in range(1, 10):
        print(name, i)