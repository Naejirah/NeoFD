import tkinter as tk

from .generic_ai_type import PageGenericAiType
from .stablediffusion import StableDiffusion


class Txt2Img(PageGenericAiType):
    name = 'Text to Image'
    ai_list = ['StableDiffusion']
    ai_dict = {
        'StableDiffusion': StableDiffusion
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
