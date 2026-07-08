from src.strategy import (
    EncryptionStrategy,
    CompressionStrategy,
    DataProcessor,
)


def test_encryption_strategy():
    data = [78, 82, 91]

    processor = DataProcessor(EncryptionStrategy())

    result = processor.execute(data)

    assert result == [value ^ 0x4F for value in data]


def test_compression_strategy():
    data = [100, 80]

    processor = DataProcessor(CompressionStrategy())

    result = processor.execute(data)

    assert result == [85.0, 68.0]


def test_change_strategy():
    data = [40]

    processor = DataProcessor(EncryptionStrategy())

    encrypted = processor.execute(data)

    processor.set_strategy(CompressionStrategy())

    compressed = processor.execute(data)

    assert encrypted != compressed