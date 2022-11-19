import datetime


def main():
    time0 = datetime.datetime.strptime(input(), "%H:%M")
    x = datetime.timedelta(minutes=int(input()))
    print(f"{time0 + x:%H:%M}")


if __name__ == "__main__":
    main()
