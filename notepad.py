from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

root=Tk()
root.title("Notepad")
root.geometry("700x400")

# Functions area
def new():
    global file
    root.title("Untitled -Notepad")
    file=None
    textarea.delete(1.0,END)

def save():
    global file
    if file==None:
        file=asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])

        if file=="":
            file=None
        
        else:
            f=open(file,"w")
            f.write(textarea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file)+" -Notepad")
    else:
        f=open(file,"w")
        f.write(textarea.get(1.0,END))
        f.close()
    
def openf():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file)+" -Notepad")
        textarea.delete(1.0,END)
        f=open(file,"r")
        textarea.insert(1.0,f.read())
        f.close()

def ext():
    root.destroy()

def cut():
    textarea.event_generate(("<<Cut>>"))

def copy():
    textarea.event_generate(("<<Copy>>"))

def paste():
    textarea.event_generate(("<<Paste>>"))
    
def about():
    showinfo("About us","Notepad made by Nairo ryuunosuke")

# Text area
textarea=Text(root,font="Helvetica 14")
file=None
textarea.pack(expand=True,fill=BOTH)

# Menu area
menubar=Menu(root)
# File menu area
filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label="New file",command=new)
filemenu.add_command(label="Save file",command=save)
filemenu.add_command(label="Open file",command=openf)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=ext)
menubar.add_cascade(label="File",menu=filemenu)

# Edit menu area
editmenu=Menu(menubar,tearoff=0)
editmenu.add_command(label="Cut",command=cut)
editmenu.add_command(label="Copy",command=copy)
editmenu.add_command(label="Paste",command=paste)
menubar.add_cascade(label="Edit",menu=editmenu)

# Help menu area
helpmenu=Menu(menubar,tearoff=0)
helpmenu.add_command(label="About",command=about)
menubar.add_cascade(label="Help",menu=helpmenu)

# Scroll bar command area
scroll=Scrollbar(textarea)
scroll.pack(side=RIGHT,fill=Y)
scroll.config(command=textarea.yview)
textarea.config(yscrollcommand=scroll.set)

root.config(menu=menubar)
root.mainloop()