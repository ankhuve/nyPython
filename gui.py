from tkinter import *

# Skapa fönster
root = Tk()

# Modifiera root-fönster
root.title("GUI")
root.geometry("800x600")

app = Frame(root)
app.grid()

button1 = Button(app, text = "This is a button")
button1.grid()

button2 = Button(app)
button2.grid()
button2.configure(text = "This will show text")

button3 = Button(app)
button3.grid()
button3["text"] = "This will also show text"

# Starta event-loop
root.mainloop()

