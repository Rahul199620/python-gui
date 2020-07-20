#import the useful libraries 
import tkinter as tk
from tkinter import ttk
soft= tk.Tk() 
#create label
name= ttk.Label(soft,text='enter your name').grid(row=0,column=0,sticky=tk.W)
email= ttk.Label(soft,text='enter your email').grid(row=1,column=0,sticky=tk.W)
name= ttk.Label(soft,text='enter age').grid(row=2,column=0,sticky=tk.W)
soft.mainloop()
