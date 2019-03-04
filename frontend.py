from  tkinter import *
import backend

def get_selected_row(event):
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])


    #print(selected_tuple)
def view_command():
    list1.delete(0,END)
    for row in backend.views():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in backend.select(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        list1.insert(END,row)

def add_command():

    backend.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    list1.delete(0,END)
    for row in backend.views():
        list1.insert(END,row)

def delete_command():
    backend.delete(selected_tuple[0])
    list1.delete(0,END)
    for row in backend.views():
        list1.insert(END,row)
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)

def update_command():
    backend.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    list1.delete(0,END)
    for row in backend.views():
        list1.insert(END,row)
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)







window=Tk()
window.geometry("800x500")

window.title("Welcome ")

l1=Label(window,text="Title")
l1.grid(row=0,column=0)

l2=Label(window,text="Author")
l2.grid(row=0,column=2)

l3=Label(window,text="Year")
l3.grid(row=1,column=0)

l4=Label(window,text="ISBN")
l4.grid(row=1,column=2)

title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

author_text=StringVar()
e2=Entry(window,textvariable=author_text)
e2.grid(row=0,column=3)

year_text=StringVar()
e3=Entry(window,textvariable=year_text)
e3.grid(row=1,column=1)

isbn_text=StringVar()
e4=Entry(window,textvariable=isbn_text)
e4.grid(row=1,column=3)

list1=Listbox(window,height=7,width=50)
list1.grid(row=2,column=0,rowspan=7,columnspan=2)

list1.bind('<<ListboxSelect>>',get_selected_row)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

bt1=Button(window,width=10,text="View All",command=view_command).grid(row=3,column =3)
bt2=Button(window,width=10,text="Search Entry",command=search_command).grid(row=4,column =3)
bt3=Button(window,width=10,text="Add Entry",command=add_command).grid(row=5,column =3)
bt4=Button(window,width=10,text="Update",command=update_command).grid(row=6,column =3)
bt5=Button(window,width=10,text="Delete",command=delete_command).grid(row=7,column =3)
bt6=Button(window,width=10,text="Close",command=window.destroy).grid(row=8,column =3)





window.mainloop()
