"""
Timer: user is able to set a certain amount of timer in it along with a break timer too
features:
set work and break intervals
display remaining time for work and breaks
play a sound or print a message when the time is up
Optimization:
Add a pause button
"""
from tkinter import *
from tkinter.messagebox import showinfo
import time,datetime

# test func with pass argument
def test():
    print("Hello")
# Timer code
def timerrun():
    global scvalue

    # Work timer area
    totalsec=workhourvalue.get()*3600+workminvalue.get()*60+worksecvalue.get()
    while totalsec>=0:
        timer=datetime.timedelta(seconds=totalsec)
        scvalue.set(f"{timer}- Work")
        screen.update()
        time.sleep(1)
        totalsec-=1
    showinfo("Times Up!!","Time allocated for work is over agree to proceed to rest period.")

    # Rest timer area
    totalsec=resthourvalue.get()*3600+restminvalue.get()*60+restsecvalue.get()
    while totalsec>=0:
        timer=datetime.timedelta(seconds=totalsec)
        scvalue.set(f"{timer}- Rest")
        screen.update()
        time.sleep(1)
        totalsec-=1
    showinfo("Times Up!!","Time allocated for rest is over.")
    scvalue.set("Time is Up!!!")
    screen.update()
# Clearing value code
def clear():
    global workhourvalue,workminvalue,worksecvalue,resthourvalue,restminvalue,restsecvalue
    workhourvalue.set(0)
    workminvalue.set(0)
    worksecvalue.set(0)
    resthourvalue.set(0)
    restminvalue.set(0)
    restsecvalue.set(0)
    scvalue.set("")
    screen.update()
    hourdis.update()
    mindis.update()
    secdis.update()
# About section code
def about():
    showinfo("About me","Timer made by Nairo ryuunosuke")

root=Tk()
root.geometry("300x270")
root.title("Timer")

# Menubar code
menubar=Menu(root)
helpmenu=Menu(menubar,tearoff=0)
helpmenu.add_command(label="About",command=about)
helpmenu.add_command(label="Clear",command=clear)
helpmenu.add_command(label="Exit",command=root.destroy)
menubar.add_cascade(label="Help",menu=helpmenu)

# Timer display code area
scvalue=StringVar()
screen=Entry(root,textvariable=scvalue,font="helvetica 15 bold")
Label(root,text="Timer:",font="helvetica 10").grid(row=1,column=0)
screen.grid(row=1,column=1,padx=5,pady=10)
scvalue.set("")

# Work timer setup
workhourvalue=IntVar()
workminvalue=IntVar()
worksecvalue=IntVar()
Label(root,text="For work set the time below",font="helvetica 10").grid(row=2,column=1)
Label(root,text="Hour: ",font="helvetica 10").grid(row=3,column=0)
hourdis=Entry(root,textvariable=workhourvalue)
Label(root,text="Minute: ",font="helvetica 10").grid(row=4,column=0)
mindis=Entry(root,textvariable=workminvalue)
Label(root,text="Second: ",font="helvetica 10").grid(row=5,column=0)
secdis=Entry(root,textvariable=worksecvalue)
hourdis.grid(row=3,column=1)
mindis.grid(row=4,column=1)
secdis.grid(row=5,column=1)

# Rest timer setup
resthourvalue=IntVar()
restminvalue=IntVar()
restsecvalue=IntVar()
Label(root,text="For rest set the time below",font="helvetica 10").grid(row=6,column=1)
Label(root,text="Hour: ",font="helvetica 10").grid(row=7,column=0)
hourdis=Entry(root,textvariable=resthourvalue)
Label(root,text="Minute: ",font="helvetica 10").grid(row=8,column=0)
mindis=Entry(root,textvariable=restminvalue)
Label(root,text="Second: ",font="helvetica 10").grid(row=9,column=0)
secdis=Entry(root,textvariable=restsecvalue)
hourdis.grid(row=7,column=1)
mindis.grid(row=8,column=1)
secdis.grid(row=9,column=1)

# Button to start
startbutton=Button(root,text="Run the timer",font="helvetica 10 bold",command=timerrun,pady=5).grid(row=10,column=1)
# pausebutton=Button(root,text="Pause",font="helvetica 10 bold",command=test,pady=5).grid(row=11,column=1)

# Setting the menu
root.config(menu=menubar)
root.mainloop()