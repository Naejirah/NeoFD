from .type.txt2txt import BaseTxt2Txt


class Txt2TxtPage(BaseTxt2Txt):
    name = 'Text to Text'
    ai_info = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
