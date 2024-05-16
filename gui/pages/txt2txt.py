import tkinter as tk

from .ai_model import BaseAIModelPage
from .text_input import BaseTextInput


class BaseTxt2Txt(BaseAIModelPage, BaseTextInput):
    type = 'txt2txt'

    def generate(self):
        print('Model : {}'.format(self.current_model_path))
        super().generate()
        print('Should generate a Text\n')

        # TODO : mnt je fais un post et get je crois à l'API avec les donénes que j'ai
        # self.current_model_path, le texte, l'IA ...

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
