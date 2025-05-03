import json
import logging
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

CODE_FOLDER = os.getenv("CODE_FOLDER", "code")  # Fallback to "code" if not set
SERVER_PORT = os.getenv("SERVER_PORT", 4320)  # Fallback to 4320 if not set
REDIS_SERVER = os.getenv("REDIS_SERVER", "redis-server")
REDIS_PORT = os.getenv("REDIS_PORT", 6379)  # Fallback to 6379 if not set
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD", None)  # No password by default
REDIS_DB = os.getenv("REDIS_DB", 0)  # Default Redis database is 0
REDIS_URL = f"redis://{REDIS_SERVER}:{REDIS_PORT}/{REDIS_DB}"
COMPANY = os.getenv("COMPANY", "CIDRA")  # Fallback to "default_company" if not set

class Config:
    def __init__(self, config_data):
        self.config_data = config_data  

    def get_tools_summary(self):
        """Returns a summary of tools from the configuration."""
        tools = self.config_data.get("tools", [])
        return {
            "title": self.config_data.get("title", ""),
            "description": self.config_data.get("description", ""),
            "version": self.config_data.get("version", ""),
            "tools": [
                {
                    "id": tool.get("id"),
                    "title": tool.get("title"),
                    "description": tool.get("description"),
                }
                for tool in tools
            ],
        }

    def get_tool_config(self, tool_id):
        """Returns the configuration of a specific tool by its ID."""
        tools = self.config_data.get("tools", [])
        for tool in tools:
            if tool.get("id") == tool_id:
                return tool
        return None

def load_configurations():
    """Loads configurations from the config.json file."""
    try:
        config_path = os.path.join(CODE_FOLDER, "config.json")
        with open(config_path, "r") as config_file:
            config_data = json.load(config_file)
        config_data['company'] = COMPANY
        config_data['redis_url'] = REDIS_URL
        config_data['server_port'] = SERVER_PORT
        config_data['redis_password'] = REDIS_PASSWORD
        config_data['redis_db'] = REDIS_DB
        config_data['redis_server'] = REDIS_SERVER
        config_data['redis_port'] = REDIS_PORT
        config_data['code_folder'] = CODE_FOLDER
        return Config(config_data)
    except Exception as e:
        logging.error(f"Failed to load configurations: {e}")
        raise Exception("Error loading configurations.")