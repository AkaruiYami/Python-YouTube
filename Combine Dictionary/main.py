# How to combine dictionary
def method1():
    # combine dictionary using method update
    d1 = {"a": 1, "b": 2, "c": 3}
    d2 = {"d": 4, "e": 5}
    extra_dict = {"f": 6, "g": 7}

    d3 = {}
    d3.update(d1)
    d3.update(d2)
    d3.update(extra_dict)
    print(d3)


def method2():
    # combine dictionary using unpacking
    d1 = {"a": 1, "b": 2, "c": 3}
    d2 = {"d": 4, "e": 5}
    extra_dict = {"f": 6, "g": 7}

    d3 = {**d1, **d2, **extra_dict}
    print(d3)


def method3():
    # only on python 3.9+
    # combine dictionary using "|"
    d1 = {"a": 1, "b": 2, "c": 3}
    d2 = {"d": 4, "e": 5}
    extra_dict = {"f": 6, "g": 7}

    d3 = d1 | d2 | extra_dict
    print(d3)


if __name__ == "__main__":
    method1()
    method2()
    method3()
