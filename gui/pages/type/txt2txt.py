from ..generics.ai_model import BaseAIModelPage
from .inputs.text_input import BaseTextInput


class BaseTxt2Txt(BaseAIModelPage, BaseTextInput):
    type = 'txt2txt'

    def generate(self):
        print('Model : {}'.format(self.current_model_path))
        super().generate()
        print('Should generate a Text\n')

        response = self.post_ai_generation()
        if response is not None:
            print(response)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
