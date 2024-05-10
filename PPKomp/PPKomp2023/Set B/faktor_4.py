import math

n = int(input())

faktor = []
for i in range(1, int(math.sqrt(n)) + 1):
    if n % i == 0:
        faktor.append(i)
        pasangan = n // i
        if i == pasangan:
            continue
        faktor.append(pasangan)

print(*faktor)
print(len(faktor))
