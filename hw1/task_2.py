from collections import Counter


def main():
    queries = [
        'чехол',
        'iphone',
        'чехол',
        'наушники',
        'iphone',
        'iphone',
        'кабель',
        'чехол',
        'iphone',
    ]

    counts = Counter(queries)

    top_query, top_count = counts.most_common(1)[0]

    share = round(top_count / len(queries) * 100, 1)

    once = [query for query, count in counts.items() if count == 1]

    print('всего запросов:', len(queries))
    print('сколько раз ввели каждый:', dict(counts))
    print('самый частый запрос:', top_query)
    print('его доля, %:', share)
    print('ввели один раз:', once)


if __name__ == '__main__':
    main()
