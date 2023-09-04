import time
from tkinter import *
from tkinter import filedialog
from pygame import mixer
import os

root = Tk()
root.title("Reese Player")
root.geometry("300x350+290+10")
root.configure(background="#333333")
root.resizable(False, False)

lower_frame = Frame(root,bg="ffffff", width=485, height=180)
lower_frame.place(x=0, y=400)

root.mainloop()
