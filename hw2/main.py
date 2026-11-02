import csv
from collections import defaultdict


CSV_FILE = 'Corp_Summary.csv'
OUT_FILE = 'summary.csv'


def read_file(path: str) -> list[dict]:
    """Читает csv и возвращает список сотрудников."""
    with open(path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=';')
        workers = list(reader)

    return workers


def get_teams(workers: list[dict]) -> dict:
    """Собирает отделы по каждому департаменту."""
    teams = defaultdict(set)

    for worker in workers:
        teams[worker['Департамент']].add(worker['Отдел'])

    return teams


def get_stats(workers: list[dict]) -> dict:
    """Считает численность и зарплаты по каждому департаменту."""
    salaries = defaultdict(list)

    for worker in workers:
        salaries[worker['Департамент']].append(int(worker['Оклад']))

    stats = {}

    for dep, money in salaries.items():
        stats[dep] = {
            'count': len(money),
            'min': min(money),
            'max': max(money),
            'avg': round(sum(money) / len(money), 2),
        }

    return stats


def print_teams(teams: dict) -> None:
    """Печатает департаменты и их отделы."""
    for dep, names in teams.items():
        print(dep)

        for name in sorted(names):
            print('   ', name)

        print()


def print_stats(stats: dict) -> None:
    """Печатает сводку по департаментам."""
    for dep, row in stats.items():
        print(dep)
        print('    человек:', row['count'])
        print('    мин:', row['min'])
        print('    макс:', row['max'])
        print('    средняя:', row['avg'])
        print()


def save_stats(stats: dict, path: str = OUT_FILE) -> None:
    """Сохраняет сводку по департаментам в csv."""
    with open(path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(['Департамент', 'Человек', 'Мин', 'Макс', 'Средняя'])

        for dep, row in stats.items():
            writer.writerow([
                dep, row['count'], row['min'], row['max'], row['avg'],
            ])

    print('Отчет сохранен в', path)


def make_report(option: int, path: str = CSV_FILE,
                out: str = OUT_FILE) -> None:
    """Делает отчет по выбранному варианту."""
    workers = read_file(path)

    if option == 1:
        print_teams(get_teams(workers))
    elif option == 2:
        print_stats(get_stats(workers))
    elif option == 3:
        save_stats(get_stats(workers), out)
    else:
        raise ValueError('Вариант должен быть 1, 2 или 3')


def main() -> None:
    """Спрашивает вариант отчета и запускает его."""
    option = int(input('Выбери вариант (1, 2 или 3): '))

    make_report(option)


if __name__ == '__main__':
    main()
