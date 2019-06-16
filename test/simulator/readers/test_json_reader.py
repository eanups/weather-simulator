import unittest

from weather.simulator.readers.json_reader import JsonReader


class TestJsonReader(unittest.TestCase):

    def setUp(self):
        self.reader = JsonReader("city_info.json")

    def test_get_city_metadata(self):
        cities = self.reader.get_json()

        assert(cities['Sydney'] is not None)
        syd_lat = float(cities['Sydney']['position']['latitude'])
        self.assertAlmostEqual(syd_lat, -33.869)

    def test_get_city_metadata_unknown_city(self):
        cities = self.reader.get_json()

        assert(cities.get('White') is None)

    def test_get_city_metadata_unknown_attribute(self):
        cities = self.reader.get_json()

        assert(cities.get('Sydney') is not None)
        syd_population = cities['Sydney'].get('position').get('population')
        self.assertIsNone(syd_population)

    def tearDown(self):
        self.reader = None
