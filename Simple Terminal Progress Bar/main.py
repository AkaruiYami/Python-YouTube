import time


def progress_bar(t_i, c_i, bar_length, fill):
    percent = f"{100 * c_i / float(t_i):.1f}"
    percent = 100 * c_i / float(t_i)
    fill_length = bar_length * c_i // t_i
    bar = fill * fill_length + "-" * (bar_length - fill_length)

    print(f"\rProgress: |{bar}| {percent}%", end="")

    if c_i == t_i:
        print()


total_iteration = 30
for i in range(total_iteration + 1):
    progress_bar(total_iteration, i, 15, ">")
    time.sleep(0.1)
