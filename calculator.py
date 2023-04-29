from tkinter import*
import customtkinter as ctk

root = ctk.CTk()
ctk.set_appearance_mode("dark") #mode: system (default), light ,dark
ctk.set_default_colour_theme("green") #theme :green (default),dark green,black
root.title("codeclause-GUI calculator")
root.geometry("800x600")
root.theme=("light green")

e= ctk.CTkentry(root)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)


def button_click(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

def button_clear():
    e.delete(0,END)


def button_add():
    first_number=e.get()
    e.delete(0,END)
    global f_num
    global math
    math="addition"
    f_num=int(first_number)

def button_equal():
    second_number=e.get()
    e.delete(0,END)

    if math =="addition":
        e.insert(0,f_num+int(second_number))

    if math =="subtraction":
        e.insert(0,f_num-int(second_number))

    if math =="multiplication":
        e.insert(0,f_num*int(second_number))

    if math =="division":
        e.insert(0,f_num/int(second_number))


def button_subtract():
    first_number = e.get()
    global f_fum
    global math
    math="subtraction"
    f_num=int(first_number)
    e.delete(0,END)


def button_multiply():
    first_number = e.get()
    global f_fum
    global math
    math="multiplication"
    f_num=int(first_number)
    e.delete(0,END)

def button_divided():
    first_number = e.get()
    global f_fum
    global math
    math="division"
    f_num=int(first_number)
    e.delete(0,END)

#define buttons

button_1=ctk.CTkbutton(root,text="1",
  command=lambda: button_click(1))

button_2=ctk.CTkbutton(root,text="2",
  command=lambda: button_click(2))

button_3=ctk.CTkbutton(root,text="3",
  command=lambda: button_click(3))

button_4=ctk.CTkbutton(root,text="4",
  command=lambda: button_click(4))

button_5=ctk.CTkbutton(root,text="5",
  command=lambda: button_click(5))

button_6=ctk.CTkbutton(root,text="6",
  command=lambda: button_click(6))

button_7=ctk.CTkbutton(root,text="7",
  command=lambda: button_click(7))

button_8=ctk.CTkbutton(root,text="8",
  command=lambda: button_click(8))

button_9=ctk.CTkbutton(root,text="9",
  command=lambda: button_click(9))

button_0=ctk.CTkbutton(root,text="0",
  command=lambda: button_click(0))

    
button_add=ctk.CTkbutton(root,text="+",
  command=button_add)

button_equal=ctk.CTkbutton(root,text="=",
  command=button_equal)

button_clear=ctk.CTkbutton(root,text="Clear",
  command=button_clear)

button_subtract=ctk.CTkbutton(root,text="-",
  command=button_subtract)

button_multiply=CTk.CTkbutton(root,text="*",
  command=button_multiply)

button_divide=CTk.CTkbutton(root,text="/", 
  command=button_divide)


# put the buttons on screen

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)


button_0.grid(row=4,column=0)
button_clear.grid(row=4,column=1,columnspan=2)


button_add.grid(row=5,column=0)
button_equal.grid(row=5,column=1,columnspan=2)


button_subtract.grid(row=6,column=0)
button_multiply.grid(row=6,column=2)
button_divide.grid(row=6,column=1)


root.mainloop()