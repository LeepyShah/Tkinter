import tkinter as tk
from tkinter import ttk

def button_fun():
    print(string_var.get())
    string_var.set('button pressed')
#window 
window=tk.Tk()
window.title("Tkinter Variabels")
window.geometry("300x200")
 
#tkinter variabel
string_var=tk.StringVar()


#widgets
label=ttk.Label(master=window,text="label",textvariable=string_var)
label.pack()

entry=ttk.Entry(master=window,textvariable=string_var)
entry.pack()

entry2=ttk.Entry(master=window,textvariable=string_var)
entry2.pack()

button=ttk.Button(master=window,text="button",command=button_fun)
button.pack()

#exercise
#create 2 entry fields and 1 labels ,they should all be connected via a StringVar
#set a start value of 'test'

exercise_var=tk.StringVar(value='test')
# exercise_var.set('test')

exercise_label=ttk.Label(master=window,textvariable=exercise_var)
exercise_label.pack()
entry1=ttk.Entry(master=window,textvariable=exercise_var)
entry1.pack()
entry2=ttk.Entry(master=window,textvariable=exercise_var)
entry2.pack()


#run
window.mainloop()
