import os
import PIL
from skimage import io


from weather.simulator.utils.file_util import FileUtil


class ImageReader:

    def_elevation_map = "gebco_08_rev_elev_21600x10800.png"

    # Setting to exceed the max pixels that can be rendered.
    PIL.Image.MAX_IMAGE_PIXELS = 233280000

    def_img_path = FileUtil.get_resource_file(def_elevation_map)
    img_file_path = os.environ.get('ELEV_IMG_FILE_PATH', def_img_path)
    pixels = io.imread(img_file_path)

    @classmethod
    def get_pixels(cls):
        return cls.pixels





