import tkinter as tk

from .ai_model import BaseAIModelPage
from .image_input import BaseImageInput


class BaseImg2Img(BaseAIModelPage, BaseImageInput):
    type = 'img2img'

    def generate(self):
        print('Model : {}\n'.format(self.current_model_path))
        # print('Model path with radiobutton : ' + self.current_model_path_radiobutton.get())
        super().generate()
        print('Should generate an Image\n')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
