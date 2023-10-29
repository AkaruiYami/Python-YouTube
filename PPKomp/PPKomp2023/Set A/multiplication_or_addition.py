def main():
    a, b = map(int, input().split())
    r = a * b
    if r <= 10_000:
        print(r)
    else:
        print(a + b)


if __name__ == "__main__":
    main()
