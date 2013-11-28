from tkinter import *
root = Tk()
root.geometry("1000x500")
root.resizable(0,0)

frame=Frame(root, height=250, width=500, bg="red")
frame.grid(row=0,column=0,sticky=N+W)

frame2=Frame(root, height=250, width=500, bg="green")
frame2.grid(row=0,column=1,sticky=N+E)

frame3=Frame(root, height=250, width=500, bg="blue")
frame3.grid(row=1,column=1,sticky=S+E)

frame4=Frame(root, height=250, width=500, bg="black")
frame4.grid(row=1, column=0, sticky=N+S+E+W)

Button(frame, text="OK").grid(column=0, row=0, sticky=N+S+E+W)
