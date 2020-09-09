from tkinter import *

root = Tk()


root.title("window")
root.geometry('200x200')
Button(root,text ='click',bg = 'yellow',command = root.destroy).pack(padx = 10)


mainloop()