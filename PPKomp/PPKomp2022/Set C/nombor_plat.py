def main():
    n = int(input())
    plats = [input() for _ in range(n)]

    for plat in plats:
        filter_func = lambda c: c.isdecimal()
        digits = list(filter(filter_func, list(plat)))
        digits = list(map(int, digits))

        r = ""
        total = sum(digits)
        if total % 2 != 0:
            r += "S1"

        if all([n % 2 != 0 for n in digits]):
            r += "S2"

        if r == "":
            print(total)
        else:
            print(r)


if __name__ == "__main__":
    main()
