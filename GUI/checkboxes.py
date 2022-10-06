import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry('500x200')
        self.main_window.title('Label Demo')

        self.topframe = tkinter.Frame(self.main_window)
        self.bottomframe = tkinter.Frame(self.main_window)


        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()

        self.cb1 = tkinter.Checkbutton(self.topframe,text='Option1',variable=self.cb_var1)
        self.cb2 = tkinter.Checkbutton(self.topframe,text='Option2',variable=self.cb_var2)
        self.cb3 = tkinter.Checkbutton(self.topframe,text='Option3',variable=self.cb_var3)

        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()

        self.topframe.pack()
        self.bottomframe.pack()

        self.mybutton = tkinter.Button(self.main_window,text="Click Me!",command=self.do_something)
        self.quitbutton = tkinter.Button(self.main_window,text="Quit",command=self.main_window.destroy)

        self.mybutton.pack(side='left')
        self.quitbutton.pack(side='right')

        tkinter.mainloop()

    def do_something(self):
        self.message = "You have selected: \n"

        if self.cb_var1.get() == 1:
            self.message += "1\n"
        if self.cb_var2.get() == 1:
            self.message += "2\n"
        if self.cb_var3.get() == 1:
            self.message += "3\n"
        
        
        
        tkinter.messagebox.showinfo("response",self.message)

myGUI = MyGUI()
