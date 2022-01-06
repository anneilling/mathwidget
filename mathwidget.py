from tkinter import *
n=0
def txt_to_lbl(event):
    text=txt.get()#from Entry to text
    lbl.configure(text=text)
    txt.delete(0,END)

aken=Tk()
aken.title("Решение квадратного уравнения")
aken.geometry('1000x500')
aken.configure(bg="lightgrey")
lbl=Label(aken,text="Решение квадратного уравнения",height=2,width=30,font="Arial 20",fg="blueviolet",bg="aliceblue")
resen=Button(aken,text="Решить",font="Helvetica 20", fg="darkblue", bg="lightcyan", height=4, width=20 , relief=GROOVE )
lbl1=Label(aken,text="Решение", height=4, width=40, font="Arial 20", fg="black", bg="thistle")
lbl2=Label(aken,text="x**2+", height=1, width=6, font="Arial 20", fg="black", bg="lightgrey")
lbl3=Label(aken,text="x+", height=1, width=6, font="Arial 20", fg="black", bg="lightgrey")
lbl4=Label(aken,text="=0", height=1, width=6, font="Arial 20", fg="black", bg="lightgrey")
txt=Entry(aken,font="Helvetica 30", width=3,fg="maroon", bg="silver",justify=RIGHT)
txt2=Entry(aken,font="Helvetica 30", width=3,fg="maroon", bg="silver",justify=RIGHT)
txt3=Entry(aken,font="Helvetica 30", width=3,fg="maroon", bg="silver",justify=RIGHT)

lbl.pack()
lbl1.pack(side=BOTTOM)
txt.pack(side=LEFT)
lbl2.pack(side=LEFT)
txt2.pack(side=LEFT)
lbl3.pack(side=LEFT)
txt3.pack(side=LEFT)
lbl4.pack(side=LEFT)
resen.pack(side=RIGHT)
aken.mainloop()

