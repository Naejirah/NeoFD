import tkinter as tk

from .ai_model import BaseAIModelPage
from .text_input import BaseTextInput, BaseInput
from .page import BasePage
from .txt2txt_page import Txt2TxtPage


class BaseOutput(tk.Frame):
    def generate_output(self):
        print('generate output  BaseOutput')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class BaseTextOutput(BaseAIModelPage, BaseTextInput):
# class BaseTextOutput(BaseOutput):
    def generate_output(self):
        print('Model : {}'.format(self.current_model_path))
        # print('Model path with radiobutton : ' + self.current_model_path_radiobutton.get())
        super().generate()
        # super().generate_output()
        print('Should generate a Text\n')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class BaseInput2Output(BaseInput, BaseOutput, tk.Frame):
    # def generate(self):
    #     print('Model : {}'.format(self.current_model_path))
    #     # print('Model path with radiobutton : ' + self.current_model_path_radiobutton.get())
    #     super().generate()
    #     print('Should generate a Text\n')

    def __init__(self, input_class, output_class, *args, **kwargs):

        print('initialine BaseInpyt2Output : ', input_class)

        self.name = 'Image to Image'
        # self.ai_dict = {
        #     'StableDiffusion': StableDiffusion
        # }

        self.model_dict = {
            'v2-1_768-ema-pruned': '/path/to/model/v2-1_768-ema',
            'ema-pruned-next-generation': '/path/to/next/generation'
        }

        if input_class is BaseTextInput and output_class is BaseTextOutput:
            # BaseTextInput(self)
            print('azeqsd')
            Txt2TxtPage(self)


        super().__init__(*args, **kwargs)
        print(input_class)
        # input_class(self)
        # output_class(self)

        # input_class.__init__(self, *args, **kwargs)
        # output_class.__init__(self, *args, **kwargs)
        # input_class(self)
        # output_class(self)
        # self.generate_input()
        # self.generate_output()
