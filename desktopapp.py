#Current doller value in India is 81.63 on 01-10-2022
from tkinter import *

window =Tk()

def conversion():
    indianrupee = (float(dollers.get())*81.64)
    t1.insert(END, indianrupee)

b1 = Button(window, text="Convert",command=conversion)
b1.grid(row=4, column=1)

dollers=StringVar()
e1 = Entry(window, textvariable=dollers)
e1.grid(row=0, column=1)

t1 = Text(window, height=5, width=15)
t1.grid(row=0, column=2)

window.mainloop()