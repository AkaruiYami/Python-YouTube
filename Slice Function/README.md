There is a built-in function in python call `slice()`.

This function can be use to create a slice object. Let see the example of when to use this. Let say we have slicing operation on certain iterable and this operation is conducted many times as below:

```python

list1 = ["apple", "orange", "watermelon", "sadmelon"]

print(list1[:-1])
pretty_print(list1[:-1])
super_pretty_print(list1[:-1])
```

In the example above, we have a code that compare the different between print function where `pretty_print` and `super_pretty_print` is a custom function defined by user. We want the value printed by those functions remain the same, so the slicing must be the same between those 3. In this case, if we change slicing value for `print`, the changes must be done to all other function which is very repeatitive. So, we want to use a single variable that hold this slicing value.

Using `slice()` function, we can achieve this goal. Change our code to:

```python

list1 = ["apple", "orange", "watermelon", "sadmelon"]
my_slice = slice(None, -1)

print(list1[my_slice])
pretty_print(list1[my_slice])
super_pretty_print(list1[my_slice])
```

