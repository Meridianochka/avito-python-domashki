"""Разбор вложенных json-словарей по конфигу."""


def extract_nested_value(obj: dict, keys: list):
    """Достает значение по цепочке ключей."""
    value = obj

    for key in keys:
        if not isinstance(value, dict) or key not in value:
            return None

        value = value[key]

    return value


def process_dictionary_with_config(dictionary: dict, config: dict) -> dict:
    """Делает из вложенного словаря плоский (по конфигу)."""
    flat = {}

    for attribute, rule in config.items():
        # кортеж в конфиге (путь, функция) значит, что значение обрабатываем
        if isinstance(rule, tuple):
            path_list, func = rule
        else:
            path_list, func = rule, None

        value = extract_nested_value(dictionary, path_list)

        if value is not None and func is not None:
            value = func(value)

        flat[attribute] = value

    return flat


def process_list_of_dicts_with_config(list_of_dicts: list,
                                      config: dict) -> list:
    """То же самое для списка словарей (например, призов)."""
    if list_of_dicts is None:
        return []

    return [process_dictionary_with_config(nested_dict, config)
            for nested_dict in list_of_dicts]


def create_processor(config: dict, list_processor: bool = False):
    """Возвращает функцию с уже подставленным конфигом."""
    def processor(data):
        if list_processor:
            return process_list_of_dicts_with_config(data, config)

        return process_dictionary_with_config(data, config)

    return processor


def main() -> None:
    """Проверка функций на маленьком словаре."""
    toy = {'a': {'b': {'c': '1998-10-12'}}, 'name': 'Anna'}
    toy_config = {
        'name': ['name'],
        'year': (['a', 'b', 'c'], lambda s: int(s[:4])),
        'lost': ['a', 'nothing'],
    }

    assert extract_nested_value(toy, ['a', 'b', 'c']) == '1998-10-12'
    assert extract_nested_value(toy, ['a', 'nothing']) is None
    assert process_dictionary_with_config(toy, toy_config) == {
        'name': 'Anna', 'year': 1998, 'lost': None,
    }
    assert process_list_of_dicts_with_config([toy, toy], toy_config) == [
        {'name': 'Anna', 'year': 1998, 'lost': None},
        {'name': 'Anna', 'year': 1998, 'lost': None},
    ]

    toy_processor = create_processor(toy_config)

    assert toy_processor(toy)['year'] == 1998

    print('json_dict_processing: все проверки прошли')


if __name__ == '__main__':
    main()
