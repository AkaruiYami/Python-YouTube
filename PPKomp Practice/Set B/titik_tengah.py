titik_A = list(map(float, input().split()))
titik_M = list(map(float, input().split()))

xB = titik_M[0] * 2 - titik_A[0]
yB = titik_M[1] * 2 - titik_A[1]

print(f"{str(xB).removesuffix('.0')} {str(yB).removesuffix('.0')}")

