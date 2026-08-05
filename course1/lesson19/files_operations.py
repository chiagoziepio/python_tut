import os

# these are ways of handling files

# r = read
# a =  append to the file
# w = write. overwrite the file
# x = create a new file

filesPrefix = "course1/lesson19/"
# you can also omit passing the  "r" because it is the default
nameFile = open(f"{filesPrefix}name.txt", "r")
print(nameFile.read())
nameFile.close()


# append

nameFile = open(f"{filesPrefix}name.txt", "a")
nameFile.write("\nDavid")
nameFile.close()

nameFile = open(f"{filesPrefix}name.txt", "r")
print(nameFile.read())
nameFile.close()

# write
animalsFile = open(f"{filesPrefix}animals.txt", "w")
animalsFile.write("dog\ncat\nbear\n")
animalsFile.close()

animalsFile = open(f"{filesPrefix}animals.txt", "r")
print(animalsFile.read())
animalsFile.close()

# create a new file


if not os.path.exists(f"{filesPrefix}dogs.txt"):
    dogsFile = open(f"{filesPrefix}dogs.txt", "x")
    dogsFile.close()



# reading a file that might not exist

try:
    dogsFile = open(f"{filesPrefix}dogds.txt", "r")
    print(dogsFile.read())
except FileNotFoundError as e :
    print(f"The file does not exist {e}")
else:
    dogsFile.close()


# deleting a file

if os.path.exists(f"{filesPrefix}dogs.txt"):
    os.remove(f"{filesPrefix}dogs.txt")
    print("The file has been deleted")
else:
    print("The file does not exist")


# using the with statement

with open(f"{filesPrefix}name.txt", "r") as f:
    content = f.read()

with open(f"{filesPrefix}animals.txt", "w") as f:
    f.write(content)