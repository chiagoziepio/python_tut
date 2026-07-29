# modules are reusable files of code that can be imported into other files
#  modules are used to organize code
#  modules are used to make code reusable
#  modules are used to make code easier to read
#  modules are used to make code easier to maintain
# example of a module are the math module, sys module, random module, the enum module
#  modules can be custom or built in or from a library

import random
from math import sqrt
print(random.randint(1, 3))
import Lagos
from rps7 import play_rock_paper_scissor

print(sqrt(4))
print(Lagos.song)
Lagos.randomFunFactAboutLagos()

# __name__ shows the name of the module. if the module is imported, it will show the name of the file else the value will be __main__
print(__name__)
print(Lagos.__name__)
play = play_rock_paper_scissor()
play()