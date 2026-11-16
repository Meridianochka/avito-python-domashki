"""Конфиг и процессор для призов."""

from json_dict_processing import create_processor


CONFIG_PRIZE = {
    'prize_amount': ['prizeAmount'],
    'prize_amount_adjusted': ['prizeAmountAdjusted'],
    'award_year': (['awardYear'], int),
    'category_en': ['category', 'en'],
    'prize_status': ['prizeStatus'],
    # для бонуса (частоты слов в мотивациях)
    'motivation_en': ['motivation', 'en'],
}


def prize_processor():
    """Процессор для списка призов."""
    return create_processor(CONFIG_PRIZE, list_processor=True)
