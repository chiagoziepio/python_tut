class Vehicle :
    def __init__(self, make: str, year :int):
       self.make = make
       self.year = year
       
    def move(self):
        print("moving")
    def getYearMake(self):
        print(f"i am a {self.year} {self.make}")

paddyCar = Vehicle(make= "toyota", year=2021)
paddyCar.move()
paddyCar.getYearMake()