import requests
import json
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def home_page():
    if request.method == "POST":
        user_city = request.form.get("city")

        API = "c35439e57be5419f941122650242709"
        # include air quality index
        aqi = "yes"
        url = f"http://api.weatherapi.com/v1/current.json?key={API}&q={user_city}&aqi={aqi}"
        result = requests.get(url)
        wdata = json.loads(result.text)
        print(wdata)

        country = wdata['location']['country']

        temperature1 = wdata["current"]["temp_c"]

        icon1 = wdata["current"]["condition"]["icon"]

        text1 = wdata["current"]["condition"]["text"]

        wind1 = wdata["current"]["wind_mph"]
        print(wind1)

        return render_template("parent.html", city_name=user_city, country=country, temperature=temperature1, icon=icon1, text=text1, wind=wind1)
    return render_template("main.html")


if __name__ == "__main__":
    app.run()

