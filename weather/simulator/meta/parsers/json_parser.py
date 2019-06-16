from weather.simulator.readers.json_reader import JsonReader
from weather.logger import log


class CityMetaJson:
    """
    Place holder class to get the meta-data from JSON
    """

    cities = JsonReader("city_info.json").get_json()

    @classmethod
    def get_city_lat_lon(cls, city):
        _city = city.strip().title()
        if _city not in cls.cities:
            log.error(f'Unable to find city: [{city}] or co-ordinates are not configured for it.')
            raise NotImplementedError
        lat = cls.cities.get(_city).get('position').get('latitude')
        lon = cls.cities.get(_city).get('position').get('longitude')

        return lat, lon

    @classmethod
    def get_cities(cls):
        return [city for city in cls.cities.keys()]


