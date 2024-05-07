import tkinter as tk

from pages.txt2img import Txt2Img
from pages.img2img import Img2Img
from pages.txt2txt import Txt2Txt
from pages.img2txt import Img2Txt

RESOLUTION = '1440x810'


class App(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        txt2img = Txt2Img(self)
        img2img = Img2Img(self)
        txt2txt = Txt2Txt(self)
        img2txt = Img2Txt(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        txt2img.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        img2img.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        txt2txt.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        img2txt.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        btn_txt2img = tk.Button(buttonframe, text="txt2img", command=txt2img.show)
        btn_img2img = tk.Button(buttonframe, text="img2img", command=img2img.show)
        btn_txt2txt = tk.Button(buttonframe, text="txt2txt", command=txt2txt.show)
        btn_img2txt = tk.Button(buttonframe, text="img2txt", command=img2txt.show)

        btn_txt2img.pack(side="left")
        btn_img2img.pack(side="left")
        btn_txt2txt.pack(side="left")
        btn_img2txt.pack(side="left")

        txt2img.show()


if __name__ == "__main__":
    root = tk.Tk()
    main = App(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry(RESOLUTION)
    root.mainloop()
