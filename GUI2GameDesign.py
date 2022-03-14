# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 19:01:22 2020

@author: User
"""


from tkinter import *
import random
import time
#fromtkinter import ttk
from tkinter import messagebox
colours=["blue","red","yellow","green","red","pink","red","black","green","cyan"]
global i
i=0
global redcount
redcount=0
global greencount
greencount=0


def startclick(n):
    global i
    global canvas
    global redcount
    global greencount
    for i in range(1,n+1):
        m=random.randint(0,10)
        if m==1 or m==4 or m==6:
            redcount=redcount+1
        if m==3 or m==8:
            greencount=greencount+1
        try:
            a=random.randint(50,250)
            b=random.randint(50,300)
            canvas.create_oval(a,b,a+50,b+50,outline="white",fill=colours[m],width=2)
            canvas.update()
        except:
            print()
    return (1)

def level1():
    global canvas
    global redcount
    global greencount
    x=startclick(10)
    if x==1:
        time.sleep(10)
    messagebox.showinfo("ANSWER","number of red balls="+str(redcount)+" and number of green balls="+str(greencount))
    canvas.delete("all")
    redcount=0
    greencount=0
    
def level2():
    global canvas
    global redcount
    global greencount
    x=startclick(16)
    if x==1:
        time.sleep(7)
    messagebox.showinfo("ANSWER","number of red balls="+str(redcount)+" and number of green balls="+str(greencount))
    canvas.delete("all")
    redcount=0
    greencount=0
    
def level3():
    global canvas
    global redcount
    global greencount
    x=startclick(26)
    if x==1:
        time.sleep(5)
    messagebox.showinfo("ANSWER","number of red balls="+str(redcount)+"and number of green balls="+str(greencount))
    canvas.delete("all")
    redcount=0
    greencount=0
    
    

    
def startgame():
    
    l1=Button(root,text="Level 1",bg="#e79700",width=20,height=1,font=("Open Sans",13,"bold"),fg="white",command=level1)
    l1.place(x=550,y=40)  
    l2=Button(root,text="Level 2",bg="#e79700",width=20,height=1,font=("Open Sans",13,"bold"),fg="white",command=level2)
    l2.place(x=550,y=80)  
    l3=Button(root,text="Level 3",bg="#e79700",width=20,height=1,font=("Open Sans",13,"bold"),fg="white",command=level3)
    l3.place(x=550,y=120)          
   # x=startclick()
   # if x==1:
   #     time.sleep(5)
   # messagebox.showinfo("ANSWER","number of red balls="+str(redcount)+"and number of green balls="+str(greencount))
   # canvas.delete("all")
   # redcount=0
   # greencount=0



root=Tk()
root.title("COUNT THE COLOURS")
root.geometry("800x700+20+20")
canvas=Canvas(width=500,height=500,bg="#87ceeb")
canvas.place(x=20,y=20)
#===BUTTON=====
w=Label(root,text="Can you count the number of red and green coloured balls?",bg="black",fg="yellow")
w.place(x=20,y=500)
y=Label(root,text="You have 5 seconds to answer...Press Start button to play!!",bg="white",fg="blue")
y.place(x=20,y=550)
b=Button(root,text="START",bg="#e79700",width=20,height=1,font=("Open Sans",13,"bold"),fg="white",command=startgame)
b.place(x=20,y=600)
root.mainloop()