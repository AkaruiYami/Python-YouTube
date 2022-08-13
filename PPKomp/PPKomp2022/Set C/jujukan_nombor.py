
def main():
    t = list(map(int, input().split(" ")))
    n_adds = int(input())

    d = t[1] - t[0]
    next_t = [t[-1] + (d * n) for n in range(1, n_adds+1)]

    print(*t, *next_t)


if __name__ == '__main__':
    main()
