"""Свои where и group by для списка плоских словарей (как в sql)."""


def filter_rows(rows: list, conditions: dict) -> list:
    """Оставляет строки, которые подходят под условия.

    В условиях можно передать значение или функцию-проверку.
    """
    good = []

    for row in rows:
        fits = True

        for field, condition in conditions.items():
            value = row.get(field)

            if callable(condition):
                fits = condition(value)
            else:
                fits = value == condition

            if not fits:
                break

        if fits:
            good.append(row)

    return good


def group_by_attributes(rows: list, attributes: list) -> dict:
    """Группирует строки по полям (ключ - кортеж значений)."""
    groups = {}

    for row in rows:
        key = tuple(row.get(attribute) for attribute in attributes)
        groups.setdefault(key, []).append(row)

    return groups


def apply_aggregation(groups: dict, aggregation, field: str = None) -> dict:
    """Считает агрегацию внутри каждой группы."""
    result = {}

    for key, rows in groups.items():
        if field is None:
            result[key] = aggregation(rows)
        else:
            result[key] = aggregation(rows, field)

    return result


def main() -> None:
    """Проверка фильтра и группировки на выдуманных людях."""
    people = [
        {'name': 'Alice', 'country': 'USA', 'age': 25},
        {'name': 'Bob', 'country': 'UK', 'age': 30},
        {'name': 'Charlie', 'country': 'USA', 'age': 25},
    ]

    assert filter_rows(people, {'country': 'USA'}) == [people[0], people[2]]
    assert filter_rows(people, {'age': lambda age: age > 26}) == [people[1]]
    assert group_by_attributes(people, ['country', 'age']) == {
        ('USA', 25): [people[0], people[2]],
        ('UK', 30): [people[1]],
    }

    groups = group_by_attributes(people, ['country'])

    assert apply_aggregation(groups, len) == {('USA',): 2, ('UK',): 1}

    print('dataset_helpers: все проверки прошли')


if __name__ == '__main__':
    main()
