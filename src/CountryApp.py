from typing import List, Tuple
from models import Country
from readers import DataReader
from sorters import CountrySorter

# Головний клас для керування процесом
class CountryApp:
    def __init__(self, reader: DataReader, sorter: CountrySorter):
        """Ін'єкція залежностей через конструктор."""
        self.reader = reader
        self.sorter = sorter
    def process(self, file_path: str) -> Tuple[List[Country], List[Country]]:
        """
        Основний метод, який зчитує дані та повертає два відсортовані списки.
        """
        countries = self.reader.read_data(file_path)
        
        sorted_by_area = self.sorter.sort_by_area(countries, reverse=True)
        sorted_by_population = self.sorter.sort_by_population(countries, reverse=True)
        
        return sorted_by_area, sorted_by_population