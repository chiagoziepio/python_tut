import random
capital = "Lagos"
bird = "chicken"
flower = "rose"
song = "personally"

def randomFunFactAboutLagos():
    options = ["the capital of nigeria", "the bird that is the most common in Nigeria", "the flower that grows in Nigeria", "the song that Nigerians sing"]
    randomIndex = random.randint(0, 3)
    print(options[randomIndex])

#  this excution will not run if the module is imported
if __name__ == "__main__":
    randomFunFactAboutLagos()