import pytest
from src.models import Country
from src.CountrySorter import CountrySorter

@pytest.fixture
def sample_countries():
    # Фікстура для надання тестових даних
    return [
        Country("Україна", 603628, 41000000),
        Country("Польща", 312696, 38000000),
        Country("Німеччина", 357022, 83000000)
    ]

@pytest.mark.parametrize("reverse, expected_first", [
    (True, "Україна"),  # Найбільша площа
    (False, "Польща")   # Найменша площа
])
def test_sort_by_area(sample_countries, reverse, expected_first):
    # Тестування методу сортування за площею
    sorted_list = CountrySorter.sort_by_area(sample_countries, reverse=reverse)
    assert sorted_list[0].name == expected_first

@pytest.mark.parametrize("reverse, expected_first", [
    (True, "Німеччина"), # Найбільше населення
    (False, "Польща")    # Найменше населення
])