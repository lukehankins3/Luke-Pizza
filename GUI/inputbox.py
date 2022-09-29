import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry('500x200')
        self.main_window.title('InputBox Demo')

        self.topframe = tkinter.Frame(self.main_window)
        self.bottomframe = tkinter.Frame(self.main_window)

        self.topframe.pack()
        self.bottomframe.pack()

        self.prompt_label = tkinter.Label(self.topframe,text='Please enter the distance in kilometers')

        self.kilo_entry = tkinter.Entry(self.topframe,width=10)

        self.prompt_label.pack(side='left')
        self.kilo_entry.pack(side='left')


        self.calc_button = tkinter.Button(self.bottomframe,text="Convert",command=self.convert)
        self.quitbutton = tkinter.Button(self.main_window,text="Quit",command=self.main_window.destroy)

        self.calc_button.pack(side='left')
        self.quitbutton.pack(side='right')

        tkinter.mainloop()

    def convert(self):
        kilo = float(self.kilo_entry.get())

        miles = round(kilo * 0.6214,2)

        tkinter.messagebox.showinfo("Results",str(kilo) + 'kilometers is equal to ' + str(miles) + ' miles')

myGUI = MyGUI()



