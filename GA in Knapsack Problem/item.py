import random
from collections import namedtuple

Item = namedtuple("Item", ["name", "value", "weight"])


def generate_items(
    n: int,
    mn_value: int = 0,
    mx_value: int = 10,
    mn_weight: int = 100,
    mx_weight: int = 2000,
):
    items = []
    for i in range(n):
        name = "Item {}".format(i)
        value = random.randint(mn_value, mx_value)
        weight = random.randint(mn_weight, mx_weight)
        items.append(Item(name, value, weight))
    return items
