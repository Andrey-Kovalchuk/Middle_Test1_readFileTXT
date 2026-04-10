import os
from abc import ABC, abstractmethod
from typing import List
from models import Country
from readers.DataReader import DataReader

class TextFileReader(DataReader):
    def read_data(self, file_path: str) -> List[Country]:
        """
        Зчитує дані з текстового файлу у форматі 'назва країни, площа, населення'.
        Повертає список об'єктів Country.
        """
        countries = []
        
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Файл {file_path} не знайдено.")

        with open(file_path, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, 1):
                line = line.strip()
                if not line:
                    continue  # Пропускаємо порожні рядки
                
                parts = [part.strip() for part in line.split(',')]
                
                if len(parts) != 3:
                    raise ValueError(f"Помилка формату у рядку {line_number}: очікується 3 значення, отримано {len(parts)}.")
                
                try:
                    name = parts[0]
                    area = float(parts[1])
                    population = int(parts[2])
                    countries.append(Country(name, area, population))
                except ValueError as e:
                    raise ValueError(f"Помилка конвертації типів у рядку {line_number}: {e}")
        
        return countries