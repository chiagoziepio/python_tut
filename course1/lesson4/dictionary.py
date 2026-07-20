plants = {
    "rose": "red",
    "tulip": "yellow",
    "daisy": "white"
}

print(plants)
print(type(plants))

# accessing items in dictionary
valueOfRose = plants["rose"]
print(valueOfRose)
valueOfTulip = plants.get("tulip")
print(valueOfTulip)

# listng keys
keys = plants.keys()
print(keys)
# length of dictionary
print(len(plants))
# length of keys
print(len(keys))

# listng values
values = plants.values()
print(values)

# verifying if an item is in the dictionary
roseInPlants = "rose" in plants
print(roseInPlants)
chocolateInPlants = "chocolate" in plants
print(chocolateInPlants)

# chaning the value of an item in the dictionary
plants["rose"] = "pink"
print(plants)

# updating the value of an item in the dictionary
plants.update({"daisy": "pink"})
print(plants)
plants.update({"cashew" : "green"})
print(plants)

# removing an item from the dictionary
print(plants.pop("rose"))
print(plants)
del plants["daisy"]
print(plants)
# removing the last item from the dictionary
print(plants.popitem())
print(plants)

trees = {
    "oak": "red",
    "maple": "yellow",
    "birch": "brown"
}

trees.update({"pine": "green"})
# iterating over the keys and values
for key, value in trees.items():
    print(key, value)


# clearing the dictionary
trees.clear()
print(trees)
# deleting the dictionary
# del trees

# making a copy of the dictionary
# bad way of doing it
newPlants = plants
newPlants["rose"] = "purple"
print(newPlants)
print(plants)
# the above is bad because they are pointing to the same object in memory

copyPlants = plants.copy()
copyPlants["amber"] = "purple"
print(newPlants)
print(plants)
print(copyPlants)