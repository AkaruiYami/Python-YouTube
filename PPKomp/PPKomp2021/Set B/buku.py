import math

s = int(input())

# s = (1 + n) / 2 * n
# 2 * s = (1 + n) * n
# 2 * s = n^2 + n
# n^2 + n = 2 * s
# (n + 1/2)^2 = 2 * s + (1/2)^2
# (n + 0.5)^2 = 2 * s + 0.25
# n + 0.5 = sqrt(2 * s + 0.25)
# n = sqrt(2 * s + 0.25) - 0.5
n = math.sqrt(2 * s + 0.25) - 0.5

print(n)
