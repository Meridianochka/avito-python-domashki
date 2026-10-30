queries = [
    "чехол",
    "iphone",
    "чехол",
    "наушники",
    "iphone",
    "iphone",
    "кабель",
    "чехол",
    "iphone",
]

from collections import Counter

counts = Counter(queries)

print(len(queries))
print(counts)
print(counts.most_common(1))

top_q, top_c = counts.most_common(1)[0] 

print(round(top_c / len(queries) * 100, 1))

one = [q for q, c in counts.items() if c ==1]

print(one)