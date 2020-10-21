from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Milan')
root.geometry("width=500, height=500")

my_notebook = ttk.Notebook(root)
my_notebook.pack(pady=15)

my_frame1 = Frame(my_notebook, width=500, height=500, bg="blue")
my_frame2 = Frame(my_notebook, width=500, height=500, bg="red")

my_frame1.pack(fill="both", expand=1)
my_frame2.pack(fill="both", expand=1)

mynotebook.add()

root.mainloop()