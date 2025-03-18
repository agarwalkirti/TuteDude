'''
ASSIGNMENT 1:
Module 10 & 11: CALCULATOR USING TKINTER
'''
#Step 1 import tkinter
from tkinter import *
import math

#Step 2 Gui interactions
window= Tk()

#Step 3 adding inputs
window.title('Calculator')
window.geometry('500x500')
window.config(background='light grey')

e1=Entry(window,width=50,borderwidth=5)

def add():
    e1_value = e1.get()
    global math_op
    global n
    n= int(e1_value)
    print('Input1', e1_value)
    e1.delete(0,END)
    math_op = 'addition'

def sub():
    e1_value = e1.get()
    global math_op
    global n
    n= int(e1_value)
    print('Input1', e1_value)
    e1.delete(0, END)
    math_op = 'subtraction'

def mul():
    e1_value = e1.get()
    global math_op
    global n
    n= int(e1_value)
    print('Input1', e1_value)
    e1.delete(0, END)
    math_op = 'multiplication'

def div():
    e1_value = e1.get()
    global math_op
    global n
    n= int(e1_value)
    print('Input1', e1_value)
    e1.delete(0,END)
    math_op = 'division'

def equal():
    n2 = e1.get()
    e1.delete(0, END)
    print('Input2', n2)
    if math_op == 'addition' :
        e1.insert(0,n + int(n2))
    elif math_op == 'subtraction' :
        e1.insert(0,n - int(n2))
    elif math_op == 'multiplication' :
        e1.insert(0,n * int(n2))
    elif math_op == 'division' :
        e1.insert(0,n / int(n2))

def sqrt():
    e1_value = e1.get()
    n = int(e1_value)
    print('Input1', e1_value)
    n = math.sqrt(n)
    e1.insert(0,n)

def pow():
    e1_value = e1.get()
    n = int(e1_value)
    print('Input1', e1_value)
    n = math.pow(n,2)
    e1.insert(0,n)

def clear():
    e1.delete(0,END)

def click(num):
    result=e1.get()
    e1.delete(0,END)
    e1.insert(0,str(result)+str(num))

b1=Button(window,text='1',bg='grey',width=15,borderwidth=1,command=lambda:click(1))
b2=Button(window,text='2',bg='grey',width=15,borderwidth=1,command=lambda:click(2))
b3=Button(window,text='3',bg='grey',width=15,borderwidth=1,command=lambda:click(3))
b4=Button(window,text='4',bg='grey',width=15,borderwidth=1,command=lambda:click(4))
b5=Button(window,text='5',bg='grey',width=15,borderwidth=1,command=lambda:click(5))
b6=Button(window,text='6',bg='grey',width=15,borderwidth=1,command=lambda:click(6))
b7=Button(window,text='7',bg='grey',width=15,borderwidth=1,command=lambda:click(7))
b8=Button(window,text='8',bg='grey',width=15,borderwidth=1,command=lambda:click(8))
b9=Button(window,text='9',bg='grey',width=15,borderwidth=1,command=lambda:click(9))
b0=Button(window,text='0',bg='grey',width=15,borderwidth=1,command=lambda:click(0))
b_add=Button(window,text='+',bg='grey',width=15,borderwidth=1,command=add)
b_sub=Button(window,text='-',bg='grey',width=15,borderwidth=1,command=sub)
b_mul=Button(window,text='*',bg='grey',width=15,borderwidth=1,command=mul)
b_div=Button(window,text='/',bg='grey',width=15,borderwidth=1,command=div)
b_eq=Button(window,text='=',bg='grey',width=15,borderwidth=1,command=equal)
b_sqrt=Button(window,text='sqrt',bg='grey',width=15,borderwidth=1,command=sqrt)
b_pow=Button(window,text='square',bg='grey',width=15,borderwidth=1,command=pow)
b_clear=Button(window,text='clear',bg='grey',width=15,borderwidth=1,command=clear)

# row start from 0 column from 1 of grid
e1.place(x=0,y=0)

b1.place(x=10,y=90)
b2.place(x=120,y=90)
b3.place(x=220,y=90)
b4.place(x=10,y=110)
b5.place(x=120,y=110)
b6.place(x=220,y=110)
b7.place(x=10,y=130)
b8.place(x=120,y=130)
b9.place(x=220,y=130)
b0.place(x=10,y=150)
b_add.place(x=120,y=150)
b_sub.place(x=220,y=150)
b_mul.place(x=10,y=170)
b_div.place(x=120,y=170)
b_eq.place(x=220,y=170)
b_clear.place(x=10,y=190)
b_sqrt.place(x=120,y=190)
b_pow.place(x=220,y=190)

#Step 4 main loop
window.mainloop()
