import tkinter as tk

from .generic_ai_type import PageGenericAiType
from .generic import PageGeneric


class Blip(PageGeneric):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        label = tk.Label(self, text="I'm at Falcon")
        label.pack(side="top", fill="both", expand=True)


class Img2Txt(PageGenericAiType):
    name = 'Image to Text'
    ai_list = ['Blip']
    ai_dict = {
        'Blip': Blip
    }
