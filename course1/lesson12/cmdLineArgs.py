# the command line argument parser is a way of receiving argument from the commad line

def offerDrink(name, drink):
    print(f"\n Hola {name}, quires un {drink} con leche?")

if __name__ == "__main__":

    import argparse

    greeter = argparse.ArgumentParser(
        description= "This is for providing a personalized greeting"
    )

    greeter.add_argument(
        "-n", "--name" , metavar= "name", required= True, help= "Provide a name to get a personalized greeting"
    )
    greeter.add_argument(
        "-d", "--drink", metavar= "drink", required= True, help= "Provide a drink of choice", choices= ["te", "agua", "cafe"]
    )

    greeterArgs = greeter.parse_args()

    offerDrink(greeterArgs.name, greeterArgs.drink)