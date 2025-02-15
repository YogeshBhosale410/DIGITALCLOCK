import tkinter as tk
from time import strftime
from tkinter import messagebox
from playsound import playsound
import threading
 #you can transfor time and adate as you need

# we need to create the root window which is our main window wher we can simply add out elemets or attributes
root=tk.Tk()
root.title=("DIGITAL CLOCK")
altime='13:40:50'
sound=r"PROJECTS\DIGITALCLOCK\alert.mp3"
def alaram():
    playsound(sound)
def message():
    messagebox.showinfo("ALARAM","utt jaa abhi tho bahi.....")


# NEXT WE CAN CRETATE THE TIME FUNCTION
def time():
    string=strftime('%H:%M:%S  %p \n %D')
    # in this observe taht p is  capital latter
    label.config(text=string)

    if strftime('%H:%M:%S')==altime:
        threading.Thread(target=alaram, daemon=True).start()
        message()

       
                 
   
    label.after(1000,time)


# careating label object and assining the label font size and backgroud etc
label=tk.Label(root,font=('calibri',40,'bold'),background='black',foreground='red')

    # in this we are paking or adding the labale elements in root window  or arrnage in apporopriate manner
label.pack(anchor='center')

time()
    # it loop the main window and wait for the user input
root.mainloop()