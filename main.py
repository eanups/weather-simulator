import hug
from weather_generate import Weather


@hug.get()
def index():
    return {
        'INFO': "Welcome to weather-simulator beta! Why don't you try /weather"
    }


@hug.get()
def weather(city: hug.types.text=None):
    return {
        'city': city,
        'weather': Weather.simulate(city)
    }



