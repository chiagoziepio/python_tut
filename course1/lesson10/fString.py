#  there various ways to handle strings in python
#  1 is the concatenation operator
#  2 percent s operator (%s)
#  3 is the format method
#  4 id th fstring method, which is the new and best way to handle strings

#  concatenation operator
name = "Harry"
age = 30
message = name + " is " + str(age) + " years old"
print(message)

#  percent s operator
message = " name is %s and age is %s" % (name, age)
print(message)

#  format method
message = "the name is {} and the age is {}".format(name, age)
print(message)
# format method also has the indexing method , which tells where a variable is in the string
message= "his name is {1} and his age is {0}".format((age + 1), name)
print(message)

#  fstring method

message = f"the boy's name is {name} and his age is {age}"
print(message)

# formating f strings
num = 10
#  the .2f tells the string to round to 2 decimal places
message =  f"{name} is this {4.5 * num:.2f}"
print(message)

# f string in a loop
for x in range(10):
    message = f"{x} divied by 4.3 is {x / 4.3:.3f}"
    print(message)
    # formating a percent
    message = f"{x} divied by 4.3 is {x / 4.3:.3%}"
    print(message)