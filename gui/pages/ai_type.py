import tkinter as tk

from .page import BasePage


class BaseAIType(BasePage):
    name = ''
    model_list = []
    ai_dict = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Version pack
        # for ai_name, ai_class in self.ai_dict.items():
        #     ai = ai_class(self)
        #     buttonframe = tk.Frame(self)
        #     container = tk.Frame(self)
        #     buttonframe.pack(side="top", fill="x", expand=False)
        #     container.pack(side="top", fill="both", expand=True)
        #     ai.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        #     tk.Button(buttonframe, text=ai_name, command=ai.lift).pack()

        # Version grid
        i = 0
        for ai_name, ai_class in self.ai_dict.items():
            ai = ai_class(self)
            # buttonframe = tk.Frame(self)
            # container = tk.Frame(self)
            # buttonframe.pack(side="top", fill="x", expand=False)
            # container.pack(side="top", fill="both", expand=True)
            # ai.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
            btn = tk.Button(self, text=ai_name, command=ai.lift)
            btn.grid(row=0, column=i)
            i += 1
