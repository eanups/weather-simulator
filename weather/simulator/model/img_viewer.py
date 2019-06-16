import matplotlib.pyplot as plt
import matplotlib.patches as patches

from weather.simulator.readers.img_reader import ImageReader
from weather.simulator.utils import weather_config as c


class ImageViewer:

    @classmethod
    def display(cls, city, x, y):
        """
        Display Image with co-ordinates
        :param city: city name
        :param x: Pixel x location
        :param y: Pixel y location
        :return: Image display
        """

        # Create figure and axes
        fig, ax = plt.subplots(1)

        ax.imshow(ImageReader.get_pixels())

        # Create a Rectangular patch
        rect = patches.Rectangle((x, y), c.DELTA * 2, c.DELTA * 2, linewidth=1, edgecolor='black', facecolor='none')
        ax.add_patch(rect)

        plt.annotate("  " + city, (x, y))

        plt.show()
