import json
import tkinter as tk
from functools import partial
from tkinter.filedialog import askopenfilename, askdirectory

import requests

from .ai import BaseAI
from .api_page import BaseAPIPage
from .blip import Blip


class BaseAIModelPage(BaseAPIPage):
    name = ''
    ai_name = ''
    type = ''
    ai_info = {}

    def set_ai_and_model_path(self, ai_name, model_path):
        self.ai_name = ai_name
        self.current_model_path = model_path

    # def get_model_path(self, path):
    #     self.current_model_path = path

    def get_ai_api_url(self):
        return self.get_api_url() + 'ia/trouverParCategorie?Categorie={}'.format(self.type)

    def get_model_api_url(self):
        return self.get_api_url() + 'modele/'

    def post_model_api_url(self):
        return self.get_api_url() + 'modele/'

    def get_api_info(self):
        if not self.ai_info:
            self.get_ais()

    def get_path_to_model(self):
        return askopenfilename(title='Open a cktp file', filetypes=[('models', '.ckpt'), ('all files', '.')])

    def get_path_to_model_folder(self):
        return askdirectory(title='Open a folder')

    def get_models(self, ai_name):
        url = self.get_model_api_url() + ai_name
        response = self.call_api(requests.get(url, headers={}))
        if response is not None:
            models = [model['output'] for model in response]
            return models
        return response

    def get_ais(self):
        url = self.get_ai_api_url()
        response = self.call_api(requests.get(url, headers={}))
        if response is not None:
            ais = [ai['output'] for ai in response]
            for ai in ais:
                models = self.get_models(ai)
                if models is not None:
                    model_info = {}
                    for model in models:
                        name = model
                        path = ""
                        model_info.update({
                            name: path
                        })

                    self.ai_info.update({
                        ai: {
                            'class': BaseAI,
                            'models': model_info
                        }
                    })

    def add_model(self, ai_name, is_file):
        url = self.post_model_api_url() + ai_name
        data = {
            "chemin": self.get_path_to_model() if is_file else self.get_path_to_model_folder()
        }
        response = self.call_api(requests.post(url, json=data))
        if response is not None:
            self.set_ai_and_model_path(ai_name, data.get('chemin'))

    def view_ai(self, ai_name, ai):
        page = ai['class'](self)

        for btn in self.grid_slaves():
            if btn.grid_info()['row'] == 2:
                btn.grid_forget()

        i = 0
        models = self.get_models(ai_name)
        if models is not None:
            for model in models:
                name = model
                path = ""
                btn = tk.Button(self, name=(name.replace(".", "")), text='Run with ' + name,
                                command=partial(self.set_ai_and_model_path, ai_name, path))
                btn.grid(row=2, column=i)
                i += 1

        btn = tk.Button(self, name='new_model_ckpt', text='Add new model (ckpt)',
                        command=partial(self.add_model, ai_name, True))
        btn.grid(column=i, row=2)
        i += 1
        btn = tk.Button(self, name='new_model_torch', text='Add new model (torch)',
                        command=partial(self.add_model, ai_name, False))
        btn.grid(column=i, row=2)

        page.place(in_=self.ai_container, x=0, y=0, relwidth=1, relheight=1)
        page.show()

    def render_ai_info(self):
        buttonframe = tk.Frame(self)
        buttonframe.grid(row=1, column=0)
        self.ai_container = tk.Frame(self)

        i = 0
        for ai_name, ai in self.ai_info.items():
            btn = tk.Button(buttonframe, text=ai_name, command=partial(self.view_ai, ai_name, ai))
            btn.grid(row=2, column=i)
            i += 1

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ai_container = None
        self.current_model_path = ''
        self.row = 1

        self.get_api_info()
        self.render_ai_info()
