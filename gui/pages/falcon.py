import tkinter as tk

from .page import BasePage


class Falcon(BasePage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print('using Falcon')