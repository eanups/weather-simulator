from weather.simulator.meta.parsers.json_parser import CityMetaJson
from weather.simulator.model.algos.mercator import Mercator
from weather.simulator.readers.img_reader import ImageReader

from weather.simulator.utils import weather_config as c
from weather.logger import log


class ImageParser:

    def __init__(self):
        self.pixels = ImageReader.get_pixels()
        self.img_height, self.img_width = self.pixels.shape

    def get_xy_from_city(self, city):
        lat, lon = CityMetaJson().get_city_lat_lon(city)
        return Mercator.get_xy_of_map_from_lat_lon(lat, lon, self.img_width, self.img_height)

    def get_pixel_value_info(self, city):
        x, y = self.get_xy_from_city(city)

        log.debug(f'Location [x, y] = [{x}, {y}]')
        log.debug(f'Normalized values: {x / self.img_width} , {y / self.img_height}')

        # Get vectorized grid [rows, columns] location for x,y
        return self.pixels[y - c.DELTA:y + c.DELTA, x - c.DELTA:x + c.DELTA]






