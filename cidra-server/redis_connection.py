import redis
import logging

def get_redis_connection(config):
    """Establishes a connection to the Redis server."""
    try:
        redis_conn = redis.StrictRedis(
            host=config['redis']['host'],
            port=config['redis']['port'],
            db=config['redis']['db'],
            decode_responses=True
        )
        # Test the connection
        redis_conn.ping()
        logging.info("Connected to Redis successfully.")
        return redis_conn
    except Exception as e:
        logging.error(f"Failed to connect to Redis: {e}")
        return None