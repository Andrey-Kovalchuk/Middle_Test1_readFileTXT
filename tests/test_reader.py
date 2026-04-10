import pytest
from src.readers.TextFileReader import TextFileReader

@pytest.fixture
def temp_data_file(tmp_path):
    # Створення тимчасового файлу для тестування зчитування
    file_path = tmp_path / "test_data.txt"
    file_path.write_text("США, 9833517, 331000000\nКанада, 9984670, 37742154", encoding="utf-8")
    return str(file_path)