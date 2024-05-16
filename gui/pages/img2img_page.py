import tkinter as tk

from .stablediffusion import StableDiffusion
from .img2img import BaseImg2Img


class Img2ImgPage(BaseImg2Img):
    name = 'Image to Image'
    ai_info = {
        'stable-diffusion': {
            'class': StableDiffusion,
            'models': {
                'v2-1_768-ema-pruned': '/path/to/model/v2-1_768-ema',
                'ema-pruned-next-generation': '/path/to/next/generation'
            }
        }
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
