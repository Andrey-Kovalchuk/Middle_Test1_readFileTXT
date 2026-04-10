import pytest
from src.readers.TextFileReader import TextFileReader

@pytest.fixture
def temp_data_file(tmp_path):
    # Створення тимчасового файлу для тестування зчитування
    file_path = tmp_path / "test_data.txt"
    file_path.write_text("США, 9833517, 331000000\nКанада, 9984670, 37742154", encoding="utf-8")
    return str(file_path)
def test_read_valid_data(temp_data_file):
    # Перевірка методу read_data на коректних даних
    reader = TextFileReader()
    countries = reader.read_data(temp_data_file)
    assert len(countries) == 2
    assert countries[0].name == "США"
    assert countries[1].population == 37742154