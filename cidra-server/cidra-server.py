import os
import redis
import logging
import json
from flask import Flask, jsonify
from dotenv import load_dotenv
from flask_cors import CORS 

load_dotenv()

app = Flask(__name__)
CORS(app)
logging.basicConfig(level=logging.INFO)

# Configurations
company = os.getenv("COMPANY", "Unknown")
repository = os.getenv("REPOSITORY", "local")
redis_host = os.getenv("REDIS_SERVER", "localhost")
redis_port = int(os.getenv("REDIS_PORT", 6379))
data_timeout = int(os.getenv("DATA_TIMEOUT", 30))
code_folder = os.getenv("CODE_FOLDER", "code")
config_path = os.path.join(code_folder, "config.json")

logging.info(f"Configurations loaded for {company}")

# Validate the presence of config.json
if not os.path.exists(code_folder):
    os.makedirs(code_folder, exist_ok=True)
    logging.error(f"Code folder '{code_folder}' does not exist. Please download the application.")
    raise FileNotFoundError(f"Code folder '{code_folder}' not found.")

if not os.path.exists(config_path):
    logging.error(f"Configuration file '{config_path}' is missing. Please ensure it is available.")
    raise FileNotFoundError(f"Configuration file '{config_path}' not found.")

def get_redis_connection():
    """Establishes and returns a Redis connection."""
    try:
        r = redis.Redis(host=redis_host, port=redis_port, socket_timeout=data_timeout)
        r.ping()
        logging.info("Redis connection established successfully")
        return r
    except redis.exceptions.ConnectionError:
        logging.error("Failed to connect to Redis")
        return None

@app.route("/health", methods=["GET"])
def health_check():
    """Returns the health status of the application."""
    redis_conn = get_redis_connection()
    if redis_conn:
        return jsonify({"status": "healthy", "redis": "connected"}), 200
    return jsonify({"status": "degraded", "redis": "disconnected"}), 500

@app.route("/liveness", methods=["GET"])
def liveness_probe():
    """Kubernetes liveness probe."""
    return jsonify({"status": "alive"}), 200

@app.route("/config", methods=["GET"])
def get_config():
    """Returns the title, description, and list of tools from config.json."""
    try:
        with open(config_path, "r") as f:
            config_data = json.load(f)
        tools_summary = [{"id": tool["id"], "title": tool["title"], "description": tool["description"]} for tool in config_data.get("tools", [])]
        return jsonify({
            "title": config_data.get("title", "Unknown"),
            "description": config_data.get("description", "No description available"),
            "tools": tools_summary
        }), 200
    except Exception as e:
        logging.error(f"Failed to read config.json: {e}")
        return jsonify({"error": "Failed to load configuration."}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
