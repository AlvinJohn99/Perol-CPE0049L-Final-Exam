from src.factory import ServiceFactory
from src.strategy import DataProcessor


def test_create_encryption_service():
    service = ServiceFactory.create_service("encryption")
    assert isinstance(service, DataProcessor)


def test_create_compression_service():
    service = ServiceFactory.create_service("compression")
    assert isinstance(service, DataProcessor)


def test_invalid_service():
    try:
        ServiceFactory.create_service("invalid")
        assert False
    except ValueError:
        assert True