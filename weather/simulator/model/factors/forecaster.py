from enum import Enum, auto

from weather.simulator.meta.parsers.img_parser import ImageParser
from weather.simulator.model.factors.coordinates import Coordinates
from weather.simulator.model.factors.generator import WeatherGenerator
from weather.simulator.model.img_viewer import ImageViewer
from weather.simulator.utils.timezone import TimeZone
from weather.simulator.utils import weather_config as c


class AutoName(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name


class Forecast(AutoName):
    SNOWY = auto()
    RAINY = auto()
    SUNNY = auto()


class WeatherForecaster:

    def __init__(self, city):
        self.city = city
        self.temperature = WeatherGenerator(city).generate_temperature()
        self.humidity = WeatherGenerator.generate_humidity()
        self.pressure = WeatherGenerator.generate_pressure()
        self.elevation = Coordinates.get_mean_elevation(city)
        self.latitude, self.longitude = Coordinates.get_latitude_longitude(city)
        self.time = TimeZone.current_local_time(city)

    def get_conditions(self):
        """
        Return probable conditions. viz either one of [SUNNY, RAINY, SNOWY] based on a trivial decision tree.
        :return:
        """
        probable = Forecast.SUNNY
        if self.temperature < c.ZERO_TEMPERATURE:
            if self.humidity > c.SNOW_HUMIDITY:
                probable = Forecast.SNOWY
        else:
            if self.humidity > c.HIGH_HUMIDITY:
                probable = Forecast.RAINY
            elif self.humidity > c.REF_HUMIDITY and self.pressure < c.REF_PRESSURE:
                probable = Forecast.RAINY

        return probable.value

    def view_location(self):
        """
        Return detailed forecast result
        :return:
        """
        x, y = ImageParser().get_xy_from_city(self.city)
        ImageViewer.display(self.city, x, y)

    def forecast(self):
        """
        Return detailed forecast result
        :return:
        """
        return f'{self.city}|{self.latitude}, {self.longitude}, {self.elevation}|{self.time}|{self.get_conditions()}' \
               f'|{self.temperature}|{self.pressure}|{self.humidity}'


if __name__ == '__main__':
    WeatherForecaster('Sydney').view_location()






