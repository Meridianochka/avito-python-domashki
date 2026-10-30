from collections import defaultdict

reviews = [
    {"id": 1, "product": "Чехол", "stars": 5},
    {"id": 1, "product": "Чехол", "stars": 3},
    {"id": 1, "product": "Чехол", "stars": 4},
    {"id": 2, "product": "Наушники", "stars": 2},
    {"id": 2, "product": "наушники", "stars": 2},
    {"id": 2, "product": "НАУШНИКИ", "stars": 5},
    {"id": 3, "product": "Планшет", "stars": 5},
    {"id": 4, "product": "Колонка", "stars": 4},
    {"id": 4, "product": "Колонка", "stars": 4},
    {"id": 5, "product": "Кабель", "stars": 1},
]

by_product = defaultdict(list)

for r in reviews:
    name = r['product'].lower()
    by_product[name].append(r['stars'])

avg_stars = {}

for name, stars in by_product.items():
    avg_stars[name] = sum(stars) / len(stars)

print(avg_stars)

candidates = {}

for name, avg in avg_stars.items():
    if len(by_product[name]) >= 2:
        candidates[name] = avg

worst = min(candidates, key=candidates.get)

print(worst, candidates[worst])

low = [r for r in reviews if r['stars'] <= 2]

print(len(low))

share = len(low) / len(reviews) * 100

print(round(share, 1))