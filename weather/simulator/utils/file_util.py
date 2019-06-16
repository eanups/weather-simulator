import os


class FileUtil:

    file_path = os.path.abspath(os.path.dirname(__file__))
    resource_dir = "../../../resources"

    @classmethod
    def get_resource_file(cls, file_name):
        return os.path.join(cls.file_path, cls.resource_dir, file_name)
