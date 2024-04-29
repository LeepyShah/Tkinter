import tkinter as tk
from tkinter import ttk

def button_func():
    entry_text=entry.get()
    #update the label
    # label.configure(text="Some othe text")
    label['text']=entry_text
    entry['state']='disabled'

def ex_btn():
    entry_text=entry.get()
    label['text']='some text'
    entry['state']='enables'
#ex:
#add another button that changes text back to 'some text' and that enabels entry
#window
window=tk.Tk()
window.title('Getting and setting widgets')

#widgets
label=ttk.Label(master=window,text='Some text')
label.pack()

entry=ttk.Entry(master=window)
entry.pack()

button=ttk.Button(master=window,text="the button",command=button_func)
button.pack()

button_1=ttk.Button(master=window,text='enables',command=ex_btn)
button_1.pack()

#run
window.mainloop()