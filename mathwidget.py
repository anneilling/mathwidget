from tkinter import *
from math import *
import matplotlib.pyplot as plt
import numpy as np
global D,t
global a,b,c
n=0
def txt_to_lbl(event):
    text=txt.get()#from Entry to text
    lbl.configure(text=text)
    txt.delete(0,END)
D=-1
t="Нет решения!"
def lahenda():
    global D,t
    if (a.get()!="" and b.get()!="" and c.get()!=""):
        if (float(a.get())==0 and float(b.get())==0 and float(c.get())==0):
            vastus.configure(text=f"Ошибка!")
            a.configure(bg="red")
            b.configure(bg="red")
            c.configure(bg="red")
            graf=False
        elif float(a.get())==0 and float(b.get())!=0 and float(c.get())!=0:
            vastus.configure(text=f"Ошибка!")
            a.configure(bg="red")
            b.configure(bg="red")
            c.configure(bg="red")
            graf=False
        elif float(a.get())!=0 and float(b.get())==0 and float(c.get())!=0:
            vastus.configure(text=f"Ошибка!")
            a.configure(bg="red")
            b.configure(bg="red")
            c.configure(bg="red")
            graf=False
        elif float(a.get())!=0 and float(b.get())!=0 and float(c.get())==0:
            vastus.configure(text=f"Ошибка!")
            a.configure(bg="red")
            b.configure(bg="red")
            c.configure(bg="red")
            graf=False
        elif float(a.get())!=0 and float(b.get())!=0 and float(c.get())!=0:
            a_=float(a.get())
            b_=float(b.get())
            c_=float(c.get())
            D=b_*b_-4*a_*c_
            if D>0:
                x1_=round((-1*b_+sqrt(D))/(2*a_),2)
                x2_=round((-1*b_-sqrt(D))/(2*a_),2)
                t=f"X1={x1_},\nX2={x2_}"
                graf=True
            elif D==0:
                x1_=round((-1*b_)/(2*a_),2)
                t=f"X1={x1_}"
                graf=True
            else:
                t="Корней нет"
                graf=False
            vastus.configure(text=f"D={D}\n{t}")
            a.configure(bg="lightcyan")
            b.configure(bg="lightcyan")
            c.configure(bg="lightcyan")
               
    else:
        if a.get()=="":
            a.configure(bg="red")
            graf=False
        if b.get()=="":
            b.configure(bg="red")
            graf=False
        if c.get()=="":
            c.configure(bg="red")
            graf=False
    return graf,D,t

def grafik():
    graf,D,t=lahenda()
    if graf==True:
        a_=float(a.get())
        b_=float(b.get())
        c_=float(c.get())
        x0=(-b_)/(2*a_)
        y0=a_*x0*x0+b_*x0+c_
        x = np.arange(x0-10, x0+10, 0.5)#min max step
        y=a_*x*x+b_*x+c_
        par = plt.figure()
        plt.plot(x, y,'b:o', x0, y0,'r-d')
        plt.title('Квадратное уравнение')
        plt.ylabel('y')
        plt.xlabel('x')
        plt.grid(True)
        plt.show()
        text=f"Вершина параболлы ({x0},{y0})"
    else:
        text=f"График нет возможности построить"
    vastus.configure(text=f"D={D}\n{t}\n{text}")
    return graf,D,t

aken=Tk()
aken.title("Решение квадратного уравнения")
aken.geometry('1000x500')
aken.configure(bg="lightgrey")
lbl=Label(aken,text="Решение квадратного уравнения",height=2,width=30,font="Arial 20",fg="blueviolet",bg="aliceblue",relief=GROOVE)
resen=Button(aken,text="Решить",font="Helvetica 20", fg="darkblue", bg="lightcyan", activebackground="purple", height=4, width=20 , relief=GROOVE,command=lahenda )
graf=Button(aken,text="График",font="Helvetica 20", fg="darkblue", bg="lightcyan", activebackground="purple", height=4, width=15 , relief=GROOVE )
vastus=Label(aken,text="Решение", height=4, width=40, font="Arial 20", fg="black", bg="thistle",relief=GROOVE)
lbl2=Label(aken,text="x**2+", height=1, width=6, font="Arial 20", fg="black", bg="lightgrey")
lbl3=Label(aken,text="x+", height=1, width=6, font="Arial 20", fg="black", bg="lightgrey")
lbl4=Label(aken,text="=0", height=1, width=6, font="Arial 20", fg="black", bg="lightgrey")
a=Entry(aken,font="Helvetica 30", width=3,fg="maroon", bg="silver",justify=RIGHT)
b=Entry(aken,font="Helvetica 30", width=3,fg="maroon", bg="silver",justify=RIGHT)
c=Entry(aken,font="Helvetica 30", width=3,fg="maroon", bg="silver",justify=RIGHT)


lbl.pack()
vastus.pack(side=BOTTOM)
a.pack(side=LEFT)
lbl2.pack(side=LEFT)
b.pack(side=LEFT)
lbl3.pack(side=LEFT)
c.pack(side=LEFT)
lbl4.pack(side=LEFT)
graf.pack(side=RIGHT)
resen.pack(side=RIGHT) #,padx=10,pady=10
aken.mainloop()