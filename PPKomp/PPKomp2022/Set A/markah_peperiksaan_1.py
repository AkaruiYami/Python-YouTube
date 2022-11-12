# Baris pertama mengandungi markah subjek Bahasa Melayu.
# Baris kedua mengandungi markah subjek Bahasa Inggeris.
# Baris ketiga mengandungi markah subjek Sains.
# Baris keempat mengandungi markah subjek Matematik.


def main():
    marks = {"Bahasa Melayu": 0, "Bahasa Inggeris": 0, "Sains": 0, "Matematik": 0}
    for key in marks.keys():
        marks[key] = eval(input())
    
    hi = max(marks, key = marks.get)
    print(hi)


if __name__ == "__main__":
    main()
