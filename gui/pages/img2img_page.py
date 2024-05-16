from .img2img import BaseImg2Img


class Img2ImgPage(BaseImg2Img):
    name = 'Image to Image'
    ai_info = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
