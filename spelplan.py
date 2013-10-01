from tkinter import *
root=Tk()
knappar = []
bokstav = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
for i in range(10):
    li = []
    for j in range(10):
        li.append(j)
    knappar.append(li)


for k in range(10):
    Label(text=bokstav[k]).grid(column=k+1, row=0)
for r in range(1,11):
    Label(text=r).grid(column=0, row=r)

for i in range(1,11):
    for j in range(1,11):
        b=Button(root)
        photo=PhotoImage(file="smiley.gif")
        b.config(image=photo,width="20",height="20")
        b.grid(column=j, row=i, sticky=W)
Label(text="Det här är spelplanen!").grid(column=1, columnspan=10)
Label(text="Skjut på ruta").grid(row=13,column=2, columnspan=3)
Entry(root).grid(row=13, column=5, columnspan=5)

root.mainloop()
