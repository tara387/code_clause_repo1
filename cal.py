from tkinter import*

class Calculator:
    def __init__(self,master):
        self.master=master
        master.title("Calculator")

        self.display = Entry(master, width=20, font=('Georgia', 16), justify=RIGHT, bd=5)
        self.display.grid(row=0, column=0, columnspan=4, pady=10)


     #create button for the calculator
        self.create_button("1",1,0)
        self.create_button("2",1,1)
        self.create_button("3",1,2)
        self.create_button("+",1,3)

        
        self.create_button("4",2,0)
        self.create_button("5",2,1)
        self.create_button("6",2,2)
        self.create_button("*",2,3)
        
        self.create_button("7",3,0)
        self.create_button("8",3,1)
        self.create_button("9",3,2)
        self.create_button("-",3,3)

        self.create_button(".",4,0)
        self.create_button("0",4,1)
        self.create_button("=",4,2)
        self.create_button("/",4,3)


        self.create_button("C",5,0)
        self.create_button("(",5,1)
        self.create_button("(",5,2)
        self.create_button("(",5,3)
        self.create_button("sqrt",5,3)

    def create_button(self, text, row, column):
        button = Button(self.master, text=text, width=5, height=2, font=('Georgia', 16),
                        command=lambda: self.button_click(text))
        button.grid(row=row, column=column, padx=5, pady=5)

    def button_click(self, text):
        if text == "C":
            self.display.delete(0,END)
        elif text == "=":
            try:
                result = eval(self.display.get())
                self.display.delete(0,END)
                self.display.insert(0, str(result))
            except:
                self.display.delete(0, END)
                self.display.insert(0, "Error")
        elif text == "sqrt":
            try:
                result = eval(self.display.get())
                self.display.delete(0,END)
                self.display.insert(0, str(result ** 0.5))
            except:
                  self.display.delete(0,END)
                  self.display.insert(0, "Error")
        else:
            self.display.insert(END, text)

root = Tk()
Calculator = Calculator(root)
root.mainloop()
