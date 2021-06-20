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

def c1():
    if e.get() == "please enter a number":
        e.delete(0, END)
        button_add(1)
    elif e.get() == "please enter a number not letters":
        e.delete(0, END)
        button_add(1)
    else:
        button_add(1)

def c2():
    if e.get() == "please enter a number":
        e.delete(0, END)
        button_add(2)
    elif e.get() == "please enter a number not letters":
        e.delete(0, END)
        button_add(2)
    else:
        button_add(2)

def c3():
    if e.get() == "please enter a number":
        e.delete(0, END)
        button_add(3)
    elif e.get() == "please enter a number not letters":
        e.delete(0, END)
        button_add(3)
    else:
        button_add(3)

def c4():
    if e.get() == "please enter a number":
        e.delete(0, END)
        button_add(4)
    elif e.get() == "please enter a number not letters":
        e.delete(0, END)
        button_add(4)
    else:
        button_add(4)

def c5():
    if e.get() == "please enter a number":
        e.delete(0, END)
        button_add(5)
    elif e.get() == "please enter a number not letters":
        e.delete(0, END)
        button_add(5)
    else:
        button_add(5)

def c6():
    if e.get() == "please enter a number":
        e.delete(0, END)
        button_add(6)
    elif e.get() == "please enter a number not letters":
        e.delete(0, END)
        button_add(6)
    else:
        button_add(6)

def c7():
    if e.get() == "please enter a number":
        e.delete(0, END)
        button_add(7)
    elif e.get() == "please enter a number not letters":
        e.delete(0, END)
        button_add(7)
    else:
        button_add(7)

def c8():
    if e.get() == "please enter a number":
        e.delete(0, END)
        button_add(8)
    elif e.get() == "please enter a number not letters":
        e.delete(0, END)
        button_add(8)
    else:
        button_add(8)

def c9():
    if e.get() == "please enter a number":
        e.delete(0, END)
        button_add(9)
    elif e.get() == "please enter a number not letters":
        e.delete(0, END)
        button_add(9)
    else:
        button_add(9)

def c0():
    if e.get() == "please enter a number":
        e.delete(0, END)
        button_add(0)
    elif e.get() == "please enter a number not letters":
        e.delete(0, END)
        button_add(0)
    else:
        button_add(0)

#button for each number

button1 = Button(root,text = 1,padx = 40 , pady =20, command = c1,).grid(row =3, column = 0)
button2 = Button(root,text = 2,padx = 40 , pady =20, command =c2).grid(row =3, column = 1)
button3 = Button(root,text = 3,padx = 40 , pady =20, command = c3).grid(row =3, column = 2)

button4 = Button(root,text = 4,padx = 40 , pady =20, command = c4).grid(row =2, column = 0)
button5 = Button(root,text = 5,padx = 40 , pady =20, command = c5).grid(row =2, column = 1)
button6 = Button(root,text = 6,padx = 40 , pady =20, command = c6).grid(row =2, column = 2)

button7 = Button(root,text = 7,padx = 40 , pady =20, command = c7).grid(row =1, column = 0)
button8 = Button(root,text = 8,padx = 40 , pady =20, command = c8).grid(row =1, column = 1)
button9 = Button(root,text = 9,padx = 40 , pady =20, command = c9).grid(row =1, column = 2)

button0 = Button(root,text = 0,padx = 40 , pady =20, command = c0).grid(row =4, column = 0)
add_button = Button(root,text = "+",padx = 39, pady = 20, command =cadd,bg="#D1E3D1").grid(row =4,column =1)
equal_button = Button(root,text = "=", padx = 39,pady=20, command = button_equal,bg="#e9def2").grid(row = 5,column=0)

minus_button = Button(root,text = "-", padx=40,pady=20 ,command = cminus,bg="#D1E3D1").grid(row=4,column=2)
multiply_button = Button(root,text = "X", padx=40,pady=20 ,command = cmultiply,bg="#D1E3D1").grid(row=5,column=1)
dividing_button = Button(root,text = "÷", padx=40,pady=20 ,command = cdividing,bg="#D1E3D1").grid(row=5,column=2)

clear_Button = Button(root,text = "Clear",padx = 125, pady = 20,bg="#D9DEF2", command=button_clear).grid(row = 6 , column =0,columnspan = 3 )

root.mainloop()
