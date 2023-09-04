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

lower_frame = Frame(root, bg="#FFFFFF", width=485, height=180)
lower_frame.place(x=0, y=400)

image_icon = PhotoImage = PhotoImage(file="D:\\100_days_python\\day22\\music_player\\music\\logo.png")
root.iconphoto(False, image_icon)
root.mainloop()

