import os
from abc import ABC, abstractmethod
from typing import List
from src.models import Country

# Інтерфейс для зчитування даних
class DataReader(ABC):
    @abstractmethod
    def read_data(self, file_path: str) -> List[Country]:
        """Абстрактний метод для зчитування даних з файлу."""
        pass