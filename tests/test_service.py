import pytest
from nameko.testing.services import worker_factory
from src.service import MicroServiceA
from src.config import config


def test_method_A():
    service = worker_factory(MicroServiceA)
    result = service.method_A("foo")
    assert "Produced message: foo" in result
    assert "Consumed messages:" in result


def test_missing_env_var():
    import os

    os.environ.pop("KAFKA_BOOTSTRAP_SERVERS", None)
    os.environ.pop("SERVICE_NAME", None)
    os.environ.pop("TOPIC_NAME", None)

    from src.config import load_config

    config = load_config()

    assert config["KAFKA_BOOTSTRAP_SERVERS"] == "localhost:9092"
    assert config["SERVICE_NAME"] == "micro_service_A"
    assert config["TOPIC_NAME"] == "example_topic"
