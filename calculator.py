from tkinter import *

# Calculation function
def calc(event):
    global scvalue
    text=event.widget.cget("text")
    if text=="=":
        if scvalue.get().isdigit():
            value=int(scvalue)
        else:
            value=eval(scvalue.get())
        scvalue.set(value)
        sval.update()
    elif text=="C":
        scvalue.set("")
        sval.update()
    else:
        scvalue.set(scvalue.get()+text)
        sval.update()

# Window properties
root=Tk()
root.geometry("300x450")
root.title("Calculator")

# Initializing screen and value
scvalue=StringVar()
sval=Entry(root,font="helvetica 30 bold",textvariable=scvalue)
sval.pack(fill=X,padx=10,pady=15)
scvalue.set("")

# making frames and button
frame=Frame(root,background="grey")
for j in range(9,6,-1):
    b=Button(frame,text=f"{j}",font="helvetica 20 bold", padx=8,pady=5)
    b.pack(side="left",padx=5,pady=10)
    b.bind('<Button-1>',calc)
b=Button(frame,text="+",font="helvetica 20 bold", padx=11,pady=5)
b.pack(side="left",padx=5,pady=10)
b.bind('<Button-1>',calc)
frame.pack()

frame=Frame(root,background="grey")
for j in range(6,3,-1):
    b=Button(frame,text=f"{j}",font="helvetica 20 bold", padx=8,pady=5)
    b.pack(side="left",padx=5,pady=10)
    b.bind('<Button-1>',calc)
b=Button(frame,text="-",font="helvetica 20 bold", padx=11,pady=5)
b.pack(side="left",padx=5,pady=10)
b.bind('<Button-1>',calc)
frame.pack()

frame=Frame(root,background="grey")
for j in range(3,0,-1):
    b=Button(frame,text=f"{j}",font="helvetica 20 bold", padx=8,pady=5)
    b.pack(side="left",padx=5,pady=10)
    b.bind('<Button-1>',calc)
b=Button(frame,text="*",font="helvetica 20 bold", padx=11,pady=5)
b.pack(side="left",padx=5,pady=10)
b.bind('<Button-1>',calc)
frame.pack()

frame=Frame(root,background="grey")
x=11
y=5
b=Button(frame,text="C",font="helvetica 20 bold", padx=x,pady=y)
b.pack(side="left",padx=5,pady=10)
b.bind('<Button-1>',calc)
b=Button(frame,text=".",font="helvetica 20 bold", padx=x,pady=y)
b.pack(side="left",padx=5,pady=10)
b.bind('<Button-1>',calc)
b=Button(frame,text="=",font="helvetica 20 bold", padx=x,pady=y)
b.pack(side="left",padx=5,pady=10)
b.bind('<Button-1>',calc)
b=Button(frame,text="/",font="helvetica 20 bold", padx=x,pady=y)
b.pack(side="left",padx=5,pady=10)
b.bind('<Button-1>',calc)
frame.pack()

root.mainloop()