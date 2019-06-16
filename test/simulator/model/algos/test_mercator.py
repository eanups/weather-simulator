import unittest

from weather.simulator.model.algos.mercator import Mercator


class TimeMercator(unittest.TestCase):

    def setUp(self):
        pass

    def test_algorithm(self):
        mid_pixel = Mercator.get_xy_of_map_from_lat_lon(0, 0, 10800, 21600)
        self.assertEqual((5400, 10800), mid_pixel, "Error in algorithm")

    def test_algorithm_negative(self):
        mid_pixel = Mercator.get_xy_of_map_from_lat_lon(13, 32, 10800, 21600)
        self.assertNotEqual((5400, 10800), mid_pixel, "Error in algorithm")
