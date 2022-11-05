import re


def main():
    n = input()
    is_octal = True
    for c in n:
        c = int(c)
        if c not in range(8):
            is_octal = False
            break

    if is_octal:
        print("sah")
    else:
        print("tidak sah")


def alt_solution():
    n = input()

    p = re.compile(r"[^0-7]+")
    if re.search(p, n):
        print("tidak sah")
    else:
        print("sah")


if __name__ == "__main__":
    main()
    alt_solution()
