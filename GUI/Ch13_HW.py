import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry('700x200')
        self.main_window.title('InputBox Demo')

        self.topframe = tkinter.Frame(self.main_window)
        self.secondframe = tkinter.Frame(self.main_window)
        self.thirdframe = tkinter.Frame(self.main_window)
        self.bottomframe = tkinter.Frame(self.main_window)


        self.prompt_label = tkinter.Label(self.topframe,text='Input Name Here:')
        self.name_entry = tkinter.Entry(self.topframe,width=15)

        self.prompt_label.pack(side='left')
        self.name_entry.pack(side='left')

        self.top_label = tkinter.Label(self.secondframe,text='Select Toppings:')
        self.crust_label = tkinter.Label(self.thirdframe,text='Select Crust:')

        self.top_label.pack(side='left')
        self.crust_label.pack(side='left')

        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()

        self.cb1 = tkinter.Checkbutton(self.secondframe,text='Pepperoni $1.00',variable=self.cb_var1, onvalue=1, offvalue=0)
        self.cb2 = tkinter.Checkbutton(self.secondframe,text='Sausage $2.00',variable=self.cb_var2, onvalue=2, offvalue=0)
        self.cb3 = tkinter.Checkbutton(self.secondframe,text='Pineapple $3.00',variable=self.cb_var3, onvalue=3, offvalue=0)

        self.cb1.pack(side='left')
        self.cb2.pack(side='left')
        self.cb3.pack(side='left')


        self.radio_var = tkinter.IntVar()

        self.rb1 = tkinter.Radiobutton(self.thirdframe,text='Thin Crust $4.00',variable=self.radio_var,value=4)
        self.rb2 = tkinter.Radiobutton(self.thirdframe,text='Pan-Tossed Crust $5.00',variable=self.radio_var,value=5)
        self.rb3 = tkinter.Radiobutton(self.thirdframe,text='Cheese-Stuffed Crust $6.00',variable=self.radio_var,value=6)

        self.rb1.pack(side='left')
        self.rb2.pack(side='left')
        self.rb3.pack(side='left')


        self.CALCbutton = tkinter.Button(self.bottomframe,text="Calculate Total",command=self.calculate)
        self.QUITbutton = tkinter.Button(self.bottomframe,text="Quit",command=self.main_window.destroy)

        self.CALCbutton.pack(side='left')
        self.QUITbutton.pack(side='right')


        self.topframe.pack()
        self.secondframe.pack()
        self.thirdframe.pack()
        self.bottomframe.pack()

        tkinter.mainloop()

    def calculate(self):
        tkinter.messagebox.showinfo("Order" , self.name_entry.get() + ", Your total is $" + str(self.radio_var.get() + 
        self.cb_var1.get() + self.cb_var2.get() + self.cb_var3.get()))
        

myGUI = MyGUI()