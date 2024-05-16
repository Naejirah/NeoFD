from .txt2txt import BaseTxt2Txt
from .falcon import Falcon


class Txt2TxtPage(BaseTxt2Txt):
    name = 'Text to Text'
    ai_info = {
        'falcon': {
            'class': Falcon,
            'models': {
                'falcon7B': '/path/to/Falcon7B',
                'model2-TBD': '/model/2/to/be/determined'
            }
        }
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
