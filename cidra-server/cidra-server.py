import os
import json
import logging
from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv

# Clean Architecture adjustments for better separation of concerns and maintainability
# Create a dedicated module for configuration
from config import load_configurations

# Create a dedicated module for Redis connection
from redis_connection import get_redis_connection

# Create a dedicated module for tool execution
from tool_execution import execute_tool

# Main application setup
load_dotenv()

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

logging.basicConfig(level=logging.INFO)

# Load configurations
config = load_configurations()
logging.info(f"Configurations loaded for {config.config_data['company']}")

@app.route("/health", methods=["GET"])
def health_check():
    """Returns the health status of the application."""
    logging.info("Health check endpoint called.")
    redis_conn = get_redis_connection(config)
    if (redis_conn):
        logging.info("Redis connection is healthy.")
        return jsonify({"status": "healthy", "redis": "connected"}), 200
    logging.warning("Redis connection is degraded.")
    return jsonify({"status": "degraded", "redis": "disconnected"}), 500

@app.route("/liveness", methods=["GET"])
def liveness_probe():
    """Kubernetes liveness probe."""
    return jsonify({"status": "alive"}), 200

@app.route("/config", methods=["GET"])
def get_config():
    """Returns the title, description, and list of tools from config.json."""
    logging.info("Config endpoint called.")
    try:
        tools_summary = config.get_tools_summary()
        logging.info("Configurations retrieved successfully.")
        return jsonify(tools_summary), 200
    except Exception as e:
        logging.error(f"Failed to load configuration: {e}")
        return jsonify({"error": "Failed to load configuration."}), 500

@app.route("/getconfig/<tool_id>", methods=["GET"])
def get_tool_config(tool_id):
    """Returns the configuration of a specific tool from config.json."""
    logging.info(f"Tool config endpoint called for tool_id: {tool_id}")
    try:
        tool_config = config.get_tool_config(tool_id)
        if tool_config:
            logging.info(f"Configuration for tool_id {tool_id} retrieved successfully.")
            return jsonify(tool_config), 200
        logging.warning(f"Tool with ID {tool_id} not found.")
        return jsonify({"error": "Tool not found."}), 404
    except Exception as e:
        logging.error(f"Failed to load tool configuration: {e}")
        return jsonify({"error": "Failed to load tool configuration."}), 500

@app.route("/runCommand", methods=["POST", "OPTIONS"])
def run_command():
    logging.info("Run command endpoint called.")
    options = handle_options()
    if options:
        return options
    try:
        information = json.loads(request.data)
        logging.info(f"Received command: {information['id']}")
        id = information['id']
        params = information['params']
        results = execute_tool(id, params, config)
        logging.info(f"Command {id} executed successfully.")
        return results
    except Exception as e:
        logging.error(f"Failed to process command: {e}")
        return jsonify({"error": "Failed to process command."}), 500

def handle_options():
    print(request.method)
    if request.method == "OPTIONS":
        # Handle preflight request
        response = app.make_default_options_response()
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Methods"] = "POST, OPTIONS"
        response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
        return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config.config_data['server_port'])

