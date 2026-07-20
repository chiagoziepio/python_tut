names = ["paddy", "john", "jane", "tom"]
hasPaddy = "paddy" in names
print(hasPaddy)

indexOfJane = names.index("jane")
print(indexOfJane)
# length of list
print(len(names))

# add item to list
names.append("bill")
print(names)
# adding a list to a list
names += ["agu" , "joy"]
print(names)
names.extend(["paul", "Adam"])
print(names)
#  checking type
print(type(names))

# adding item to a particular index
names.insert(3,"andrew")
print(names)
names[4:4] =["azu", "ndu"]
print(names)

# replacing item in list
names[2] = "adam"
print(names)
names[3:4] = ["ewu" , "ene"]
print(names)
# removing item from list 
names.remove("joy")
print(names)
# removing the last item in the list
names.pop()
print(names)
# deleting an item from a list
del names[2]
print(names)
# deleting the whole list
# del names
# clearing the list
# names.clear()
# print(names)

# sorting the list
# sorts in ascending order
names.sort()
print(names)
names[2] = "Steve"
print(names)
names.sort()
print(names)
# making the sort account for case
names.sort(key=str.lower)
print(names)

# sort in descending order
names.sort(reverse=True)
print(names)
# sorting without affecting the original list
sortedNames = sorted(names)
print(sortedNames)
sortedNames = sorted(names, key=str.lower)
print(sortedNames)
# making copy of list
copyNames = names.copy()
secondCopy = list(names)
thirdCopy =  names[:]
print(copyNames)
print(secondCopy)    
print(thirdCopy)
thirdCopy.clear()
print(thirdCopy)
print(names)