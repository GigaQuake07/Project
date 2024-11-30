import tkinter as tk
from Functions import *
root=tk.Tk()
root.title('Substitution Management App')
b1=tk.Button(root, text='Take attendance', command=attendance())
b2=tk.Button(root, text='Give substitution', command=subs())
b1.pack()
b2.pack()
root.mainloop()