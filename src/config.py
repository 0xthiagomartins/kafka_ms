import os
import yaml


def load_config():
    config_file = os.path.join(os.path.dirname(__file__), "config.yml")
    with open(config_file, "r") as file:
        config = yaml.safe_load(file)

    config["KAFKA_BOOTSTRAP_SERVERS"] = os.getenv(
        "KAFKA_BOOTSTRAP_SERVERS", config["KAFKA_BOOTSTRAP_SERVERS"]
    )
    config["SERVICE_NAME"] = os.getenv("SERVICE_NAME", config["SERVICE_NAME"])
    config["TOPIC_NAME"] = os.getenv("TOPIC_NAME", config["TOPIC_NAME"])

    return config


config = load_config()
