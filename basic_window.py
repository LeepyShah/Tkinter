print("""Creating a Basic window with some widgets""")
# Widgets:text,buttons,checkboxes,menus,frames etc
import tkinter as tk
from tkinter import ttk

def button_func():
    print('a button was pressed')
def ex_btn():
    print("hello")
#create a window
window=tk.Tk()
window.title("Window and widgets")
window.geometry("800x500")

#ttk label
label=ttk.Label(master=window,text="This is a test")
label.pack()

#tk text
text=tk.Text(master=window)
text.pack()

#ttk entry
entry=ttk.Entry(master=window)
entry.pack()

#exersice_label
exersice_label=ttk.Label(master=window,text="my label")
exersice_label.pack()

#ttk button
button=ttk.Button(master=window,text="A button",command=button_func)
button.pack()

#exersice button
# exersice_button=ttk.Button(master=window,text="exercise button",command=ex_btn)
exersice_button=ttk.Button(master=window,text="exercise button",command=lambda: print('hello'))
exersice_button.pack()

#run
window.mainloop()

