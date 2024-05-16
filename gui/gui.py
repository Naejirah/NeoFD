import tkinter as tk
from functools import partial
import requests

from pages.txt2img_page import Txt2ImgPage
from pages.img2img_page import Img2ImgPage
from pages.txt2txt_page import Txt2TxtPage
from pages.img2txt_page import Img2TxtPage

from pages.generics.api_page import BaseAPIPage

RESOLUTION = '1440x810'


class App(BaseAPIPage):
    TYPE_AVAILABLE = {
        'txt2img': Txt2ImgPage,
        'img2img': Img2ImgPage,
        'txt2txt': Txt2TxtPage,
        'img2txt': Img2TxtPage,
    }

    def get_api_url(self):
        return super().get_api_url() + 'categorie'

    def get_categories(self):
        url = self.get_api_url()
        response = self.call_api(requests.get(url, headers={}))
        if response is not None:
            categories = [category['output'] for category in response]
            return categories
        return response

    def view_category(self, name):
        if name in self.TYPE_AVAILABLE:
            page = self.TYPE_AVAILABLE[name](self)
            page.place(in_=self.container, x=0, y=0, relwidth=1, relheight=1)
            page.show()
        else:
            # TODO : Non supporté, créer la classe correspondant au name si besoin
            print(name, ' is unsupported, you need to create the necessary type to "TYPE_AVAILABLE"')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        buttonframe = tk.Frame(self)
        self.container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        self.container.pack(side="top", fill="both", expand=True)

        category_list = self.get_categories()
        if category_list is not None:
            for category in category_list:
                new_btn = tk.Button(buttonframe, text=category + ' from API',
                                    command=partial(self.view_category, category))
                new_btn.pack(side='left')


if __name__ == "__main__":
    root = tk.Tk()
    main = App(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry(RESOLUTION)
    root.mainloop()
