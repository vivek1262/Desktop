import tkinter as tk
import tkinter.ttk as ttk

win = tk.Tk()

win.title("calculator_app")
win.geometry('250x230')

expr = ' '                                                                                                  
text = tk.StringVar()
def press(num):
    global expr
    expr += str(num)
    text.set(expr)

def clr():
    global expr
    expr = ''
    text.set(expr)
def equal():
    global expr
    ttl = str(eval(expr))
    text.set(ttl)

entry = ttk.Entry(win,justify = 'right',textvariable = text)
entry.grid(row=0,columnspan=4,sticky='nsew')


btn_7 = ttk.Button(win,text = 7,command = lambda:press(7))
btn_7.grid(row=1,column=0)
btn_8 = ttk.Button(win,text = 8,command = lambda:press(8))
btn_8.grid(row=1,column=1)
btn_9 = ttk.Button(win,text = 9,command = lambda:press(9))
btn_9.grid(row=1,column=2)
btn_d = ttk.Button(win,text = '/',command = lambda:press('/'))
btn_d.grid(row=1,column=3)

btn_4 = ttk.Button(win,text = 4,command = lambda:press(4))
btn_4.grid(row=2,column=0)
btn_5 = ttk.Button(win,text = 5,command = lambda:press(5))
btn_5.grid(row=2,column=1)
btn_6 = ttk.Button(win,text = 6,command = lambda:press(6))
btn_6.grid(row=2,column=2)
btn_m = ttk.Button(win,text = '*',command = lambda:press('*'))
btn_m.grid(row=2,column=3)

btn_1 = ttk.Button(win,text = 1,command = lambda:press(1))
btn_1.grid(row=3,column=0)
btn_2 = ttk.Button(win,text = 2,command = lambda:press(2))
btn_2.grid(row=3,column=1)
btn_3 = ttk.Button(win,text = 3,command = lambda:press(3))
btn_3.grid(row=3,column=2)
btn_s = ttk.Button(win,text = '-',command = lambda:press('-'))
btn_s.grid(row=3,column=3)

btn_0 = ttk.Button(win,text = 0,command = lambda:press(0))
btn_0.grid(row=4,column=0)
btn_D = ttk.Button(win,text = '.',command = lambda:press('.'))
btn_D.grid(row=4,column=1)
btn_P= ttk.Button(win,text = '%',command = lambda:press('%'))
btn_P.grid(row=4,column=2)
btn_c = ttk.Button(win,text ='clear',command = clr)
btn_c.grid(row=4,column=3)

btn_e = ttk.Button(win,text ='=',command = equal)
btn_e.grid(row=5,columnspan=4,sticky = 'nsew')




win.mainloop()