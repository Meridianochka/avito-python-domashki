"""Считалки для списков плоских словарей (среднее, медиана, топ)."""

import statistics


def get_values(rows: list, field: str) -> list:
    """Собирает значения поля, пропуски выкидывает."""
    return [row[field] for row in rows if row.get(field) is not None]


def count_rows(rows: list) -> int:
    """Сколько всего строк."""
    return len(rows)


def mean_value(rows: list, field: str):
    """Среднее по полю (None, если считать нечего)."""
    values = get_values(rows, field)

    if not values:
        return None

    return round(statistics.mean(values), 2)


def median_value(rows: list, field: str):
    """Медиана по полю."""
    values = get_values(rows, field)

    if not values:
        return None

    return statistics.median(values)


def max_value(rows: list, field: str):
    """Самое большое значение поля."""
    values = get_values(rows, field)

    if not values:
        return None

    return max(values)


def min_value(rows: list, field: str):
    """Самое маленькое значение поля."""
    values = get_values(rows, field)

    if not values:
        return None

    return min(values)


def top_n(metrics: dict, n: int = 5, biggest: bool = True) -> list:
    """Первые n объектов с самой большой метрикой."""
    pairs = [(key, value) for key, value in metrics.items()
             if value is not None]
    pairs.sort(key=lambda pair: pair[1], reverse=biggest)

    return pairs[:n]


def main() -> None:
    """Проверка считалок на выдуманных людях."""
    people = [
        {'name': 'Alice', 'age': 25},
        {'name': 'Bob', 'age': 30},
        {'name': 'Charlie', 'age': None},
    ]

    assert count_rows(people) == 3
    assert get_values(people, 'age') == [25, 30]
    assert mean_value(people, 'age') == 27.5
    assert median_value(people, 'age') == 27.5
    assert max_value(people, 'age') == 30
    assert min_value(people, 'age') == 25
    assert mean_value(people, 'height') is None
    assert top_n({'a': 5, 'b': 7, 'c': None}, 1) == [('b', 7)]

    print('aggregations: все проверки прошли')


if __name__ == '__main__':
    main()
