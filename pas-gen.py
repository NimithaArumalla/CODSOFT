from tkinter import *
import string
import random
s=list(string.ascii_letters+string.digits+'!@$%^&*()#+_|\}{][:;<>?/~`')
root=Tk()
root.geometry("450x200")
root.configure(bg='#3cb371')
root.title("password generator")

def click():
    global pas
    pas=""
    size=e.get()
    size=int(size)
    if size <=5:
        #ps.delete(0,END)
        ps.config(text="length should be greater than 5")
    elif size>20:
        ps.config(text="length should be less than 20")
    else:
        for i in range(size):
            pas+=random.choice(s)
        #ps.delete(0,END)
        ps.config(text=pas)
        

l1=Label(root,text="Enter length of password:",font=('calibri',14,'bold'),bg='#3cb371',fg='white').grid(row=0,column=0)
e=Entry(root,width=30,borderwidth=5)
e.grid(row=0,column=1)
l2=Label(root,text="password:",font=('calibri',14,'bold'),bg='#3cb371',fg='white').grid(row=1,column=0)
ps=Label(root,text="your password will be here")
ps.grid(row=1,column=1)
l3=Label(root,text=" ",bg='#3cb371').grid(row=2,column=0)
b1=Button(root,text="Generate password",padx=25,pady=10,bg="#ff9600",fg="white",font=('bold'),command=click)
b1.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()
