g = input()
n = int(input())
M = list(map(int, input().split(" ")))

grade_tabel = {
        "A": (85, 100),
        "B": (70, 84),
        "C": (60, 69),
        "D": (50, 59),
        "E": (40, 49),
        "F": (0, 39)
        }

mn, mx = grade_tabel[g]
total = 0
for m in M:
    if mn <= m <= mx:
        total += 1
print(total)
