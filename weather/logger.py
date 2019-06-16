import logging
from logging.config import fileConfig

from weather.simulator.utils.file_util import FileUtil

fileConfig(FileUtil.get_resource_file('logging_conf.ini'))
log = logging.getLogger()


