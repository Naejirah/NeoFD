from ..generics.page import BasePage


class BaseAI(BasePage):
    """
    Base class for using an AI.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print('using an AI')
