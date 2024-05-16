from ..generics.ai_model import BaseAIModelPage
from .inputs.image_input import BaseImageInput


class BaseImg2Img(BaseAIModelPage, BaseImageInput):
    type = 'img2img'

    def generate(self):
        print('Model : {}\n'.format(self.current_model_path))
        super().generate()
        print('Should generate an Image\n')

        response = self.post_ai_generation()
        if response is not None:
            print(response)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
