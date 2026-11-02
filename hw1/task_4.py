def main():
    days = [
        {'day': 'пн', 'orders': 20, 'revenue': 40_000, 'returns': 2},
        {'day': 'вт', 'orders': 16, 'revenue': 19_200, 'returns': 4},
        {'day': 'ср', 'orders': 25, 'revenue': 55_000, 'returns': 1},
        {'day': 'чт', 'orders': 10, 'revenue': 12_000, 'returns': 3},
        {'day': 'пт', 'orders': 30, 'revenue': 48_000, 'returns': 3},
    ]

    week_revenue = sum(d['revenue'] for d in days)

    best = max(days, key=lambda d: d['revenue'])

    bad_days = [d['day'] for d in days if d['returns'] / d['orders'] > 0.2]

    print('выручка за неделю:', week_revenue)
    print('лучший день:', best['day'], best['revenue'])
    print('средняя выручка на заказ:')

    for day in days:
        print('   ', day['day'], day['revenue'] / day['orders'])

    print('возвратов больше 20%:', bad_days)


if __name__ == '__main__':
    main()
