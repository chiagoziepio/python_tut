import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()

def get_weather(city):
    API_KEY = os.getenv("API_KEY")
    print("\n*** Get Weather Information ***")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()
    return data


if __name__ == "__main__":

    def loadWeather():
        city = input("\nPlease enter the city name:\n")
        weather : dict = get_weather(city)
        # pprint(weather)
        print(f"\nThe weather in {weather.get("name")} is {weather.get("main").get("temp")} degrees Celsius. \nBest desciption of the weather is: {weather.get("weather")[0].get("description")}.\nBut it might feel like {weather.get("main").get("feels_like")} degrees Celsius.\n")


loadWeather()