from tkinter import *

class Temas:
    def tema_amarillo(self, root):
        self.root = root
        self.tema_1 = "yellow"
        self.root.configure(background=self.tema_1)
        return self.root

    def tema_blanco(self, root):
        self.root = root
        self.tema_2 = "white"
        self.root.configure(background=self.tema_2)
        return self.root

    def tema_rojo(self, root):
        self.root = root
        self.tema_3 = "red"
        self.root.configure(background=self.tema_3)
        return self.root
