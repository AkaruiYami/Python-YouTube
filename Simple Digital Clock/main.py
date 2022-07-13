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
        # lbl.config(text=time.strftime("%H:%M:%S")) # 24 hours format
        lbl.config(text=time.strftime("%I:%M:%S %p"))  # 12 hours format
        win.after(1000, tick)

    tick()
    win.mainloop()


if __name__ == "__main__":
    main()
