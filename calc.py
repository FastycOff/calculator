from tkinter import *
from math import sqrt

root = Tk()
root.title("Калькулятор")
root.resizable(False, False)
root.geometry("199x210")

main = 0
action = None
entry1 = Entry(root,bg="gray")

def sum():
    global action
    global main
    main = entry1.get()
    entry1.delete("0", END)
    action = "plus"

def min():
    global action
    global main
    main = entry1.get()
    entry1.delete("0", END)
    action = "min"

def mult():
    global action
    global main
    main = entry1.get()
    entry1.delete("0",END)
    action = "mult"

def split():
    try:
        global action
        global main
        main = entry1.get()
        entry1.delete("0",END)
        action= "split"
    except:
        None
def clear():
    entry1.delete(len(entry1.get())-1,END)

def dot():
    entry1.insert(END,".")
def squaring():
    try:
        main = entry1.get()
        entry1.delete("0", END)
        main = float(main)*float(main)
        entry1.insert(0,main)
    except:
        None
#### Извлечение корня
def extR():
    global action
    global main
    try:
        main = entry1.get()
        entry1.delete(0, END)
        entry1.insert(0,sqrt(float(main)))
    except:
        None
def fc():
    entry1.delete(0, END)

def zero():
    entry1.insert(END,"0")
def one():
    entry1.insert(END,"1")
def two():
    entry1.insert(END,"2")
def three():
    entry1.insert(END,"3")
def four():
    entry1.insert(END,"4")
def five():
    entry1.insert(END,"5")
def six():
    entry1.insert(END,"6")
def seven():
    entry1.insert(END,"7")
def eight():
    entry1.insert(END,"8")
def nine():
    entry1.insert(END,"9")

## знак равно, заключает действия
def end():
    global action
    global main
    global add
    global result
    try:

        add = entry1.get()
        if action == "plus":
            result = float(main)+float(add)
        if action == "min":
            result = float(main)-float(add)
        if action == "mult":
            result = float(main)*float(add)
        if action == "split":
            result = float(main)/float(add)
        entry1.delete("0", END)
        entry1.insert(0, result)
        action = None
        main = 0
        add = 0
    except:
        None
# кнопки действий
but1 = Button(root,text = "+", command=sum,bg="gray",fg="pink",width=2,height=1)
but3 = Button(root,text = "=", command=end,bg="blue",fg="pink",width=2,height=1)
but2 = Button(root,text = "-", command=min,bg="gray",fg="pink",width=2,height=1)
but4 = Button(root,text = "*", command=mult,bg="gray",fg="pink",width=2,height=1)
but5 = Button(root,text = "/", command=split,bg="gray",fg="pink",width=2,height=1)
but6 = Button(root,text = ".", command=dot,bg="gray",fg="pink",width=2,height=1)
but7 = Button(root,text = "⌫ ",command=clear,bg="gray",fg="pink",width=2,height=1)
but8 = Button(root,text = "√", command=extR,bg="gray",fg="pink",width=2,height=1)
but9 = Button(root,text = "Clear", command=fc,bg="gray",fg="pink",width=2,height=1)
but10= Button(root,text = "X²", command=squaring,bg="gray",fg="pink",width=2,height=1)
#кнопки с цифрами
butzero = Button(root,text = "0",command=zero,bg="white",fg="green",width=2,height=1)
butone = Button(root,text =  "1",command=one,bg="white",fg="green",width=2,height=1)
buttwo = Button(root,text =  "2",command=two,bg="white",fg="green",width=2,height=1)
butthree = Button(root,text ="3",command=three,bg="white",fg="green",width=2,height=1)
butfour = Button(root,text = "4",command=four,bg="white",fg="green",width=2,height=1)
butfive = Button(root,text = "5",command=five,bg="white",fg="green",width=2,height=1)
butsix = Button(root,text  = "6",command=six,bg="white",fg="green",width=2,height=1)
butseven = Button(root,text ="7",command=seven,bg="white",fg="green",width=2,height=1)
buteight = Button(root,text ="8",command=eight,bg="white",fg="green",width=2,height=1)
butnine = Button(root,text = "9",command=nine,bg="white",fg="green",width=2,height=1)

column=34 #  y
row=45    #  x  ## длина шага каждой строки (row*int)+10

entry1.place(x=0, y=0, height=34,width=199)
but1.place(x=(3*row)+10, y=2*column)
but2.place(x=(3*row)+10, y=4*column)
but3.place(x=(2*row)+10, y=5*column)
but4.place(x=(3*row)+10, y=3*column)
but5.place(x=(3*row)+10, y=5*column)
but6.place(x=(1*row)+10, y=5*column)
but7.place(x=(3*row)+10, y=1*column)
but8.place(x=(1*row)+10, y=1*column)
but9.place(x=(2*row)+10, y=1*column)
but10.place(x=(0*row)+10,y=1*column)

butzero.place(x=(row*0+10),y=5*column)

butone.place(x=(0*row)+10, y=4*column)       
buttwo.place(x=(1*row)+10, y=4*column)
butthree.place(x=(2*row)+10,y=4*column)

butfour.place(x=(0*row)+10, y=3*column)
butfive.place(x=(1*row)+10, y=3*column) 
butsix.place(x=(2*row)+10,  y=3*column)

butseven.place(x=(0*row)+10,y=2*column)
buteight.place(x=(1*row)+10,y=2*column)
butnine.place(x=(2*row)+10,y=2*column)

root.mainloop()
