import json
import os

class Config(object):
    def __init__(self):
        self.api_key = ""
        self.environment = ""
        self.read_config()
        self.read_env()

    def read_config(self):
        config_file_path = "config.json"

        try:
            with open(config_file_path, "r") as file:
                config_data = json.load(file)
                self.api_key = config_data.get("api_key", "")
                self.environment = config_data.get("environment", "")
        except FileNotFoundError:
            print(f"Config file '{config_file_path}' not found. Make sure it exists.")

    def read_env(self):
        # If environment variables are set, override config values
        api_key_env = os.environ.get("API_KEY")
        environment_env = os.environ.get("ENVIRONMENT")

        if api_key_env:
            self.api_key = api_key_env
        if environment_env:
            self.environment = environment_env
