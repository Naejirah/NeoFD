import tkinter as tk

from .generic import PageGeneric


class PageGenericAiType(PageGeneric):
    name = ''
    ai_list = []
    model_list = []
    ai_dict = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for ai_name, ai_class in self.ai_dict.items():
            ai = ai_class(self)
            buttonframe = tk.Frame(self)
            container = tk.Frame(self)
            buttonframe.pack(side="top", fill="x", expand=False)
            container.pack(side="top", fill="both", expand=True)
            ai.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
            tk.Button(buttonframe, text='Go to '+ai_name, command=ai.lift).pack()
