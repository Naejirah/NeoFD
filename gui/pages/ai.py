import tkinter as tk

from .page import BasePage


class BaseAI(BasePage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print('using an AI')
