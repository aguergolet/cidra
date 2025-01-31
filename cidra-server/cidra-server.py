import os
import redis
import logging
from flask import Flask, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

# Configurations
company = os.getenv("COMPANY", "Unknown")
repository = os.getenv("REPOSITORY", "local")
redis_host = os.getenv("REDIS_SERVER", "localhost")
redis_port = int(os.getenv("REDIS_PORT", 6379))
data_timeout = int(os.getenv("DATA_TIMEOUT", 30))

logging.info(f"Configurations loaded for {company}")

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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
