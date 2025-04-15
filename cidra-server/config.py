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

def load_configurations():
    """Loads configurations from the config.json file."""
    try:
        config_path = os.path.join(CODE_FOLDER, "config.json")
        with open(config_path, "r") as config_file:
            config = json.load(config_file)
        config['company'] = COMPANY
        config['redis_url'] = REDIS_URL
        config['server_port'] = SERVER_PORT
        config['redis_password'] = REDIS_PASSWORD
        config['redis_db'] = REDIS_DB
        config['redis_server'] = REDIS_SERVER
        config['redis_port'] = REDIS_PORT
        config['code_folder'] = CODE_FOLDER
        return config
    except Exception as e:
        logging.error(f"Failed to load configurations: {e}")
        raise Exception("Error loading configurations.")