import tkinter as tk


class BaseTextInput(tk.Frame):
    def generate(self):
        print('Entry : {}\n'
              'Width : {}\n'
              'Height : {}\n'
              'CFG Scale : {}\n'
              'Seed : {}\n'.format(self.entry.get(), self.width.get(), self.height.get(), self.cfg_scale.get(),
                                   self.seed.get()))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        row = 2

        container = tk.Frame(self)
        # Nb column = weight + 1
        container.columnconfigure(0, weight=1)
        # Nb row = weight + 1
        container.rowconfigure(0, weight=3)

        label = tk.Label(self, text="Text")
        label.grid(column=0, row=row)
        string_var = tk.StringVar()
        self.entry = tk.Entry(self, textvariable=string_var, width=120)
        self.entry.grid(column=1, row=row, pady=50)
        row += 1

        label = tk.Label(self, text="Width")
        label.grid(column=0, row=row)
        self.width = tk.Spinbox(self, from_=1, to=1920)
        self.width.grid(column=1, row=row)
        row += 1

        label = tk.Label(self, text="Height")
        label.grid(column=0, row=row)
        self.height = tk.Spinbox(self, from_=1, to=1920)
        self.height.grid(column=1, row=row)
        row += 1

        label = tk.Label(self, text="CFG Scale")
        label.grid(column=0, row=row)
        self.cfg_scale = tk.Spinbox(self, from_=0, to=20)
        self.cfg_scale.grid(column=1, row=row)
        row += 1

        label = tk.Label(self, text="Seed")
        label.grid(column=0, row=row)
        int_var = tk.IntVar(value=-1)
        self.seed = tk.Entry(self, textvariable=int_var, width=60)
        self.seed.grid(column=1, row=row)
        row += 1

        generate_btn = tk.Button(self, text='Generate', command=self.generate)
        generate_btn.grid(column=0, row=row, pady=20)
