set_huruf = "ABCDEFG"

n = int(input())
n_set_huruf = len(set_huruf)

print(set_huruf[n % n_set_huruf - 1])
