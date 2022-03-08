# Simple Progress Bar

This is a very simple progress bar for terminal / console.

So here we have a function `progress_bar` with has 4 parameters.

| Parameter  | Expected Argument | Description                                                  |
| ---------- | ----------------- | ------------------------------------------------------------ |
| t_i        | int               | Total iteration                                              |
| c_i        | int               | Current iteration                                            |
| bar_length | int               | The number of characters in the progress bar.                |
| fill       | str               | The character to represent the progress in the progress bar. |

Here we calculate the percentage of our progress:

```python
percent = f"{100 * c_i / float(t_i):.1f}"
```

Then we calculate the length of the progress bar that need to be fill relative to the current percentage of progress.

```python
bar = fill * fill_length + "-" * (bar_length - fill_length)
```

After that we write it into terminal.

```python
print(f"\rProgress: |{bar}| {percent}%", end="")
```

When we print the progress bar into termial, make sure that we give empty string ("") to parameter `end` in our print funcion so that it would not print a new line. We also need to make sure that at the beggining of our progress bar, we put `\r`.

`\r` is an escape character that bring the cursor to its location. In this case, in the next iteration, we overwrite the previous progress bar because we bring the cursor to the begging of print statement and write a new progress bar on it.

The print statement above can only work in python 3.6 and above since it use `f-string`. To make it work in python 3.5 and below, just change that statement to:

```python
print("\rProgress: |{}| {:.1f}%".format(bar, percent), end="")
```

And don't forget to rewrite the `percent` if you are using pyhton 3.5 and below:

```python
percent = 100 * c_i / float(t_i)
```
