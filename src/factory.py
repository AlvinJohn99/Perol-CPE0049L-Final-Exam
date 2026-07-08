from src.strategy import EncryptionStrategy, CompressionStrategy, DataProcessor


class ServiceFactory:
    @staticmethod
    def create_service(service_name):
        service_name = service_name.lower()

        if service_name == "encryption":
            return DataProcessor(EncryptionStrategy())

        if service_name == "compression":
            return DataProcessor(CompressionStrategy())

        raise ValueError(f"Unknown service: {service_name}")
