from readers import TextFileReader
from sorters import CountrySorter
from app import CountryApp

if __name__ == "__main__":
    # Створюємо тестовий файл для перевірки
    test_file_path = "countries_data.txt"
    with open(test_file_path, "w", encoding="utf-8") as f:
        f.write("Україна, 603628, 41000000\n")
        f.write("Польща, 312696, 38000000\n")
        f.write("Німеччина, 357022, 83000000\n")

    # Ініціалізація компонентів
    reader = TextFileReader()
    sorter = CountrySorter()
    app = CountryApp(reader, sorter)

    try:
        # Запуск процесу
        by_area, by_pop = app.process(test_file_path)

        print("--- Сортування за площею (за спаданням) ---")
        for c in by_area:
            print(f"{c.name}: {c.area} кв. км")

        print("\n--- Сортування за населенням (за спаданням) ---")
        for c in by_pop:
            print(f"{c.name}: {c.population} осіб")

    except Exception as e:
        print(f"Сталася помилка: {e}")