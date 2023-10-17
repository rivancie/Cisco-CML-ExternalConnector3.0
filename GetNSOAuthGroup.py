# This module Requests
import tkinter
import GetDeviceList
import Vars_Constants
from tkinter import *
import tkinter.font as font
import ast
import json

V = Vars_Constants
def info():
    # Get the info for NSO gui

    def confirmClick():
        # This function gets the user input items for NSO API login
        V.auth_username = enter1.get()
        V.auth_pw = enter2.get()
        V.new_auth = ast.literal_eval(clicked2.get())
        root.destroy()

    root = Tk()
    root.title("NSO AuthGroups and Credentials")
    root.geometry("300x250")
    message = "Confirm when done"
    text_box = Text(root, height=1, width=70)
    text_box.pack(expand=TRUE)
    text_box.insert(END, message)

    label1 = Label(root, text="NSO Device Username")
    label1.pack(side=TOP)
    enter1 = Entry(root, width=20)
    enter1.pack(side=TOP)
    enter1.insert(0, Vars_Constants.auth_username)

    label2 = Label(root, text="NSO Auth Password")
    label2.pack(side=TOP)
    enter2 = Entry(root, width=20)
    enter2.pack(side=TOP)
    enter2.insert(0, Vars_Constants.auth_pw)

    # AuthGroup drop-down
    clicked2 = StringVar(root)
    clicked2.set("Select AuthGroup")

    # Create Dropdown menu
    drop2 = OptionMenu(root, clicked2, *V.authgroup_list)
    drop2.pack()

    button_font = font.Font(size=10, weight="bold")
    myButton1 = Button(root, text="Confirm NSO Credentials", command=confirmClick)
    myButton1['font'] = button_font
    myButton1.pack()

    tkinter.mainloop()
