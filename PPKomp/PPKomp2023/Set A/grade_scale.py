def main():
    students = [int(input()) for _ in range(30)]
    total = 0
    for student in students:
        if 70 <= student <= 84:
            total += 1

    print(total)


if __name__ == "__main__":
    main()
