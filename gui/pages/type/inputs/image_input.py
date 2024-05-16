import tkinter as tk
from tkinter.filedialog import askopenfilename


class BaseImageInput(tk.Frame):
    """
    Base class to display the list of information used for AI images.
    """
    def generate(self):
        """
        Generate the list of information.

        @return: void
        """
        print('Path to file : {}\n'
              'Description : {}\n'.format(self.filepath, self.description.get()))

    def get_image(self, row):
        """
        Opens a selection widget for an image.

        @param row: row line number
        @return: void
        """
        self.filepath = askopenfilename(title='Open an image', filetypes=[('png files', '.png'), ('all files', '.*')])
        photo = tk.PhotoImage(file=self.filepath)
        canvas = tk.Canvas(self, width=200, height=200)
        canvas.create_image(0, 0, anchor='nw', image=photo)
        canvas.grid(column=1, row=row)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.filepath = ''
        row = 3

        # Displays the different inputs
        container = tk.Frame(self)
        # Nb column = weight + 1
        container.columnconfigure(0, weight=1)
        # Nb row = weight + 1
        container.rowconfigure(0, weight=3)

        label = tk.Label(self, text="Image")
        label.grid(column=0, row=row)
        open_img_btn = tk.Button(self, text='Open an image', command=lambda: self.get_image(row))
        open_img_btn.grid(column=1, row=row)
        row += 2

        label = tk.Label(self, text="Description")
        label.grid(column=0, row=row)
        string_var = tk.StringVar()
        self.description = tk.Entry(self, textvariable=string_var, width=120)
        self.description.grid(column=1, row=row, pady=50)
        row += 1

        generate_btn = tk.Button(self, text='Generate', command=self.generate)
        generate_btn.grid(column=0, row=row, pady=20)
