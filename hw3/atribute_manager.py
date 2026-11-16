"""Добавление и удаление полей у списка плоских словарей."""


def add_attribute(rows: list, name: str, func) -> list:
    """Добавляет поле (значение считает функция от всей строки)."""
    for row in rows:
        row[name] = func(row)

    return rows


def drop_attribute(rows: list, name: str) -> list:
    """Убирает поле, если оно есть."""
    for row in rows:
        row.pop(name, None)

    return rows


def count_missing(rows: list) -> dict:
    """Считает пустые значения по каждому полю."""
    missing = {}

    for row in rows:
        for field, value in row.items():
            if field not in missing:
                missing[field] = 0

            if value is None or value == [] or value == '':
                missing[field] += 1

    return missing


def main() -> None:
    """Проверка добавления и удаления поля."""
    people = [
        {'name': 'Alice', 'age': 25},
        {'name': 'Bob', 'age': None},
    ]

    add_attribute(people, 'is_adult', lambda row: row['age'] is not None)

    assert people[0]['is_adult'] is True
    assert count_missing(people) == {'name': 0, 'age': 1, 'is_adult': 0}

    drop_attribute(people, 'is_adult')

    assert 'is_adult' not in people[0]

    print('atribute_manager: все проверки прошли')


if __name__ == '__main__':
    main()
