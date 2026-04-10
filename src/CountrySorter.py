from typing import List
from models import Country

# Клас, що відповідає виключно за сортування
class CountrySorter:
    @staticmethod
    def sort_by_area(countries: List[Country], reverse: bool = False) -> List[Country]:
        """Повертає новий відсортований список за площею."""
        return sorted(countries, key=lambda c: c.area, reverse=reverse) 