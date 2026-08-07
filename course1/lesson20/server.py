from flask import Flask, render_template, request
from weather import get_weather
from waitress import serve

app = Flask(__name__)

@app.route("/")
@app.route("/index")

def index():
    return render_template("index.html")


@app.route("/weather", )
def weather():
    city = request.args.get("city")
    if not bool(city.strip()):
        city = "Enugu"
    data = get_weather(city)
    if not data.get("cod") == 200:
        return render_template("city-not-found.html")
    title = data["name"]
    status = data["weather"][0]["description"].capitalize()
    temp = f"{data["main"]["temp"]:.1f}"
    feels_like = f"{data["main"]["feels_like"]:.1f}"
    return render_template("weather.html", title=title, status=status, temp=temp, feels_like=feels_like)


if __name__ == "__main__":
    serve(app,host="0.0.0.0", port=5000)