n = int(input())

l = "ABCDEFG"

def translation(n):
    m = len(l)
    n = (n-1) % 12
    if n < m:
        return n
    return n - 2 * (n - (m-1))

print(l[translation(n)])