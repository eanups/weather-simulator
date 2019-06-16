from weather.simulator.meta.parsers.img_parser import ImageParser
from weather.simulator.meta.parsers.json_parser import CityMetaJson
from weather.simulator.utils import weather_config as c


class Coordinates:

    @classmethod
    def get_mean_elevation(cls, city):

        grid_space = ImageParser().get_pixel_value_info(city)
        mean_elevation = grid_space.mean() * c.MAX_ELEVATION / c.MAX_PIXEL_VAL

        return mean_elevation

    @classmethod
    def get_latitude_longitude(cls, city):
        return CityMetaJson.get_city_lat_lon(city)
