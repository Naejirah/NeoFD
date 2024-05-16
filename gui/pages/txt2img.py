import tkinter as tk

from .ai_model import BaseAIModelPage
from .text_input import BaseTextInput


class BaseTxt2Img(BaseAIModelPage, BaseTextInput):
    type = 'txt2img'

    def generate(self):
        print('Model : {}'.format(self.current_model_path))
        super().generate()
        print('Should generate an Image\n')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
