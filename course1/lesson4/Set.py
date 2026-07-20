# set is a collection of unique items
fruits = {"apple", "orange", "banana", "mango"}
print(fruits)
print(type(fruits))

# in set, 1 and True are considered the same, 0 and False are considered the same

mixedSet = {True,4,  "apple", False}
print(mixedSet)

# checking if an item is in the set
appleInSet = "apple" in fruits
print(appleInSet)

# adding an item to the set
fruits.add("pear")
# adding a set to another set
colors = {"red", "green", "blue"}
mixedSet.update(colors)
print(mixedSet)
# merging two sets

# creating a set from a list
names = {"john", "adam", "jane"}
trees = {"oak", "maple", "birch"}
newSet = names.union(trees)
print(newSet)

# merging two sets but just keeping the duplicates
one = {1,2,3,4,5}
two= {1,2,3,4,5,6, 7}
one.intersection_update(two)
print(one)
# merging two sets but just keeping except duplicates
one = {1,2,3,4,5}
two= {1,2,3,4,5,6, 7}
one.symmetric_difference_update(two)
print(one)