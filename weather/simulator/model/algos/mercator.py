import numpy as np


class Mercator:

    """
    Responsible for converting latitude and longitude co-ordinates to (x,y) point on a mercator projection map,
    based on the map size.
    """

    @classmethod
    def get_xy_of_map_from_lat_lon(cls, latitude, longitude, img_width, img_height):
        """
        Return (x,y) point of the map from latitude and longitude.
        :param latitude: Map latitude position
        :param longitude: Map longitude position
        :param img_width: Image / Map width
        :param img_height: Image / Map height
        :return: (x,y) pixel
        """
        x = (longitude + 180) * (img_width / 360)

        #  Degrees to radians
        lat_rad = latitude * np.pi / 180

        merc_n = np.log(np.tan((np.pi / 4) + (lat_rad / 2)))
        y = (img_height / 2) - (img_width * merc_n / (2 * np.pi))

        return int(x), int(y)
