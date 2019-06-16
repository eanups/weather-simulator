import json
import os

from weather.simulator.utils.file_util import FileUtil


class JsonReader:

    def __init__(self, json_file):
        def_json_file = FileUtil.get_resource_file(json_file)
        self.json_file = os.environ.get('JSON_FILE', def_json_file)

    def get_json(self):
        with open(self.json_file) as json_fh:
            return json.load(json_fh)

    def __repr__(self):
        return '''JsonReader(json_file) where JSON format is
               "{
                    "<city_name": {
                          "position": {
                          "latitude": <float>,
                          "longitude": <float>
                        },
                        "avg_temperature": <float>,
                        "avg_pressure": <float>,
                        "avg_humidity": <float>
                    }
                } 
                  .. '''