import tkinter


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry('500x200')
        self.main_window.title('Label Demo')

        self.label1 = tkinter.Label(self.main_window,text='Hello World')
        self.label2 = tkinter.Label(self.main_window,text='This is my GUI program')

        self.label1.pack()
        self.label2.pack()

        tkinter.mainloop()



myGUI = MyGUI()

print("Hi there!")