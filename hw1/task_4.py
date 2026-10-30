days = [
    {"day": "пн", "orders": 20, "revenue": 40_000, "returns": 2},
    {"day": "вт", "orders": 16, "revenue": 19_200, "returns": 4},
    {"day": "ср", "orders": 25, "revenue": 55_000, "returns": 1},
    {"day": "чт", "orders": 10, "revenue": 12_000, "returns": 3},
    {"day": "пт", "orders": 30, "revenue": 48_000, "returns": 3},
]

week_revenue = sum(d["revenue"] for d in days)
print(week_revenue)

best = max(days, key=lambda d: d["revenue"])
print(best["day"], best["revenue"])

for d in days:
    print(d['day'], d['revenue'] / d['orders'])

bad_days = [d["day"] for d in days if d["returns"] / d["orders"] > 0.2]
print(bad_days)

