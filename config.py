import configparser
import os

DEFAULT_CONFIG = """
[global]
components_dir = /home/{username}/godot_components
"""


class Config:
    def __init__(self) -> None:
        self._username = os.getlogin()
        self.path = self.get_defaut_path()
        self._dirname = os.path.dirname(self.path)
        os.makedirs(self._dirname, exist_ok=True)

        self.config = configparser.ConfigParser()
        try:
            self.open_config_file()
        except FileNotFoundError:
            self.create_config_file()
        finally:
            self.fill_properties()

    def get_all_as_str(self):
        with open(self.path, "r") as config_file:
            content = config_file.read()
            return content

    def fill_properties(self):
        self.components_dir = self.config["global"]["components_dir"]

    def open_config_file(self):
        with open(self.path, "r") as config_file:
            self.config.read_file(config_file)

    def create_config_file(self):
        self.config.add_section("global")
        self.config["global"][
            "components_dir"
        ] = "/home/{username}/Drive/godot/godot-resources/components".format(
            username=self._username
        )

        with open(self.path, "w+") as config_file:
            self.config.write(config_file)

    def get_defaut_path(self):
        return f"/home/{self._username}/.config/gdcomp/conf.ini"
