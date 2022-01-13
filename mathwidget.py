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
t=0
def veel():
    global t
    if t==0:
        aken.geometry(str(aken.winfo_width())+"x"+str(aken.winfo_height()-200))
        btn_veel.config(text="Увеличить окно")
        t=1
    else:
        aken.geometry(str(aken.winfo_width())+"x"+str(aken.winfo_height()+200))
        btn_veel.config(text="Уменьшить окно")
        t=0
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
def kit():
    x1 = np.arange(0, 9.5, 1)#min max step
    y1=(2/27)*x1*x1-3
    x2 = np.arange(-10, 0.5, 1)#min max step
    y2=0.04*x2*x2-3
    x3 = np.arange(-9, -2.5, 1)#min max step
    y3=(2/9)*(x3+6)**2+1
    x4 = np.arange(-3, 9.5, 1)#min max step
    y4=(-1/12)*(x4-3)**2+6
    x5 = np.arange(5, 8.8  , 1)#min max step
    y5=(1/9)*(x5-5)**2+2
    x6 = np.arange(5, 9 , 1)#min max step
    y6=(1/8)*(x6-7)**2+1.5
    x7 = np.arange(-13, -8.5 , 1)#min max step
    y7=(-0.75)*(x7+11)**2+6
    x8 = np.arange(-15, -12.5 , 1)#min max step
    y8=(-0.5)*(x8+13)**2+3
    x9 = np.arange(-15, -9.5 , 1)#min max step
    y9=[1]*len(x9)
    x10 = np.arange(3, 4.5 , 1)#min max step
    y10=[3]*len(x10)
    fig = plt.figure()
    plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10)
    plt.title('КИТ')
    plt.ylabel('y') 
    plt.xlabel('x')
    plt.grid(True)
    plt.show()
def glass():
    x1 = np.arange(-9,-0.5, 0.5)#min max step
    y1=(-1/16)*(x1+5)**2+2
    x2 = np.arange(1,9.5, 0.5)#min max step
    y2=(-1/16)*(x2-5)**2+2
    x3 = np.arange(-9,-0.5, 0.5)#min max step
    y3=(1/4)*(x3+5)**2-3
    x4 = np.arange(1,9.5, 0.5)#min max step
    y4=(1/4)*(x4-5)**2-3
    x5 = np.arange(-9,-5.5  , 0.5)#min max step
    y5=-(x5+7)**2+5
    x6 = np.arange(6,9.5 , 0.5)#min max step
    y6=-(x6-7)**2+5
    x7 = np.arange(-1, 1.5 , 0.5)#min max step
    y7=(-0.5)*x7*x7+1.5
    fig = plt.figure()
    plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7)
    plt.title('Очки')
    plt.ylabel('y')
    plt.xlabel('x')
    plt.grid(True)
    plt.show()  
def frog():
    x1 = np.arange(-7,7.5, 0.5)#min max step
    y1=(-3/49)*x1*x1+8
    x2 = np.arange(-7,7.5, 0.5)#min max step
    y2=(4/49)*x2*x2+1
    x3 = np.arange(-6.8,-1.5, 0.5)#min max step
    y3=(-0.75)*(x3+4)**2+11
    x4 = np.arange(2,7.3, 0.5)#min max step
    y4=(-0.75)*(x4-4)**2+11
    x5 = np.arange(-5.8,-2.3  , 0.5)#min max step
    y5=-(x5+4)**2+9
    x6 = np.arange(2.8, 6.3 , 0.5)#min max step
    y6=-(x6-4)**2+9
    x7 = np.arange(-4,4.5 , 0.5)#min max step
    y7=(4/9)*x7*x7-5
    x8 = np.arange(-5.2,5.7 , 0.5)#min max step
    y8=(4/9)*x8*x8-9
    x9 = np.arange(-7,-2.3 , 0.5)#min max step
    y9=(-1/16)*(x9+3)**2-6
    x10 = np.arange(2.8,7.5 , 0.5)#min max step
    y10=(-1/16)*(x10-3)**2-6
    x11 = np.arange(-7,0.5, 0.5)#min max step
    y11=(1/9)*(x11+4)**2-11
    x12 = np.arange(0, 7.5 ,0.5)#min max step
    y12=(1/9)*(x12-4)**2-11
    x13 = np.arange(-7,-4.0 ,0.5)#min max step
    y13=-(x13+5)**2
    x14 = np.arange(4.5 ,7.5 ,0.5)#min max step
    y14=-(x14-5)**2
    x15 = np.arange(-3, 3.5 ,0.5)#min max step
    y15=(2/9)*x15*x15+2
    fig = plt.figure()
    plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10,x11,y11,x12,y12,x13,y13,x14,y14,x15,y15)
    plt.title('Лягушка')
    plt.ylabel('y')
    plt.xlabel('x')
    plt.grid(True)
    plt.show()
def umbr():
    x1 = np.arange(-12, 12, 0.5)#min max step
    y1=(-1/18)*x1*x1+12
    x2 = np.arange(-4, 4, 0.5)#min max step
    y2=(-1/8)*x2*x2+6
    x3 = np.arange(-12, -4, 0.5)#min max step
    y3=(-1/8)*(x3+8)**2+6
    x4 = np.arange(4, 12, 0.5)#min max step
    y4=(-1/8)*(x4-8)**2+6
    x5 = np.arange(-4, -0.3 , 0.5)#min max step
    y5=2*(x5+3)**2-9
    x6 = np.arange(-4, 0.2 , 0.5)#min max step
    y6=1.5*(x6+3)**2-10
    fig = plt.figure()
    plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6)
    plt.title("Зонтик")
    plt.ylabel("y")
    plt.xlabel("y")
    plt.grid(True)
    plt.show()
aken=Tk()
aken.title("Решение квадратного уравнения")
aken.geometry('1000x500')
aken.configure(bg="lightgrey")
lbl=Label(aken,text="Решение квадратного уравнения",height=2,width=30,font="Arial 20",fg="blueviolet",bg="aliceblue",relief=GROOVE)
resen=Button(aken,text="Решить",font="Helvetica 20", fg="darkblue", bg="lightcyan", activebackground="purple", height=4, width=20 , relief=GROOVE,command=lahenda )
graf=Button(aken,text="График",font="Helvetica 20", fg="darkblue", bg="lightcyan", activebackground="purple", height=4, width=15 , relief=GROOVE, command = grafik )
vastus=Label(aken,text="Решение", height=4, width=40, font="Arial 20", fg="black", bg="thistle",relief=GROOVE)
lbl2=Label(aken,text="x**2+", height=1, width=6, font="Arial 20", fg="black", bg="lightgrey")
lbl3=Label(aken,text="x+", height=1, width=6, font="Arial 20", fg="black", bg="lightgrey")
lbl4=Label(aken,text="=0", height=1, width=6, font="Arial 20", fg="black", bg="lightgrey")
a=Entry(aken,font="Helvetica 30", width=3,fg="maroon", bg="silver",justify=RIGHT)
b=Entry(aken,font="Helvetica 30", width=3,fg="maroon", bg="silver",justify=RIGHT)
c=Entry(aken,font="Helvetica 30", width=3,fg="maroon", bg="silver",justify=RIGHT)
btn_veel=Button(aken,text="Увеличить окно",font="Calibri 10",bg="blueviolet",command=veel)
var=StringVar()
var.set("Üks")
r1=Radiobutton(aken,text="Кит",height=2, width=4, font="Arial 10", fg="black", bg="blueviolet" , variable=var,value="Кит", command=kit)
r2=Radiobutton(aken,text="Зонтик",height=2, width=4, font="Arial 10", fg="black", bg="aliceblue" ,variable=var,value="Зонтик",command=umbr)
r3=Radiobutton(aken,text="Лягушка",height=2, width=4, font="Arial 10", fg="black", bg="blueviolet" ,variable=var,value="Лягушка",command=frog)
r4=Radiobutton(aken,text="Очки",height=2, width=4, font="Arial 10", fg="black", bg="aliceblue" ,variable=var,value="Очки", command=glass)
lbl.pack()
btn_veel.pack(side=TOP)

vastus.pack(side=BOTTOM)
r1.pack(side=BOTTOM)
r2.pack(side=BOTTOM)
r3.pack(side=BOTTOM)
r4.pack(side=BOTTOM)
a.pack(side=LEFT)
lbl2.pack(side=LEFT)
b.pack(side=LEFT)
lbl3.pack(side=LEFT)
c.pack(side=LEFT)
lbl4.pack(side=LEFT)

graf.pack(side=RIGHT)
resen.pack(side=RIGHT) 
#,padx=10,pady=10

aken.mainloop()