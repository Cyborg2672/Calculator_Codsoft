from tkinter import *


root=Tk()
root.title("Calculator")



x=Entry(root,width=40,borderwidth=3)
x.grid(row=0,column=0,columnspan=3)

def but(num):
    c=x.get()
    x.delete(0,END)
    x.insert(0,c + str(num))

def add():
    first=x.get()
    global number
    global operator
    operator="add"
    number=int(first)
    x.delete(0,END)

def minus():
    first=x.get()
    global number
    global operator
    operator="minus"
    number=int(first)
    x.delete(0,END)

def multiply():
    first=x.get()
    global number
    global operator
    operator="multiply"
    number=int(first)
    x.delete(0,END)

def divide():
    first=x.get()
    global number
    global operator
    operator="divide"
    number=int(first)
    x.delete(0,END)

def equal():
    second_number=x.get()
    x.delete(0,END)

    if operator=="add":
        x.insert(0,number + int(second_number))
    if operator=="minus":
        x.insert(0,number - int(second_number))
    if operator=="multiply":
        x.insert(0,number * int(second_number))
    if operator=="divide":
        x.insert(0,number / int(second_number))

def clr():
    x.delete(0,END)

button1=Button(root,text="1",padx=40,command=lambda:but(1))
button2=Button(root,text="2",padx=40,command=lambda:but(2))
button3=Button(root,text="3",padx=40,command=lambda:but(3))

button4=Button(root,text="4",padx=40,command=lambda:but(4))
button5=Button(root,text="5",padx=40,command=lambda:but(5))
button6=Button(root,text="6",padx=40,command=lambda:but(6))

button7=Button(root,text="7",padx=40,command=lambda:but(7))
button8=Button(root,text="8",padx=40,command=lambda:but(8))
button9=Button(root,text="9",padx=40,command=lambda:but(9))

button0=Button(root,text="0",padx=40,command=lambda:but(0))
buttonplus=Button(root,text="+",padx=40,command=add)
buttonminus=Button(root,text="-",padx=40,command=minus)

buttondivide=Button(root,text="/",padx=40,command=divide)
buttonmultiply=Button(root,text="*",padx=40,command=multiply)
buttonequal=Button(root,text="=",padx=40,command=equal)

buttonclr=Button(root,text="Clear",padx=128,command=clr)




button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)

button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)

button0.grid(row=4,column=0)
buttonplus.grid(row=4,column=1)
buttonminus.grid(row=4,column=2)

buttondivide.grid(row=5,column=0)
buttonmultiply.grid(row=5,column=1)
buttonequal.grid(row=5,column=2)


buttonclr.grid(row=6,column=0,columnspan=3)








root.mainloop()
