import tkinter as tk
from tkinter import *
from tkinter import ttk
import playsound as p

def playsound1(event):
    print(event)
    p.playsound("lobotomy.mp3", block=False)

def playsound2(event):
    print(event)
    p.playsound("SEEYUH.mp3", block=False)

def playsound3(event):
    print(event)
    p.playsound("imevil.mp3", block=False)

def playsound4(event):
    print(event)
    p.playsound("swampizzo.mp3", block=False)

win = tk.Tk()
win.attributes('-topmost',True)
win.geometry("500x100")

lobotomy = PhotoImage(file="lobotomypng.png")
carti = PhotoImage(file="carti.png")
ye = PhotoImage(file="ye.png")
swampizzo = PhotoImage(file="swampizzo.png")

b1 =  tk.Button(win, image=lobotomy)
b1.bind("<Button>",playsound1)
b2 =  tk.Button(win, image=carti)
b2.bind("<Button>",playsound2)
b3 =  tk.Button(win, image=ye)
b3.bind("<Button>",playsound3)
b4 =  tk.Button(win, image=swampizzo)
b4.bind("<Button>",playsound4)

b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)
b4.grid(row=0, column=3)

win.mainloop()