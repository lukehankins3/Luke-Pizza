import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry('500x200')
        self.main_window.title('Exercise')

        self.topframe = tkinter.Frame(self.main_window)
        self.secondframe = tkinter.Frame(self.main_window)
        self.midframe = tkinter.Frame(self.main_window)
        self.fourthframe = tkinter.Frame(self.main_window)
        self.bottomframe = tkinter.Frame(self.main_window)

        self.prompt_label1 = tkinter.Label(self.topframe,text='Enter the score for test 1')
        self.score_entry1 = tkinter.Entry(self.topframe,width=10)
        
        self.prompt_label2 = tkinter.Label(self.secondframe,text='Enter the score for test 2')
        self.score_entry2 = tkinter.Entry(self.secondframe,width=10)

        self.prompt_label3 = tkinter.Label(self.midframe,text='Enter the score for test 3')
        self.score_entry3 = tkinter.Entry(self.midframe,width=10)

        self.prompt_label1.pack(side='left')
        self.score_entry1.pack(side='left')
        self.prompt_label2.pack(side='left')
        self.score_entry2.pack(side='left')
        self.prompt_label3.pack(side='left')
        self.score_entry3.pack(side='left')

        self.topframe.pack()
        self.secondframe.pack()
        self.midframe.pack()
        self.fourthframe.pack()
        self.bottomframe.pack()


        self.avg_button = tkinter.Button(self.bottomframe,text="Average",command=self.average)
        self.quitbutton = tkinter.Button(self.main_window,text="Quit",command=self.main_window.destroy)

        self.avg_button.pack(side='left')
        self.quitbutton.pack(side='right')


        tkinter.mainloop()

    def do_something(self):
        tkinter.messagebox.showinfo("response","Thanks for clicking me!")

myGUI = MyGUI()

