from tkinter import Tk
from controler import *

root_tk = Tk()
application = controller(root_tk)
print(dir(application))
print(application.__class__)
print("-------------Información sobre la clase--------------")
print(application.__doc__)
print("--------Información sobre el método visionActivada()-------")
print(application.visionActivada.__doc__)
root_tk.mainloop()
