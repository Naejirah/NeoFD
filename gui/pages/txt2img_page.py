from .stablediffusion import StableDiffusion
from .txt2img import BaseTxt2Img


class Txt2ImgPage(BaseTxt2Img):
    name = 'Text to Image'
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
