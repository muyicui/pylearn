
# -*- coding:UTF-8 -*-# 导入 Tkinter 库
import tkinter
from tkinter import *
from tkinter import Label, Button, END
from tkinter.tix import Tk, Control, ComboBox
from tkinter.messagebox import showinfo, showwarning, showerror
top = tkinter.Tk() #create top window
top.geometry('500*500') # sieze of the window
top.title("Huanran") # title of the window
top.tk.eval("require tix") # for upgrade

#Lable
lable = tkinter.Label(top, text="hello world", font='Calibri -12 bold')
lable.pack(fill=Y, expand=1)

#button
button = tkinter.Button(top, text='Quit', command=top.quit, )
top.mainloop()