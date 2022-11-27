
def main():
    seq = list(map(int, input().split()))
    n = int(input())

    d = seq[1] - seq[0]
    cont_seq = [seq[-1] + (d * i) for i in range(1, n+1)]

    print(*seq, *cont_seq)


if __name__ == '__main__':
    main()
