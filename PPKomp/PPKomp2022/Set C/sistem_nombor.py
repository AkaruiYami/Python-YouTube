def main():
    total = 0
    while True:
        n = input()
        if n == "-1":
            break

        base, nom = n.split(" ")
        total += int(nom, int(base))

    print(total)


if __name__ == "__main__":
    main()
