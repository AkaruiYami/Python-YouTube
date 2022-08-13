# n = int(input())

# total = 0
# for i in range(1, n+1):
#     if i % 2 == 0:
#         total += i
#     else:
#         total -= i

# print(total)


import math

n = int(input())
r = math.ceil(n/2) if n%2 == 0 else math.ceil(n/2) * -1

print(r)