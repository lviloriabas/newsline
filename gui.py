import tkinter as tk
from tkinter.constants import CENTER, LEFT, RIGHT

from PIL import Image, ImageTk

from functions import get_news


def callback_window(event):
    root.geometry(f"+{event.x_root}+{event.y_root}")


def show_screen(event):
    root.deiconify()
    root.overrideredirect(1)


def hide_screen():
    root.overrideredirect(0)
    root.iconify()


def screen_appear(event):
    root.overrideredirect(1)


# Main Window
root = tk.Tk()
root.title("Newsline")

root.option_add("*Font", ("OpenSans", 11))
root.configure(bg="#252525")
root.overrideredirect(1)


# Frames
title_bar = tk.Frame(root, bg="#252525", relief=tk.SUNKEN)
title_bar.pack(expand=1, fill="x")

title_bar.bind("<B1-Motion>", callback_window)
title_bar.bind("<Button-3>", show_screen)
title_bar.bind("<Map>", screen_appear)

selection_frame = tk.Frame(root, bg="#252525")
selection_frame.pack(side=LEFT, padx=10, pady=5)

news_frame = tk.Frame(root, bg="#252525")
news_frame.pack(side=RIGHT, padx=10, pady=5)


# Labels
icon_load = Image.open("images/python1.png")
icon_image = ImageTk.PhotoImage(icon_load)
label1 = tk.Label(title_bar, image=icon_image, bg="#252525")
label1.pack(side=LEFT)

label2 = tk.Label(
    title_bar,
    text="Newsline",
    bg="#252525",
    fg="white",
    font=("Open Sans", 11)
)
label2.pack(side=LEFT, anchor=CENTER)

options_label = tk.Label(
    selection_frame,
    text="Options",
    bg="#252525",
    fg="white",
    justify="left",
    font=("Open Sans", 11, "bold"),
)
options_label.grid(row=1, column=0, pady=5)


# Buttons
close_load = Image.open("images/close_button.png")
close_image = ImageTk.PhotoImage(close_load)
close_button = tk.Button(
    title_bar,
    image=close_image,
    bg="#252525",
    highlightbackground="#252525",
    borderwidth=0,
    activebackground="#252525",
    command=root.destroy,
)
close_button.pack(side=RIGHT)

minimize_load = Image.open("images/minimize_button.png")
minimize_image = ImageTk.PhotoImage(minimize_load)
minimize_button = tk.Button(
    title_bar,
    bg="#252525",
    image=minimize_image,
    highlightbackground="#252525",
    borderwidth=0,
    activebackground="#252525",
    command=hide_screen,
)
minimize_button.pack(side=RIGHT)

ok_load = Image.open("images/ok_button.png")
ok_image = ImageTk.PhotoImage(ok_load)
ok_button = tk.Button(
    selection_frame,
    image=ok_image,
    padx=20,
    bg="#252525",
    activebackground="#252525",
    borderwidth=0,
    command=lambda: get_news(selection_url.get(), news_frame),
)


top = "https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en"
us = (
    "https://news.google.com/topics"
    "/CAAqIggKIhxDQkFTRHdvSkwyMHZNRGxqTjNjd0VnSmxiaWdBUAE?hl=en-US&gl=US"
    "&ceid=US%3Aen"
)
world = (
    "https://news.google.com/topics"
    "/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtVnVHZ0pWVXlnQVAB?hl=en-US"
    "&gl=US&ceid=US%3Aen"
)
business = (
    "https://news.google.com/topics"
    "/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtVnVHZ0pWVXlnQVAB?hl=en"
    "-US&gl=US&ceid=US%3Aen"
)
technology = (
    "https://news.google.com/topics"
    "/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGRqTVhZU0FtVnVHZ0pWVXlnQVAB?hl"
    "=en-US&gl=US&ceid=US%3Aen"
)
entertainment = (
    "https://news.google.com/topics"
    "/CAAqJggKIiBDQkFTRWdvSUwyMHZNREpxYW5RU0FtVnVHZ0pWVXlnQVAB"
    "?hl=en-US&gl=US&ceid=US%3Aen"
)
sports = (
    "https://news.google.com/topics"
    "/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp1ZEdvU0FtVnVHZ0pWVXlnQVAB?hl=en-US"
    "&gl=US&ceid=US%3Aen"
)
science = (
    "https://news.google.com/topics"
    "/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp0Y1RjU0FtVnVHZ0pWVXlnQVAB?hl=en"
    "-US&gl=US&ceid=US%3Aen"
)
health = (
    "https://news.google.com/topics"
    "/CAAqIQgKIhtDQkFTRGdvSUwyMHZNR3QwTlRFU0FtVnVLQUFQAQ?hl=en-US&gl=US"
    "&ceid=US%3Aen"
)

selection_url = tk.StringVar(root)
selection_url.set(top)

selections = [
    ("Top stories", top),
    ("U.S.", us),
    ("World news (excluding U.S.)", world),
    ("Business", business),
    ("Technology", technology),
    ("Entertainment", entertainment),
    ("Sports", sports),
    ("Science", science),
    ("Health", health),
]


for text, selection in selections:
    tk.Radiobutton(
        selection_frame,
        text=text,
        variable=selection_url,
        value=selection,
        bg="#252525",
        fg="white",
        activebackground="#3b3b3b",
        activeforeground="white",
        selectcolor="#252525",
    ).grid(column=0, sticky="w")

ok_button.grid(row=11, column=0, pady=5)


tk.mainloop()
