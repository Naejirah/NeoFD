from .ai_model import BaseAIModelPage
from .image_input import BaseImageInput


class BaseImg2Txt(BaseAIModelPage, BaseImageInput):
    type = 'img2txt'

    def generate(self):
        print('Model : {}\n'.format(self.current_model_path))
        super().generate()
        print('Should generate a Text\n')

        response = self.post_ai_generation()
        if response is not None:
            print(response)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
