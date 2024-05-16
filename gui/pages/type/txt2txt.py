from ..ai.falcon import Falcon
from ..generics.ai_model import BaseAIModelPage
from .inputs.text_input import BaseTextInput


class BaseTxt2Txt(BaseAIModelPage, BaseTextInput):
    """
    Base class for handling Text to Text AI.
    """
    name = 'Text to Text'
    type = 'txt2txt'
    ai_info = {}

    def generate(self):
        """
        Generate the list of information and does a POST request to generate an output.

        @return: void
        """
        print('Model : {}'.format(self.current_model_path))
        super().generate()
        print('Should generate a Text\n')

        response = self.post_ai_generation()
        if response is not None:
            print(response)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
