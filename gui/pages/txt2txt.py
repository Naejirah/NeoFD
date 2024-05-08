import tkinter as tk

from .ai_model import BaseAIModelPage
from .text_input import BaseTextInput


class BaseTxt2Txt(BaseAIModelPage, BaseTextInput):
    def generate(self):
        print('Model : {}'.format(self.current_model_path))
        # print('Model path with radiobutton : ' + self.current_model_path_radiobutton.get())
        super().generate()
        print('Should generate a Text\n')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
