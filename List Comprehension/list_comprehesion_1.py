fruits = [
    "Apple",
    "Avocado",
    "Akee",
    "Araza",
    "Alibertia",
    "Apricot",
    "Blueberry",
    "Blackberry",
    "Barberry",
    "Banana",
    "Bignay",
    "Biriba",
    "Breadfruit",
    "Barbados Cherry",
    "Bael Fruit",
    "Black Sapote",
    "Bilberry",
    "Boysenberry",
    "Balckcurrant",
    "Date",
    "Durian",
]

lst1 = []
for fruit in fruits:
    if fruit.lower().startswith("d"):
        lst1.append(fruit)

lst2 = [fruit for fruit in fruits if fruit.lower().startswith("d")]

lst3 = [i for i in range(10) if i % 2 == 0]

lst4 = [i if i % 2 == 0 else "GANJIL" for i in range(10)]

lst5 = [i if i % 2 == 0 else "GANJIL" for i in range(10) if i % 2 == 0]

print(f"{lst1=}")
print(f"{lst2=}")
print(f"{lst3=}")
print(f"{lst4=}")
print(f"{lst5=}")
