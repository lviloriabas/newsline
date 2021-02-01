import tkinter as tk
import webbrowser
from functools import partial
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup


news_limit = 5


def callback(a_url):
    webbrowser.open_new(a_url)


def get_news(url, frame):
    url_root = "https://news.google.com"

    source = requests.get(url).text
    soup = BeautifulSoup(source, "lxml")
    articles = soup.find_all("a", class_="DY5T1d RZIKme", limit=news_limit)

    for widget in frame.winfo_children():
        widget.destroy()

    for article in articles:
        article_url = urljoin(url_root, article.get("href"))

        title_label = tk.Label(
            frame, text=article.string, bg="#252525", fg="white"
            )
        title_label.grid(column=0, sticky="w")

        url_label = tk.Button(
            frame,
            text="Go to article",
            bg="#252525",
            activebackground="#252525",
            activeforeground="white",
            fg="#80ffdb",
            font=("OpenSans", 10, "underline"),
            justify="left",
            borderwidth=0,
            command=partial(callback, article_url),
        )
        url_label.grid(column=0)
