def main():
    plat = input()

    # Method 1: Using For loop
    # total = 0
    # for c in plat:
    #     if c.isdigit():
    #         total += int(c)
    # print(total)

    # Method 2: Using filter function
    res = "+".join(filter(lambda c: c.isdigit(), plat))
    print(eval(res))


if __name__ == "__main__":
    main()
