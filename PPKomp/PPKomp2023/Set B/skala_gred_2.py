g = input()
n = int(input())
m = list(map(int, input().split(" ")))

gred_table = {
        "A": [85, 100],
        "B": [70, 84],
        "C": [60, 69],
        "D": [50, 59],
        "E": [40, 49],
        "F": [0, 39]
        }

total = 0
mn, mx = gred_table[g]
for _m in m:
    if mn <= _m <= mx:
        total += 1

print(total)
