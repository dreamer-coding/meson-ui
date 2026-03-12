#
# ==============================================================================
# Author: Michael Gene Brockus (Dreamer)
# Email: michaelbrockus@gmail.com
# Organization: Fossil Logic
# Description:
#     This file is part of the Fossil Logic project, where innovation meets
#     excellence in software development. Michael Gene Brockus, also known as
#     "Dreamer," is a dedicated contributor to this project. For any inquiries,
#     feel free to contact Michael at michaelbrockus@gmail.com.
# ==============================================================================
#
from tkinter import ttk
import tkinter as tk
import configparser
import os


class AppInfo:
    def __init__(self):
        self.name = "Meson Build GUI"
        self.version = "0.1.0"
        self.author = "Michael Gene Brockus (Dreamer)"
        self.email = "michaelbrockus@gmail.com"
        
    def get_info(self):
        return f"{self.name} v{self.version} by {self.author} ({self.email})"


class AppThemes:
    def __init__(self, root):
        self.root = root
        self.root.title("App Themes")
        self.root.geometry("300x200")
        self.root.resizable(False, False)

        self.create_widgets()

    def create_widgets(self):
        self.theme_var = tk.StringVar()
        self.theme_var.set("light")

        self.light_theme_radio = ttk.Radiobutton(
            self.root,
            text="Light",
            variable=self.theme_var,
            value="light",
            command=self.set_theme,
        )
        self.dark_theme_radio = ttk.Radiobutton(
            self.root,
            text="Dark",
            variable=self.theme_var,
            value="dark",
            command=self.set_theme,
        )
        self.meson_theme_radio = ttk.Radiobutton(
            self.root,
            text="Meson",
            variable=self.theme_var,
            value="meson",
            command=self.set_theme,
        )

        self.light_theme_radio.pack(pady=10)
        self.dark_theme_radio.pack(pady=10)
        self.meson_theme_radio.pack(pady=10)

    def set_theme(self):
        theme = self.theme_var.get()
        self.root.event_generate("<<ThemeChanged>>", when="tail", theme=theme)
        self.root.destroy()
