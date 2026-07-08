from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def process(self, data):
        pass


class EncryptionStrategy(Strategy):
    def __init__(self, key=0x4F):
        self.key = key

    def process(self, data):
        return [value ^ self.key for value in data]


class CompressionStrategy(Strategy):
    def __init__(self, factor=0.85):
        self.factor = factor

    def process(self, data):
        return [round(value * self.factor, 2) for value in data]


class DataProcessor:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def execute(self, data):
        return self.strategy.process(data)
