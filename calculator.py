from tkinter import *
root=Tk()
e=Entry(root,width=55,borderwidth=5)
e.grid(row=0,column=0,padx=10,pady=10,columnspan=4)
root.title("calculator")
def b_click(num):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(num))
def b_clear():
    e.delete(0,END)
def b_add():
    first=e.get()
    global f_num
    global math
    math="add"
    f_num=int(first)
    e.delete(0,END)
        
def b_sub():
    first=e.get()
    global f_num
    global math
    math="sub"
    f_num=int(first)
    e.delete(0,END)
def b_mul():
    first=e.get()
    global f_num
    global math
    math="mul"
    f_num=int(first)
    e.delete(0,END)

def b_div():
    first=e.get()
    global f_num
    global math
    math="div"
    f_num=int(first)
    e.delete(0,END)

def b_equal():
    second=e.get()
    e.delete(0,END)
    if math=="add":
        e.insert(0,f_num+int(second))
    if math=="sub":
        e.insert(0,f_num-int(second))
    if math=="mul":
        e.insert(0,f_num*int(second))
    if math=="div":
        e.insert(0,f_num/int(second))
    


b1=Button(root,text="1",bg='#788478',fg="white",padx=40,pady=20,command=lambda:b_click(1)).grid(row=1,column=0)
b2=Button(root,text="2",bg='#788478',fg="white",padx=40,pady=20,command=lambda:b_click(2)).grid(row=1,column=1)
b3=Button(root,text="3",bg='#788478',fg="white",padx=40,pady=20,command=lambda:b_click(3)).grid(row=1,column=2)

b4=Button(root,text="4",bg='#788478',fg="white",padx=40,pady=20,command=lambda:b_click(4)).grid(row=2,column=0)
b5=Button(root,text="5",bg='#788478',fg="white",padx=40,pady=20,command=lambda:b_click(5)).grid(row=2,column=1)
b6=Button(root,text="6",bg='#788478',fg="white",padx=40,pady=20,command=lambda:b_click(6)).grid(row=2,column=2)

b7=Button(root,text="7",bg='#788478',fg="white",padx=40,pady=20,command=lambda:b_click(7)).grid(row=3,column=0)
b8=Button(root,text="8",bg='#788478',fg="white",padx=40,pady=20,command=lambda:b_click(8)).grid(row=3,column=1)
b9=Button(root,text="9",bg='#788478',fg="white",padx=40,pady=20,command=lambda:b_click(9)).grid(row=3,column=2)

b0=Button(root,text="0",bg='#788478',fg="white",padx=40,pady=20,command=lambda:b_click(0)).grid(row=4,column=0)
b_ad=Button(root,text="+",bg='#685734',fg="white",padx=39,pady=20,command=b_add).grid(row=1,column=3)
b_cl=Button(root,text="c",padx=40,pady=20,command=b_clear).grid(row=4,column=2)
b_e=Button(root,text="=",padx=40,pady=20,command=b_equal).grid(row=4,column=1)

b_su=Button(root,text="-",bg='#685734',fg="white",padx=41,pady=20,command=b_sub).grid(row=2,column=3)
b_mu=Button(root,text="x",bg='#685734',fg="white",padx=41,pady=20,command=b_mul).grid(row=3,column=3)
b_di=Button(root,text="/",bg='#685734',fg="white",padx=41,pady=20,command=b_div).grid(row=4,column=3)


root.mainloop()
