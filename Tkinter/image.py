#adding image using tkinter
from tkinter import *

from PIL import Image, ImageTk

root = Tk()

root.title("Image Display")

root.geometry("500x500")

upload = Image.open("mecc.jpg")

img = ImageTk.PhotoImage(upload)

label = Label(root, image=img, height=360, width=300)

label.place(x=50, y=0)

label2 = Label(root, text="this is how we add an image!")

label2.place(x=40, y=360)

root.mainloop()