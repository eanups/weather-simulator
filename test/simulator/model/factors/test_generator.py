
import unittest

from weather.simulator.model.factors.generator import WeatherGenerator
from weather.simulator.utils.weather_config import *


class TestWeatherGenerator(unittest.TestCase):

    def setUp(self):
        self.sydney = WeatherGenerator('Sydney')
        self.london = WeatherGenerator('london')

    def test_generate_humidity(self):
        h = self.sydney.generate_humidity()
        self.assertTrue(MIN_HUMIDITY < h < MAX_HUMIDITY)

    def test_generate_temperature(self):
        t = self.sydney.generate_temperature()
        self.assertTrue(MIN_TEMPERATURE < t < MAX_TEMPERATURE)

    def test_generate_pressure(self):
        p = self.sydney.generate_pressure()
        self.assertTrue(MIN_PRESSURE < p < MAX_PRESSURE)

    def test_generate_humidity_2(self):
        h = self.london.generate_humidity()
        self.assertTrue(MIN_HUMIDITY < h < MAX_HUMIDITY)

    def test_generate_temperature_2(self):
        t = self.london.generate_temperature()
        self.assertTrue(MIN_TEMPERATURE < t < MAX_TEMPERATURE)

    def test_generate_pressure_2(self):
        p = self.london.generate_pressure()
        self.assertTrue(MIN_PRESSURE < p < MAX_PRESSURE)

