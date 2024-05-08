from tkinter import Frame


class BasePage(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def show(self, widgets=None):
        self.lift()
        # for widget in widgets:
        #     widget.pack_forget()
