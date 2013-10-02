import tkinter as tk

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        button = tk.Button(text="Press me!", command=self.on_button)
        button.pack()
    def on_button(self):
        tk.messagebox.showinfo(message="Good-bye!")
        self.destroy()

app = SampleApp()
app.mainloop()
