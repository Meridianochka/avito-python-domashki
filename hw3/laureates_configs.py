"""Конфиги и процессоры для лауреатов (люди и организации)."""

from json_dict_processing import create_processor
from prizes_configs import prize_processor


def process_year(year_string: str) -> int:
    """Год из даты (приходит строкой вида 1943-11-07)."""
    return int(year_string[:4])


CONFIG_PERSON = {
    'id': (['id'], int),
    'name': ['knownName', 'en'],
    'gender': ['gender'],
    'birth_year': (['birth', 'date'], process_year),
    'country_birth': ['birth', 'place', 'country', 'en'],
    'country_now': ['birth', 'place', 'countryNow', 'en'],
    'prizes_relevant': (['nobelPrizes'], prize_processor()),
}

CONFIG_ORG = {
    'id': (['id'], int),
    'name': ['orgName', 'en'],
    'founded_year': (['founded', 'date'], process_year),
    'country_founded': ['founded', 'place', 'country', 'en'],
    'country_now': ['founded', 'place', 'countryNow', 'en'],
    'prizes_relevant': (['nobelPrizes'], prize_processor()),
}


def person_processor():
    """Процессор для лауреатов-людей."""
    return create_processor(CONFIG_PERSON)


def org_processor():
    """Процессор для лауреатов-организаций."""
    return create_processor(CONFIG_ORG)


process_persons = person_processor()
process_orgs = org_processor()


def main() -> None:
    """Проверка процессора на куске настоящего словаря из апи."""
    person = {
        'id': '745',
        'knownName': {'en': 'A. Michael Spence'},
        'gender': 'male',
        'birth': {'date': '1943-11-07',
                  'place': {'country': {'en': 'USA'},
                            'countryNow': {'en': 'USA'}}},
        'nobelPrizes': [{'awardYear': '2001',
                         'category': {'en': 'Economic Sciences'},
                         'prizeStatus': 'received'}],
    }
    flat = process_persons(person)

    assert process_year('1943-11-07') == 1943
    assert flat['id'] == 745
    assert flat['birth_year'] == 1943
    assert flat['prizes_relevant'][0]['award_year'] == 2001
    assert flat['prizes_relevant'][0]['prize_amount'] is None

    print('laureates_configs: все проверки прошли')


if __name__ == '__main__':
    main()
