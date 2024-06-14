import os
import yaml
import logging


def load_config():
    config_file = os.path.join(os.path.dirname(__file__), "config.yml")
    with open(config_file, "r") as file:
        config = yaml.safe_load(file)

    config["KAFKA_BOOTSTRAP_SERVERS"] = os.getenv(
        "KAFKA_BOOTSTRAP_SERVERS", config.get("KAFKA_BOOTSTRAP_SERVERS")
    )
    if "KAFKA_BOOTSTRAP_SERVERS" not in os.environ:
        logging.warning(
            "KAFKA_BOOTSTRAP_SERVERS not set in environment, using default from config.yml"
        )

    config["SERVICE_NAME"] = os.getenv("SERVICE_NAME", config.get("SERVICE_NAME"))
    if "SERVICE_NAME" not in os.environ:
        logging.warning(
            "SERVICE_NAME not set in environment, using default from config.yml"
        )

    config["TOPIC_NAME"] = os.getenv("TOPIC_NAME", config.get("TOPIC_NAME"))
    if "TOPIC_NAME" not in os.environ:
        logging.warning(
            "TOPIC_NAME not set in environment, using default from config.yml"
        )

    return config


config = load_config()
