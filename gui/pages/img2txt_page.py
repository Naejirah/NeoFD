from .type.img2txt import BaseImg2Txt


class Img2TxtPage(BaseImg2Txt):
    name = 'Image to Text'

    ai_info = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
