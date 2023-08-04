Imagine we have 2 list and we want to every element at the same index pair together. For example:

```python

lst1 = ['a', 'b', 'c']
lst2 = [1, 2, 3]

new_list = [('a', 1), ('b', 2), ('c', 3)]
```

To achive this, we can use built-in function `zip()`. This function will accept any number of iterable then pair those element together.

```python
lst1 = ['a', 'b', 'c']
lst2 = [1, 2, 3, 4, 5]
lst3 = ['x', 'y', 'z']

new_lst = list(zip(lst1, lst2, lst3)) # [('a', 1, 'x'), ('b', 2, 'y'), ('c', 3, 'z')]
```

`zip()` will return a zip object. Therefore, if we want to have a new list instead of zip object, we need to cast it into `list()` function as shown in example above. Please take note, `lst2` contains extra elements compare to other list but `zip()` function still able to paired those elements by discarding those extra elements.. In case we want to include all element, we can use `zip_longest()` function from  built-in `itertools` module.
