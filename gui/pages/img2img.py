import tkinter as tk

from .generic_ai_type import PageGenericAiType
from .generic import PageGeneric


class StableDiffusion(PageGeneric):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        label = tk.Label(self, text="I'm at Stable Diffusion")
        label.pack(side="top", fill="both", expand=True)


class Img2Img(PageGenericAiType):
    name = 'Image to Image'
    ai_dict = {
        'StableDiffusion': StableDiffusion
    }
