# This module creates a credentials prompt box for an active Cisco NSO instance and login
import tkinter
import GetDeviceList
import Vars_Constants
from tkinter import *
import tkinter.font as font

V = Vars_Constants


def info():
    # Get the info for NSO gui

    def confirmClick():
        # This function gets the user input items for NSO API login
        V.nso_server['ip'] = enter1.get()
        V.nso_server['username'] = enter2.get()
        V.nso_server['password'] = enter3.get()
        V.nso_server['port'] = enter4.get()
        GetDeviceList.GetList()
        V.confirmed = TRUE
        root.destroy()

    root = Tk()
    root.title("NSO Input")
    root.geometry("300x250")
    message = "Confirm when done"
    text_box = Text(root, height=1, width=70)
    text_box.pack(expand=TRUE)
    text_box.insert(END, message)

    label1 = Label(root, text="NSO IP Address")
    label1.pack(side=TOP)
    enter1 = Entry(root, width=20)
    enter1.pack(side=TOP)
    enter1.insert(0, Vars_Constants.nso_server['ip'])

    label2 = Label(root, text="NSO Username")
    label2.pack(side=TOP)
    enter2 = Entry(root, width=20)
    enter2.pack(side=TOP)
    enter2.insert(0, Vars_Constants.nso_server['username'])

    label3 = Label(root, text="NSO Password")
    label3.pack(side=TOP)
    enter3 = Entry(root, width=20)
    enter3.pack(side=TOP)
    enter3.insert(0, Vars_Constants.nso_server['password'])

    label4 = Label(root, text="NSO PORT e.g. 8080")
    label4.pack(side=TOP)
    enter4 = Entry(root, width=20)
    enter4.pack(side=TOP)
    enter4.insert(0, Vars_Constants.nso_server['port'])

    button_font = font.Font(size=10, weight="bold")
    myButton1 = Button(root, text="Confirm NSO Settings", command=confirmClick)
    myButton1['font'] = button_font
    myButton1.pack()

    tkinter.mainloop()
