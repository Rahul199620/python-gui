#import the useful libraries 
import tkinter as tk
from tkinter import ttk
soft= tk.Tk() 
#create label
def press():
    user=name_var.get()
    email=email_var.get()
    age=age_var.get()
    gen=gen_var.get()
    radio=radio_bt.get()

    print(f'{user} is{ age},{email},{gen},{radio}')

name= ttk.Label(soft,text='enter your name').grid(row=0,column=0,sticky=tk.W)
email= ttk.Label(soft,text='enter your email').grid(row=1,column=0,sticky=tk.W)
age= ttk.Label(soft,text='enter age').grid(row=2,column=0,sticky=tk.W)
gender= ttk.Label(soft,text='gender').grid(row=3,column=0,sticky=tk.W)
#entery box
name_var=tk.StringVar()
name_box=ttk.Entry(soft,width=16,textvariable=name_var).grid(row=0,column=1)

email_var=tk.StringVar()
email_box=ttk.Entry(soft,width=16,textvariable=email_var).grid(row=1,column=1)

age_var=tk.StringVar()
age_box=ttk.Entry(soft,width=16,textvariable=age_var).grid(row=2,column=1)

gen_var=tk.StringVar()
gender=ttk.Combobox(soft,width=16,textvariable=gen_var)
gender['values']=('Male','Female','other')
gender.grid(row=3,column=1)

#radio button
radio_bt=tk.StringVar()
rdbutton1=ttk.Radiobutton(soft,text="student",value="student",variable=radio_bt).grid(row=4,column=0)
rdbutton2=ttk.Radiobutton(soft,text="Teacher",value="Teacher",variable=radio_bt).grid(row=4,column=1)

button = ttk.Button(soft,text='submit',command=press).grid(row=5,column=0)


soft.mainloop()
