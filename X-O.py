#!/usr/bin/python
from tkinter import *
from tkinter import messagebox
import os
m=Tk()
m.title('Ticktak')
m.geometry('1920x1080')
FLAG=True
lst=['0','1','2','3','4','5','6','7','8']
var=0
def VALIDATE(pos,txt):
    global lst
    global var
    var=var+1
    lst[pos]=txt
    if lst[0]==lst[1] and lst[0]==lst[2] and lst[1]==lst[2]:
            messagebox.showinfo('Result','User '+lst[0]+' won the game')   
            os.execv(sys.executable, ['python'] + sys.argv)            
    elif lst[3]==lst[4] and lst[4]==lst[5] and lst[3]==lst[5]:
            messagebox.showinfo('Result','User '+lst[3]+' won the game')   
            os.execv(sys.executable, ['python'] + sys.argv)  
    elif lst[6]==lst[7] and lst[7]==lst[8] and lst[8]==lst[6]:
            messagebox.showinfo('Result','User '+lst[6]+' won the game')  
            os.execv(sys.executable, ['python'] + sys.argv)              
    elif lst[0]==lst[3] and lst[3]==lst[6] and lst[6]==lst[0]:
            messagebox.showinfo('Result','User '+lst[0]+' won the game')
            os.execv(sys.executable, ['python'] + sys.argv)  
    elif lst[1]==lst[4] and lst[4]==lst[7] and lst[7]==lst[1]:
            messagebox.showinfo('Result','User '+lst[1]+' won the game')
            os.execv(sys.executable, ['python'] + sys.argv)  
    elif lst[2]==lst[5] and lst[8]==lst[5] and lst[8]==lst[2]:
            messagebox.showinfo('Result','User '+lst[5]+' won the game')
            os.execv(sys.executable, ['python'] + sys.argv)  
    elif lst[0]==lst[4] and lst[4]==lst[8] and lst[8]==lst[0]:
            messagebox.showinfo('Result','User '+lst[0]+' won the game')
            os.execv(sys.executable, ['python'] + sys.argv)  
    elif lst[2]==lst[4] and lst[4]==lst[6] and lst[6]==lst[2]:
            messagebox.showinfo('Result','User '+lst[2]+' won the game')
            os.execv(sys.executable, ['python'] + sys.argv)  
    else:
        if var==9:
            messagebox.showinfo('Result','Game is draw')
            os.execv(sys.executable, ['python'] + sys.argv)  
def CREATE(btn,i):
    global FLAG
    pos=i
    if FLAG==True:
        txt='X'
        clr='red'
        lbl1.configure(bg='white')
        lbl2.configure(bg='green')
        FLAG=False
    else:
        txt='O'
        clr='blue'
        lbl1.configure(bg='green')
        lbl2.configure(bg='white')
        FLAG=True
    btn.configure(text=txt,state='disabled',bg=clr)   
    VALIDATE(pos,txt)
def RESET():
    os.execv(sys.executable, ['python'] + sys.argv)  
lbl1=Label(m,text='USER X TURN',font=('',20))
lbl1.grid(column=4,row=1)
lbl2=Label(m,text='USER O TURN',font=('',20))
lbl2.grid(column=4,row=2)
btnRESET=Button(m,command=RESET,text='RESET',font=('',20))
btnRESET.grid(column=5,row=3)
btn1=Button(m,command=lambda:CREATE(btn1,0),height=10,width=30)
btn1.grid(column=0,row=0)
btn2=Button(m,command=lambda:CREATE(btn2,1),height=10,width=30)
btn2.grid(column=1,row=0)
btn3=Button(m,command=lambda:CREATE(btn3,2),height=10,width=30)
btn3.grid(column=2,row=0)
btn4=Button(m,command=lambda:CREATE(btn4,3),height=10,width=30)
btn4.grid(column=0,row=1)
btn5=Button(m,command=lambda:CREATE(btn5,4),height=10,width=30)
btn5.grid(column=1,row=1)
btn6=Button(m,command=lambda:CREATE(btn6,5),height=10,width=30)
btn6.grid(column=2,row=1)
btn7=Button(m,command=lambda:CREATE(btn7,6),height=10,width=30)
btn7.grid(column=0,row=2)
btn8=Button(m,command=lambda:CREATE(btn8,7),height=10,width=30)
btn8.grid(column=1,row=2)
btn9=Button(m,command=lambda:CREATE(btn9,8),height=10,width=30)
btn9.grid(column=2,row=2)
m.mainloop()


