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