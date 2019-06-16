from weather.logger import log
from weather.simulator.model.factors.coordinates import Coordinates

import random as rand
from weather.simulator.utils import weather_config as c


class WeatherGenerator:
    """
    Weather Conditions Generator class
    """

    def __init__(self, city):
        self.city = city
        self.elevation = Coordinates.get_mean_elevation(city)
        self.latitude, self.longitude = Coordinates.get_latitude_longitude(city)

    @staticmethod
    def generate_humidity():
        return rand.randrange(c.MIN_HUMIDITY, c.MAX_HUMIDITY)

    @staticmethod
    def generate_pressure():
        return rand.randrange(c.MIN_PRESSURE, c.MAX_PRESSURE)

    def generate_temperature(self):
        """
        # Rough estimation of temperature based on latitude and elevation.
        - Every 10 degree stride from the equator toward the poles is 5 C drop in temperature
        - Every 1000m altitude results in 6.5 C drop in temperature
        :return:  Estimated temperature randomly varied around 10 degree centigrade
        """

        temperature = c.HIGH_TEMPERATURE - (c.ELEVATION_DROP_FACTOR * self.elevation / c.ELEVATION_DISTANCE_FACTOR) - \
                      (c.ALTITUDE_DROP_FACTOR * abs(self.latitude) / c.ALTITUDE_DISTANCE_FACTOR)

        log.debug(f'{self.city} > Temp: {temperature}, Ele/Lat: {(self.elevation, self.latitude)}')

        # Randomize around 10 degrees of the estimated temperature.
        return rand.uniform(temperature - c.TEMP_VARIATION, temperature + c.TEMP_VARIATION)
