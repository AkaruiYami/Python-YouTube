import math

def main():
    p, l = map(int, input().split())
    m, n = map(int, input().split())

    if p < l:
        p, l = l, p

    x1 = math.floor(m / p)
    y1 = math.floor(n / l)

    balance_m = m - (x1 * p)
    x2 = 0
    y2 = 0
    if balance_m >= l:
        x2 = math.floor(balance_m / l)
        y2 = math.floor(n / p)

    print((x1 * y1) + (x2 * y2))
    


if __name__ == '__main__':
    main()
