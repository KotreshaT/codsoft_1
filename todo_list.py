from tkinter import *
import tkinter.messagebox as msg
root=Tk()
root.geometry("600x500")
root.title("TODO LIST")

def filedetails():
    f1=open("todo.txt","a+")
    f1.write(f"\n{value.get()}")
    m1=msg.showinfo("info",f"{value.get()}  is added to the list ")
    lb.insert(END,f"{value.get()}")
    
def deldetails(value):
    with open("todo.txt", "r") as f:
        data = f.readlines() 
        
    with open("todo.txt", "w") as f2: 
        
        for line in data : 
            # condition for data to be deleted 
            if line.strip("\n") != value : 
                f2.write(line) 
    
    lb.delete(0, END)
    rfile = open("todo.txt", "r")

    for line in rfile.readlines():
        lb.insert(END,f"{line}")
    rfile.close()


l1=Label(root,text=" TODO LIST ",font="helevetika 20 bold",background="skyblue",padx=20,border=15).grid(row=0,column=3,ipadx=10)
l2=Label(root,text="Fill The Details : ",font="helevetika 15 bold",padx=20).grid(row=1,column=2)
value=StringVar()
e1=Entry(root,textvariable=value,font="helevetika 15 bold",background="light yellow").grid(row=1,column=3)
rfile = open("todo.txt", "r")
b1=Button(root,text="SAVE",command=filedetails,font="helevetika 15 bold",background="light yellow",padx=10).grid(row=2,column=3,ipadx=20)
b2=Button(root,text="DELETE",font="helevetika 15 bold",background="light yellow",command= lambda:deldetails(value.get())).grid(row=2,column=4,ipadx=10)

lb=Listbox(root,font="helevetika 15 bold")
lb.grid(row=3,column=3)

for line in rfile.readlines():
    lb.insert(END,f"{line}")
rfile.close()

root.mainloop()