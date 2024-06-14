import pytest
from nameko.testing.services import worker_factory
from src.service import MicroServiceA
from src.config import config


def test_method_A():
    service = worker_factory(MicroServiceA)
    result = service.method_A("foo")
    assert "Produced message: foo" in result
    assert "Consumed messages:" in result
