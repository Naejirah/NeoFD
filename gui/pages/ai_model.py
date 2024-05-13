import tkinter as tk
from functools import partial


class BaseAIModelPage(tk.Frame):
    model_dict = {}

    def get_model_path(self, path):
        self.current_model_path = path

    # @staticmethod
    # def on_click(e):
    #     print(str(e.widget).split(".")[-1])
    #     e.widget['background'] = 'red'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.current_model_path = ''
        self.row = 1
        i = 0

        # self.current_model_path_radiobutton = tk.StringVar()
        for model_name, model_path in self.model_dict.items():
            # Button
            btn = tk.Button(self, name=model_name, text='Run with ' + model_name, command=partial(self.get_model_path, model_path))

            # Radiobutton
            # btn = tk.Radiobutton(self, text=model_name, variable=self.current_model_path_radiobutton, value=model_path)
            # btn.bind("<Button-1>", self.on_click)
            btn.grid(column=i, row=self.row)
            i += 1

        self.row += 1
