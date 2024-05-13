import tkinter as tk

from .ai_type import BaseAIType
from .stablediffusion import StableDiffusion
from .txt2img import BaseTxt2Img


class Txt2ImgPage(BaseAIType, BaseTxt2Img):
    name = 'Text to Image'
    ai_dict = {
        'StableDiffusion': StableDiffusion
    }
    model_dict = {
        'v2-1_768-ema-pruned': '/path/to/model/v2-1_768-ema',
        'ema-pruned-next-generation': '/path/to/next/generation'
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
