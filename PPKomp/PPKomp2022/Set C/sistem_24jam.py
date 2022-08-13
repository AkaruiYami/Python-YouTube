import datetime

def main():
    inp = input()
    s = int(input())
    curr_time = datetime.datetime.strptime(inp, "%H:%M:%S") 
    delta_time = datetime.timedelta(seconds=s)
    r = curr_time + delta_time
    print(r.strftime("%H:%M:%S"))


if __name__ == '__main__':
    main()
