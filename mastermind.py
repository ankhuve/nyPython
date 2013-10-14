from tkinter import *
import random

def choosecol(i, rcol, n):
    b = Button(root, bg=rcol)
    b.config(width="5", height="2")
    b.grid(column=n, row=1)
    n+=1

root = Tk()
colors = ["red", "yellow", "blue", "green", "brown", "orange"]
Grid.rowconfigure(root,0,weight=1)
Grid.columnconfigure(root,0,weight=1)
n = 0
for i in colors:
    rcol =random.choice(colors)
    b = Button(root, bg=i, command=lambda x=colors.index(i), rcol=rcol: choosecol(x, rcol, n))
    b.config(width="5", height="2")
    b.grid(column=colors.index(i), row=0)
root.mainloop()
