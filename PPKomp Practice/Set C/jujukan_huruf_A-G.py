n = int(input())

HURUF = tuple("ABCDEFG")
t = HURUF[-abs((n-1)%12-6)+6]

print(t)