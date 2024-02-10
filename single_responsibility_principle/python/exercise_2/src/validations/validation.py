from abc import ABC, abstractmethod

class Validation(ABC):
    @abstractmethod
    def validate(self, value: str) -> bool:
        """ method to validate a value"""
        pass