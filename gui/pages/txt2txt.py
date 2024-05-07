import tkinter as tk

from .generic_ai_type import PageGenericAiType
from .generic import PageGeneric


class Falcon(PageGeneric):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        label = tk.Label(self, text="I'm at Falcon")
        label.pack(side="top", fill="both", expand=True)


class Txt2Txt(PageGenericAiType):
    name = 'Text to Text'
    ai_dict = {
        'Falcon': Falcon
    }

    ai_list = ['Falcon']
    model_list = ['Falcon7B']
