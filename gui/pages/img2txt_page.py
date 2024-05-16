from .img2txt import BaseImg2Txt
from .blip import Blip
# from .stablediffusion import StableDiffusion


class Img2TxtPage(BaseImg2Txt):
    name = 'Image to Text'

    ai_info = {
        'blip': {
            'class': Blip,
            'models': {
                'model-TBD': '/model/1/to/be/determined',
                'model2-TBD': '/model/2/to/be/determined'
            }
        },
        # 'stable-diffusion': {
        #     'class': StableDiffusion,
        #     'models': {
        #         'v2-1_768-ema-pruned': '/path/to/model/v2-1_768-ema',
        #         'ema-pruned-next-generation': '/path/to/next/generation'
        #     }
        # }
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
