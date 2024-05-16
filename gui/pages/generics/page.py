from tkinter import Frame


class BasePage(Frame):
    """
    Base class for displaying a Frame in Tkinter GUI.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def show(self):
        """
        Display the current page.

        @return: void
        """
        self.lift()
