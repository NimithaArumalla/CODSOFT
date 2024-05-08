from tkinter import *
import random

u=0
co=0
rps=["rock","paper","scissor"]
root=Tk()
root.title("game")
p=Label(root,text="PLAYER",font=("calibri",14,"bold"),bg="green",fg="white").grid(row=0,column=0)

c=Label(root,text="COMPUTER",font=("calibri",14,"bold"),bg="green",fg="white").grid(row=0,column=4)


sp=Label(root,text="      ").grid(row=1,column=1)
rock=Button(root,text="ROCK",font=("calibri",14,"bold"),bg="brown",fg="white",command=lambda:game("rock")).grid(row=2,column=0)
paper=Button(root,text="PAPER",font=("calibri",14,"bold"),bg="brown",fg="white",command=lambda:game("paper")).grid(row=2,column=2)
sp=Label(root,text="      ").grid(row=2,column=3)
scissor=Button(root,text="SCISSOR",font=("calibri",14,"bold"),bg="brown",fg="white",command=lambda:game("scissor")).grid(row=2,column=4)
sp=Label(root,text="      ").grid(row=3,column=1)
qui=Button(root,text="QUIT",font=("calibri",14,"bold"),bg="pink",fg="white",command=root.destroy).grid(row=6,column=2)

cl=Label(root,text="0",font="bold")
cl.grid(row=0,column=3)

pl=Label(root,text="0",font="bold")
pl.grid(row=0,column=1)


def game(opt):
   global u
   global co
   
   x=random.choice(rps)
   e=Entry(root,width=21,bg="black",fg="white",font=("calibri",14,"bold"))
   e.grid(row=4,column=1,columnspan=3)
   e.delete(0,END)
   e.insert(0,"computer chooses "+x)
   p=Entry(root,width=21,bg="black",fg="white",font=("calibri",14,"bold"))
   p.grid(row=5,column=1,columnspan=3)
   p.delete(0,END)
   p.insert(0,"player chooses "+opt)
   
   if opt==x:
       ep=Entry(root,bg="black",fg="white",font=("calibri",14,"bold"))
       ep.grid(row=0,column=2)
       ep.delete(0,END)
       ep.insert(0,"DRAW")

   elif((opt== 'rock' and x == 'scissor') or(opt== 'paper' and x== 'rock') or(opt== 'scissor' and x == 'paper')):
       ep=Entry(root,bg="black",fg="white",font=("calibri",14,"bold"))
       ep.grid(row=0,column=2)
       ep.delete(0,END)
       ep.insert(0,"YOU WIN")
       u+=1
       pl.config(text=u)
   else:
       ep=Entry(root,bg="black",fg="white",font=("calibri",14,"bold"))
       ep.grid(row=0,column=2)
       ep.delete(0,END)
       ep.insert(0,"COMPUTER WIN")
       co+=1
       cl.config(text=co)
root.mainloop()
