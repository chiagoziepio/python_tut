# creating dectionaries
# using curly braces
plants = {
    "cassava" : "tuber",
    "yam" : "tuber",
    "mango" : "tree"
}

# using constructor method

herbs = dict(ugu = "vegetables" , agbo = "highness")

# accessing items in a dictionary
oneItem = plants["cassava"]
print(oneItem)
anotherItem = herbs.get("ugu")
print(anotherItem)
print(isinstance(herbs, dict))

print(len(herbs.keys()))
print(len(herbs.values()))


# verifying existence of keys

isthere = "ugu" in herbs
print(isthere)
anotherIsthere = "medicine" in plants
print(anotherIsthere)

# changing values
plants["mango"] = "fruit"
print(plants)
herbs.update({"water leaf": "stew"})
print(herbs)