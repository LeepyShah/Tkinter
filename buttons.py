import tkinter as tk
from tkinter import ttk

#setup
window=tk.Tk()
window.title('buttons')
window.geometry('600x400')

#button
def button_func():
    print('a basic button')
    print(radio_var.get())

button_string=tk.StringVar(value='A button with string var')
button=ttk.Button(window, text='A simple button',command=button_func,textvariable=button_string)
button.pack()

#check
check_var=tk.IntVar(value=10)
check1=ttk.Checkbutton(window,
                      text='checkbox 1',
                      command=lambda:print(check_var.get()),
                      variable=check_var,
                      onvalue=10,
                      offvalue=5)
check1.pack()
check2=ttk.Checkbutton(
    window,
    text='checkbox 2',
    command=lambda:print(check_var.set(5))

)
check2.pack()

#radio button
radio_var=tk.StringVar()
radio1=ttk.Radiobutton(window ,
                       text="Radiobutton 1",
                       value='radio 1',
                       variable=radio_var,
                       command=lambda:print(radio_var.get()))
radio1.pack()
radio2=ttk.Radiobutton(window ,
                       text="Radiobutton 2"
                       ,value=2,
                        variable=radio_var,
                       command=lambda:print(radio_var.get())
                       )
radio2.pack()

#exercise
# create another checkbutton and 2 radiobuttons
# radio button:
#     Values for the buttons are A and B
#     ticking either prints the value of the checkbutton
#     ticking the radio button unchecks the checkbutton
# check button
#     ticking the checkbutton prints the value of the radio button Value
#     use tkinter var for Booleans!

#exe check_button
def get_check():
    print(exe_check_var.get())
    exe_check_var.set(False)
#data
exe_radio_var=tk.StringVar()
exe_check_var=tk.BooleanVar()
#widgets
exe_radio1=ttk.Radiobutton(window,
                          text='radio A',
                            value='A',
                            variable=exe_radio_var,
                            command=get_check
                            )
exe_radio1.pack()
exe_radio2=ttk.Radiobutton(window,
                            text='radio B',
                            value='B',
                            variable=exe_radio_var,
                            command=get_check)
exe_radio2.pack()
check3=ttk.Checkbutton(window,
                      text='check me',
                      variable=exe_check_var,
                      command=lambda:print(exe_radio_var.get())
                      )
check3.pack()

#run 
window.mainloop()