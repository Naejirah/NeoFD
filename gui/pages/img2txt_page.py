import tkinter as tk

from .ai_type import BaseAIType
from .img2txt import BaseImg2Txt
from .blip import Blip


class Img2TxtPage(BaseAIType, BaseImg2Txt):
    name = 'Image to Text'
    ai_dict = {
        'Blip': Blip
    }
    model_dict = {
        'model-TBD': '/model/1/to/be/determined',
        'model2-TBD': '/model/2/to/be/determined'
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
