from .txt2img import BaseTxt2Img


class Txt2ImgPage(BaseTxt2Img):
    name = 'Text to Image'
    ai_info = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
