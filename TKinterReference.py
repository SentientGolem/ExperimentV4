from tkinter import *
from tkinter import ttk

class ReferenceApp:

    def __init__(self, master):

        self.label = ttk.Label(master, text = "This will be a reference page!")
        self.label.grid(row = 0, column = 0, columnspan = 2)

        self.labelRefer = ttk.Label(master, text = "", wraplength = 200, justify = CENTER)
        self.labelRefer.config(foreground = 'cyan', background = 'purple')
        self.labelRefer.grid(row = 1, column = 0, columnspan = 2)

        self.image = PhotoImage(file = ".\\chrome.png")

        ttk.Button(master, text = "Button", command = self.refer_button).grid(row = 2, column = 0)

        ttk.Button(master, text = "Label", command = self.refer_label).grid(row = 2, column = 1)

        ttk.Button(master, text = "Picture", command = self.refer_picture).grid(row = 3, column = 0)

    def refer_button(self):
        self.labelRefer.config(text = "A button is a clicky thing that does stuff when clicked!", image = "")

    def refer_label(self):
        self.labelRefer.config(text = "A label is something that just shows text.", image = "")

    def refer_picture(self):
        self.labelRefer.config(image = self.image, text = "LOOKIT THIS BUTTON", compound = "center")

def main():

    root = Tk()
    app = ReferenceApp(root)
    root.mainloop()

if __name__ == "__main__": main()
