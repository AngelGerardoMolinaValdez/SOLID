from abc import ABC, abstractmethod

class Recorder(ABC):
    @abstractmethod
    def create(self, data: dict) -> None:
        """ method to create a Recorder in a specific way"""
