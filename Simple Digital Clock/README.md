# Simple Digital Clock

Here we going to create a simple digital clock using tkinter.
It is very simple and there no need to install any extra library or module since tkinter is part of base python.

Below is screenshot of what we going to make:

![Simple Digital Clock](Screenshot%201.jpg)

## 1.0 Creating the main application

We will first create the main application window.

```python
import tkinter as tk
win = tk.Tk()
```

Then we set the title for our application using `title()` method.

```python
win.title("Simple Digital Clock")
```

## 2.0 Add label for our time display

Since the application only purpose is to display the current time, we only need to have 1 label.

```python
lbl = tk.Label(
    win,
    font=("Segoe Print", 50, "bold"),
    bg="#FC2E20",
    fg="#010100",
    pady=15,
    padx=50,
)
lbl.pack(anchor="center")
```

As you can see from code snippet above, we create a `Label` and we set it so it is attach to our `win`.

Noted that here, we don't add `text` for our label yet.

All of the keyword arguments given to our label (font, bg, fg, pady, padx) are optional in order to give it a better look.

To know what font is available for you, hit the windows key, then type `Font Settings`. There you can browse what font is currently available for you.

Don't forget to `pack()` the label.

## 3.0 Update the time display

First, create a function that will be responsible to update our time display. We name it `tick`.

Now, we going to get the current time from our device using time module.

We format it to 12H format.

```python
    import time
    def tick():
        lbl.config(text=time.strftime("%I:%M:%S %p"))
```

You can format our time display using the code below:

| Code | Description     |
| ---- | --------------- |
| %I   | 12 Hours        |
| %H   | 24 Hours        |
| %M   | Minutes (00-59) |
| %S   | Seconds (00-59) |
| %p   | PM / AM         |

We then tell our application to call our `tick` function after 1 second as bellow:

```python
    win.after(1000, tick)
```

By putting the code above inside our `tick` funtion, we effectively create a loop where the `tick` function will be call every 1 second.

Our `tick` function should be looking as shown bellow:

```python
    def tick():
        lbl.config(text=time.strftime("%I:%M:%S %p"))
        win.after(1000, tick)
```

## 4.0 Final Step

Finally, we need to call our `tick` funtion once.
Then make sure to call `mainloop` method on our main window so it will not immedietly terminated when you run the code.

So your final code should be as shown bellow:

```python
import time
import tkinter as tk


def main():
    win = tk.Tk()
    win.title("Simple Digital Clock")

    lbl = tk.Label(
        win,
        font=("Segoe Print", 50, "bold"),
        bg="#FC2E20",
        fg="#010100",
        pady=15,
        padx=50,
    )
    lbl.pack(anchor="center")

    def tick():
        lbl.config(text=time.strftime("%I:%M:%S %p"))
        win.after(1000, tick)

    tick()
    win.mainloop()


if __name__ == "__main__":
    main()
```
