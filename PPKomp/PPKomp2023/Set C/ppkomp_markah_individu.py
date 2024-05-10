s = "disyaki berbincang atau meniru atau memberi tiru"

"""
1. markah yang sama bagi kesemua enam soalan. kecuali yang jumlah markahnya 0
"""


n = int(input())
M = []
duplicate = set()
for _ in range(n):
    m = input()    
    if m in M:
        duplicate.add(m)
    M.append(m)

result = []
for m in M:
    total = sum(map(int, m.split(" ")))
    if total > 0 and m in duplicate:
        result.append(s)
    else:
        result.append(total)

print(*result, sep="\n")


