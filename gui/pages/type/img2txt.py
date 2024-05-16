from ..generics.ai_model import BaseAIModelPage
from .inputs.image_input import BaseImageInput


class BaseImg2Txt(BaseAIModelPage, BaseImageInput):
    """
    Base class for handling Image to Text AI.
    """
    name = 'Image to Text'
    type = 'img2txt'
    ai_info = {}

    def generate(self):
        """
        Generate the list of information and does a POST request to generate an output.

        @return: void
        """
        print('Model : {}\n'.format(self.current_model_path))
        super().generate()
        print('Should generate a Text\n')

        response = self.post_ai_generation()
        if response is not None:
            print(response)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
