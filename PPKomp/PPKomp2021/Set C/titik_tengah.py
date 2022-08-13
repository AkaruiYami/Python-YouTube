# since map object cannot be access using [], we convert it to tuple first
a = tuple(map(float, input().split()))
m = tuple(map(float, input().split()))

xb = m[0] * 2 - a[0]
yb = m[1] * 2 - a[1]

print(f"{str(xb).removesuffix('.0')} {str(yb).removesuffix('.0')}")
