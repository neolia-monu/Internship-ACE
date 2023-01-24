"""
    Find common element in three sorted arrays by
    dictionary intersection
"""

from collections import Counter

ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]

d1 = Counter(ar1)
d2 = Counter(ar2)
d3 = Counter(ar3)

d = dict(d1.items() & d2.items() & d3.items())
res = []

for key, value in d.items():
    res.append(key)

print("First:", res)

#2nd method
d = dict(d1.items() & d2.items() & d3.items())
print("Second:", list(d.keys()))