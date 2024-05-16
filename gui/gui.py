import tkinter as tk
from functools import partial
import requests

from pages.type.txt2img import BaseTxt2Img
from pages.type.img2img import BaseImg2Img
from pages.type.txt2txt import BaseTxt2Txt
from pages.type.img2txt import BaseImg2Txt

from pages.generics.api_page import BaseAPIPage

RESOLUTION = '1440x810'


class App(BaseAPIPage):
    """
    Main class for the GUI.
    """
    # Dictionary of all the currently available types of AI.
    # New types can be added if needed.
    TYPE_AVAILABLE = {
        'txt2img': BaseTxt2Img,
        'img2img': BaseImg2Img,
        'txt2txt': BaseTxt2Txt,
        'img2txt': BaseImg2Txt,
    }

    def get_api_url(self):
        """
        Method to get the API URL of all the available categories.


        @return: API url
        """
        return super().get_api_url() + 'categorie'

    def get_categories(self):
        """
        GET request to get all the available categories.

        @return:
        """
        url = self.get_api_url()
        response = self.call_api(requests.get(url, headers={}))
        if response is not None:
            categories = [category['output'] for category in response]
            return categories
        return response

    def view_category(self, name):
        """
        Method to display pages related to a specific category name.

        @param name: name of the category
        @return: void
        """
        if name in self.TYPE_AVAILABLE:
            page = self.TYPE_AVAILABLE[name](self)
            page.place(in_=self.container, x=0, y=0, relwidth=1, relheight=1)
            page.show()
        else:
            # TODO : Non supporté, créer la classe correspondant au name si besoin
            print(name, ' is unsupported, you need to create the necessary type to "TYPE_AVAILABLE"')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Displays the view of the GUI.
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


# Launches the Tkinter window
if __name__ == "__main__":
    root = tk.Tk()
    main = App(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry(RESOLUTION)
    root.mainloop()
