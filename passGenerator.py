from tkinter import *
from tkinter.ttk import Label
import random

def create():
    low = "abcdefghijklmnopqrstuvwxyz0123456789"
    medium = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + low
    strong = "!@#$%^&*()" + medium
    length = variable.get()
    strength = var.get()
    password = ""

    if strength == 0:
        for _ in range (length):
            password += random.choice(low)
        return password

    elif strength == 1:
        for _ in range (length):
            password += random.choice(medium)
        return password

    else:
        for _ in range (length):
            password += random.choice(strong)
        return password

    reveal()

def genPass():
    passwordField.delete(0, END)
    password = create()
    passwordField.config(state = NORMAL)
    passwordField.insert(10,password)


def copyPass():
    password = passwordField.get()
    root.clipboard_append(password)


root = Tk()
root.title(string = "Password Generator")
root.geometry("400x200")
root.resizable(height = False, width = False)
root['background'] = '#DCAE96'
    
generateButton = Button(root, text = "Generate", command = genPass)
generateButton.place(x = 180, y = 150)

password = Label(root, text = "Password: ", font = ("Times New Roman", 12))
password.place(x=20, y=20)
passwordField = Entry(state = DISABLED)
passwordField.place(x=100, y=22)
    
copyButton = Button(root, text = "Copy", command = copyPass)
copyButton.place(x = 240, y = 18)

lenLabel = Label(root, text = "Length: ", font = ("Times New Roman", 12))
lenLabel.place(x = 20, y = 55)
lenOptions = ["8","9","10","11","12","13","14","15","16","17","18","19","20",
             "21","22","23","24","25","26","27","28","29","30"]
variable = IntVar()
variable.set(lenOptions[0])
lenMenu = OptionMenu(root, variable, *lenOptions)
lenMenu.place(x = 80, y = 50)

var = IntVar()
low = Radiobutton(root, text = "Low", variable = var, value = 0)
low.place(x = 150, y = 55)
medium = Radiobutton(root, text = "Medium", variable = var, value = 1)
medium.place(x = 210, y = 55)
strong = Radiobutton(root, text = "Strong", variable = var, value = 2)
strong.place(x = 295, y = 55)
    
root.mainloop()
