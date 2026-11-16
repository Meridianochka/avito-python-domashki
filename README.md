# avito-python-domashki

Домашки по курсу Python.

## Зависимости

Для hw1 и hw2 хватит питона 3.9 или новее, ничего ставить не надо.

Для hw3 нужны три библиотеки: requests (чтобы скачать данные с
api.nobelprize.org), matplotlib (графики) и jupyter (сам ноутбук).

```
python3 -m venv venv
source venv/bin/activate
pip install requests matplotlib jupyter
```

## Запуск

hw1 это пять отдельных файлов, каждый запускается сам по себе:

```
python3 hw1/task_1.py
```

hw2 читает `Corp_Summary.csv` из своей же папки и спрашивает номер отчета:

```
cd hw2
python3 main.py
```

Отчеты такие:

1. департаменты и отделы внутри каждого из них
2. по каждому департаменту: сколько человек, минимальная, максимальная и
   средняя зарплата
3. та же сводка в файл `summary.csv` рядом с main.py

hw3 это анализ нобелевских лауреатов, весь разбор лежит в ноутбуке:

```
cd hw3
jupyter notebook laureates_countries_task.ipynb
```

Данные ноутбук забирает из открытого апи нобелевского комитета, скачивать
ничего заранее не нужно.

Файлы hw3:

- `json_dict_processing.py` - разбор вложенных json-словарей по конфигу
- `prizes_configs.py` и `laureates_configs.py` - конфиги и процессоры для
  призов, людей и организаций
- `dataset_helpers.py` - фильтрация и группировка списка словарей
- `aggregations.py` - среднее, медиана, минимум, максимум, топ-N
- `atribute_manager.py` - добавить или убрать поле, посчитать пропуски
- `stopwords.py` - стоп-слова для бонуса про мотивации

Модули с логикой проверяют сами себя на маленьких примерах, запускаются
напрямую:

```
python3 hw3/json_dict_processing.py
python3 hw3/dataset_helpers.py
python3 hw3/aggregations.py
python3 hw3/atribute_manager.py
```
