t = int(input())
d = 0
curr = 0
while True:
    curr += 5
    if curr >= t:
        break
    curr -= 3
    d += 1

print(d)

