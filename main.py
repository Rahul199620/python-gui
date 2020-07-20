#import the useful libraries 
import tkinter as tk
from tkinter import ttk
soft= tk.Tk() 
#create label
name= ttk.Label(soft,text='enter your name').grid(row=0,column=0,sticky=tk.W)
email= ttk.Label(soft,text='enter your email').grid(row=1,column=0,sticky=tk.W)
name= ttk.Label(soft,text='enter age').grid(row=2,column=0,sticky=tk.W)
#entery box
name_var=tk.StringVar()
name_box=ttk.Entry(soft,width=16,textvariable=name_var).grid(row=0,column=1)

email_var=tk.StringVar()
email_box=ttk.Entry(soft,width=16,textvariable=email_var).grid(row=1,column=1)

age_var=tk.StringVar()
age_box=ttk.Entry(soft,width=16,textvariable=age_var).grid(row=2,column=1)
soft.mainloop()

