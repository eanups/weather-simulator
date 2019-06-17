from weather.simulator.meta.parsers.json_parser import CityMetaJson
from weather.simulator.model.factors.forecaster import WeatherForecaster


class Weather:
    @classmethod
    def simulate(cls, city=None):
        weather = ""
        try:
            if city:
                weather = WeatherForecaster(city=city).forecast()
            else:
                cities = CityMetaJson.get_cities()
                for c_city in cities:
                        weather += WeatherForecaster(city=c_city).forecast() + "\n"

        except NotImplementedError as nie:
            print(nie)

        return weather


if __name__ == '__main__':
    print(Weather.simulate())
