import hug
from wesim import Weather


@hug.get()
def index():
    return {
        'INFO': "Welcome to weather-simulator beta! Why don't you try /weather"
    }


@hug.get()
def weather(city: hug.types.text=None):
    return {
        'cities': city,
        'weather': Weather.simulate()
    }



