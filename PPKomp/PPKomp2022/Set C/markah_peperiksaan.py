
def main():
    n = int(input())
    s = dict(input().split(",") for _ in range(n))
    r = dict((eval(mark), name) for name, mark in s.items())
    print(r[max(r.keys())])


if __name__ == '__main__':
    main()
