import tkinter as tk

from pages.txt2img_page import Txt2ImgPage
from pages.img2img_page import Img2ImgPage
from pages.txt2txt_page import Txt2TxtPage
from pages.img2txt_page import Img2TxtPage

RESOLUTION = '1440x810'


class App(tk.Frame):
    def view_txt2img(self):
        txt2img = Txt2ImgPage(self)
        txt2img.place(in_=self.container, x=0, y=0, relwidth=1, relheight=1)
        txt2img.show()

    def view_img2img(self):
        img2img = Img2ImgPage(self)
        img2img.place(in_=self.container, x=0, y=0, relwidth=1, relheight=1)
        img2img.show()

    def view_txt2txt(self):
        txt2txt = Txt2TxtPage(self)
        txt2txt.place(in_=self.container, x=0, y=0, relwidth=1, relheight=1)
        txt2txt.show()

    def view_img2txt(self):
        img2txt = Img2TxtPage(self)
        img2txt.place(in_=self.container, x=0, y=0, relwidth=1, relheight=1)
        img2txt.show()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        buttonframe = tk.Frame(self)
        self.container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        self.container.pack(side="top", fill="both", expand=True)

        btn_txt2img = tk.Button(buttonframe, text="txt2img", command=self.view_txt2img)
        btn_img2img = tk.Button(buttonframe, text="img2img", command=self.view_img2img)
        btn_txt2txt = tk.Button(buttonframe, text="txt2txt", command=self.view_txt2txt)
        btn_img2txt = tk.Button(buttonframe, text="img2txt", command=self.view_img2txt)

        btn_txt2img.pack(side="left")
        btn_img2img.pack(side="left")
        btn_txt2txt.pack(side="left")
        btn_img2txt.pack(side="left")

        self.view_txt2img()


if __name__ == "__main__":
    root = tk.Tk()
    main = App(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry(RESOLUTION)
    root.mainloop()
