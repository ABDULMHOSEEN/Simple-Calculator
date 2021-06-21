from tkinter import *
from time import sleep
root = Tk()
root.title("Calculator First try")

#display the input and output
e = Entry(root,width=40)
e.grid(row=0,column=0,padx=15,pady=15,columnspan = 3)

def button_add(number):
    x = e.get()
    e.delete(0,END)
    e.insert(0,str(x) + str(number))

def button_clear():
    e.delete(0,END)

def button_equal():
    if e.get() == "":
        e.insert(0,"please enter a number")
    elif e.get() == "please enter a number":
        e.delete(0,END)
        e.insert(0,"please enter a number not letters")
    elif e.get() == "please enter a number not letters":
        e.delete(0, END)
        e.insert(0, "please enter a number not letters")
        print("باعوص")
    elif e.get() == "Error we can't dividing by 0":
        e.delete(0, END)
        e.insert(0, "please enter a number not letters")
    elif math == "dividing":
        sn = e.get()
        e.delete(0, END)
        s_n = float(sn)
        if s_n == 0:
            e.insert(0,"Error we can't dividing by 0")
        else:
            e.insert(0, f_n / s_n)
    else:
        sn=e.get()
        s_n=float(sn)
        e.delete(0,END)
        if math == "add":
            e.insert(0, f_n + s_n)
        elif math == "minus":
            e.insert(0, f_n - s_n)
        elif math == "multiply":
            e.insert(0, f_n * s_n)
        elif math == "dividing":
            e.insert(0, f_n / s_n)


def cadd():
    if e.get() == "":
        e.insert(0,"please enter a number")

    elif e.get() == "please enter a number":
        e.delete(0,END)
        e.insert(0,"please enter a number not letters")

    elif e.get() == "please enter a number not letters":
        e.delete(0, END)
        e.insert(0, "please enter a number not letters")
        print("باعوص")

    else:
        fn = e.get()
        global f_n
        global math
        math = "add"
        f_n = float(fn)
        e.delete(0, END)


def cminus():
    if e.get() == "":
        e.insert(0,"please enter a number")
    elif e.get() == "please enter a number":
        e.delete(0,END)
        e.insert(0,"please enter a number not letters")
    elif e.get() == "please enter a number not letters":
        e.delete(0, END)
        e.insert(0, "please enter a number not letters")
        print("باعوص")
    else:
        fn = e.get()
        global f_n
        global math
        math = "minus"
        f_n = float(fn)
        e.delete(0, END)

def cdividing():
    if e.get() == "":
        e.insert(0,"please enter a number")
    elif e.get() == "please enter a number":
        e.delete(0,END)
        e.insert(0,"please enter a number not letters")
    elif e.get() == "please enter a number not letters":
        e.delete(0, END)
        e.insert(0, "please enter a number not letters")
        print("باعوص")
    else:
        fn = e.get()
        global f_n
        global math
        math = "dividing"
        f_n = float(fn)
        e.delete(0, END)

def cmultiply():
    if e.get() == "":
        e.insert(0, "please enter a number")
    elif e.get() == "please enter a number":
        e.delete(0,END)
        e.insert(0,"please enter a number not letters")
    elif e.get() == "please enter a number not letters":
        e.delete(0, END)
        e.insert(0, "please enter a number not letters")
        print("باعوص")
    else:
        fn = e.get()
        global f_n
        global math
        math = "multiply"
        f_n = float(fn)
        e.delete(0, END)


def cnum(num) :
    
    if e.get() == "please enter a number":
        e.delete(0, END)
        button_add(num)
    elif e.get() == "please enter a number not letters":
        e.delete(0, END)
        button_add(num)
    else:
        button_add(num)


button1 = Button(root,text = 1,padx = 40 , pady =20, command = lambda: cnum(1)).grid(row =3, column = 0)
button2 = Button(root,text = 2,padx = 40 , pady =20, command = lambda: cnum(2)).grid(row =3, column = 1)
button3 = Button(root,text = 3,padx = 40 , pady =20, command = lambda: cnum(3)).grid(row =3, column = 2)

button4 = Button(root,text = 4,padx = 40 , pady =20, command = lambda: cnum(4)).grid(row =2, column = 0)
button5 = Button(root,text = 5,padx = 40 , pady =20, command = lambda: cnum(5)).grid(row =2, column = 1)
button6 = Button(root,text = 6,padx = 40 , pady =20, command = lambda: cnum(6)).grid(row =2, column = 2)

button7 = Button(root,text = 7,padx = 40 , pady =20, command = lambda: cnum(7)).grid(row =1, column = 0)
button8 = Button(root,text = 8,padx = 40 , pady =20, command = lambda: cnum(8)).grid(row =1, column = 1)
button9 = Button(root,text = 9,padx = 40 , pady =20, command = lambda: cnum(9)).grid(row =1, column = 2)

button0 = Button(root,text = 0,padx = 40 , pady =20, command =  lambda: cnum(0)).grid(row =4, column = 0)

add_button = Button(root,text = "+",padx = 39, pady = 20, command =cadd,bg="#D1E3D1").grid(row =4,column =1)
equal_button = Button(root,text = "=", padx = 39,pady=20, command = button_equal,bg="#e9def2").grid(row = 5,column=0)

minus_button = Button(root,text = "-", padx=40,pady=20 ,command = cminus,bg="#D1E3D1").grid(row=4,column=2)
multiply_button = Button(root,text = "X", padx=40,pady=20 ,command = cmultiply,bg="#D1E3D1").grid(row=5,column=1)
dividing_button = Button(root,text = "÷", padx=40,pady=20 ,command = cdividing,bg="#D1E3D1").grid(row=5,column=2)

clear_Button = Button(root,text = "Clear",padx = 125, pady = 20,bg="#D9DEF2", command=button_clear).grid(row = 6 , column =0,columnspan = 3 )

root.mainloop()
