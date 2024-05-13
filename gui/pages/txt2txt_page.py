import tkinter as tk

from .ai_type import BaseAIType
from .txt2txt import BaseTxt2Txt
from .falcon import Falcon


class Txt2TxtPage(BaseAIType, BaseTxt2Txt):
    name = 'Text to Text'
    ai_dict = {
        'Falcon': Falcon
    }
    model_dict = {
        'falcon7B': '/path/to/Falcon7B',
        'model2-TBD': '/model/2/to/be/determined'
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
