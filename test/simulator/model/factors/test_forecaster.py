
import unittest

from weather.simulator.model.factors.forecaster import WeatherForecaster, Forecast


class TestWeatherForecaster(unittest.TestCase):

    def setUp(self):
        self.sydney = WeatherForecaster('Sydney')
        self.bangalore = WeatherForecaster('Bangalore')
        self.thimphu = WeatherForecaster('Thimphu')

    def test_conditions_sydney(self):
        c = self.sydney.get_conditions()
        self.assertTrue(c in [Forecast.RAINY.value, Forecast.SUNNY.value])
        self.assertFalse(c in [Forecast.SNOWY.value])

    def test_conditions_thimphu(self):
        c = self.thimphu.get_conditions()
        self.assertTrue(c in [Forecast.RAINY.value, Forecast.SUNNY.value, Forecast.SNOWY.value])

    def test_conditions_bangalore(self):
        c = self.bangalore.get_conditions()
        self.assertTrue(c in [Forecast.RAINY.value, Forecast.SUNNY.value])
        self.assertFalse(c in [Forecast.SNOWY.value])

