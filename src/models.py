from dataclasses import dataclass

# Клас для представлення моделі даних
@dataclass
class Country:
    name: str
    area: float
    population: int