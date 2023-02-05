from tkinter import *
from tkinter import ttk

#setup window
window = Tk()
window.title("guber art")
window.geometry("700x500")


def hello():
    print("debug")

title = Label(window, text="guber art", font=("bold", 30))
title.pack()
c = Canvas(window, width=330, height=200)
c.place(x=250, y=350)
btn = Button(window, text='make art', width=40,
             height=5, bd='10', command=hello)
  
btn.place(x=65, y=100)
  
window.mainloop()

