
import requests
from dotenv import load_dotenv
import os
from pprint import pprint


load_dotenv()

def get_weather(city = "Enugu"):
    Api_key = os.getenv("API_KEY")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={Api_key}&units=imperial"
    res = requests.get(url)
    data = res.json()
    return data


if __name__ == "__main__":
    def weather():
        city = input("\nEnter a city name:\n")
        if not bool(city.strip()):
            city = "Enugu"
        data = get_weather(city)
        pprint(data)

    weather()

