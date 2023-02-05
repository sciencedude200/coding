from tkinter import *
from random import randint
def bAaction():
    print((randint(1,6)))
window = Tk()
buttonA = Button(window, text='roll the die for a numder 1 to 6', command=bAaction)
buttonA.pack()