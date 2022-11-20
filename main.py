import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as mBox
import subprocess
import os
import time
from colored import fg
color = fg('black')

def delete():
   aLabel.destroy()
   action.destroy()

win = tk.Tk()
win.title("TacoHub - [BETA]")
win.iconbitmap("icon.ico")
win.resizable(False, False)
win.geometry("300x100")
aLabel = ttk.Label(win ,text="TacoHub" ,font=("Lucon", 16))
aLabel.grid(column=0, row=0)
win.columnconfigure(0, weight=1)
win.rowconfigure(0, weight=0)
 
mainframe = tk.Frame(win)
mainframe.grid(column=0, row=0, sticky='new')
mainframe.grid_columnconfigure(0, weight=3)

def cs():
   delete()

   def osr():
    os.system("start .\h4k\osr")
    os.system("cd..")
    os.system("cd..")

   def rt():
    os.system("start .\h4k\ort")
    os.system("cd..")
    os.system("cd..")

   def au():
    os.system("start .\h4k\oau")
    os.system("cd..")
    os.system("cd..")

   bLabel = ttk.Label(win ,text="CSGO" ,font=("Lucon", 16))
   bLabel.grid(column=0, row=0)
   mainframe = tk.Frame(win)
   mainframe.grid(column=0, row=0, sticky='new')
   mainframe.grid_columnconfigure(0, weight=3)
   action = ttk.Button(win, text="OSIRIS", command=osr)
   action.grid(column=0, row=1)
   action = ttk.Button(win, text="RAWETRIP", command=rt)
   action.grid(column=0, row=2)
   action = ttk.Button(win, text="AURORA", command=au)
   action.grid(column=0, row=3)

def mc():
    def mt():
        os.system("start .\mch\mt")
    def im():
        os.system("start .\mch\im")
    def inr():
        os.system("start .\mch\in")

    cLabel = ttk.Label(win ,text="MINECRAFT" ,font=("Lucon", 16))
    cLabel.grid(column=0, row=0)
    mainframe = tk.Frame(win)
    mainframe.grid(column=0, row=0, sticky='new')
    mainframe.grid_columnconfigure(0, weight=3)
    action = ttk.Button(win, text="IMPACT - [1.16.5]", command=im)
    action.grid(column=0, row=1)
    action = ttk.Button(win, text="METEOR - [1.19.2]", command=mt)
    action.grid(column=0, row=2)
    action = ttk.Button(win, text="INERTIA - [1.16.5]", command=inr)
    action.grid(column=0, row=3)

def tls():
    delete()
    def hw():
        os.system("python hwic.py")
        time.sleep(1)
    def sp():
        os.system("python setup.py")
        time.sleep(1)
    def ps():
        os.system("python psg.py")
        time.sleep(1)

    cLabel = ttk.Label(win ,text="TOOLS" ,font=("Lucon", 16))
    cLabel.grid(column=0, row=0)
    mainframe = tk.Frame(win)
    mainframe.grid(column=0, row=0, sticky='new')
    mainframe.grid_columnconfigure(0, weight=3)
    action = ttk.Button(win, text="HWIC", command=hw)
    action.grid(column=0, row=1)
    action = ttk.Button(win, text="SETUP", command=sp)
    action.grid(column=0, row=2)
    action = ttk.Button(win, text="PASSGEN", command=ps)
    action.grid(column=0, row=3)
    
action = ttk.Button(win, text="CSGO", command=cs)
action.grid(column=0, row=1)
action = ttk.Button(win, text="MC", command=mc)
action.grid(column=0, row=2)
action = ttk.Button(win, text="TOOLS", command=tls)
action.grid(column=0, row=3)

win.mainloop()