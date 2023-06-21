import  time
from tkinter import Label
from tkinter import *
def time_current():
    a=time.strftime("%I: %M: %S %p")
    time_display.config(text =a)
    time_display.after(200,time_current)

tk_window=Tk()


tk_window.title(" V DIGITAL CLOCK")


time_display=Label(tk_window, font=("Times New Roman ",140,"bold","italic"),bg="black",fg="red")

time_current()

time_display.pack()

tk_window.mainloop()
 
