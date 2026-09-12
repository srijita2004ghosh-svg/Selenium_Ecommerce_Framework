import configparser
import os


class ConfigReader:

    @staticmethod
    def get_config():
        config = configparser.ConfigParser()

        project_root = os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))
        )

        config_path = os.path.join(
            project_root,
            "config",
            "config.ini"
        )

        config.read(config_path)

        return config