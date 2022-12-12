# Identify and update the code below to accomplish the following tasks:

# 1) Rearrange the widgets in the window so that it looks like the picture provided
# 2) Title the dialog box to 'Joe's Automotive'
# 3) Change the default option for the radio button to 'Normal, no additional charge' (when the programs starts up)
# 4) Fix the radio buttons so that only one is selected when the user selects it
# 5) Fix the Calculate and Quit buttons (not currently working)
# 6) The Calculate button should accurately display total cost based on what is selected (formatted in currency)

#   Extra Credit
# 7) Write the code for 'Clear_Checkboxes' that will reset everything back including the total


import tkinter as tk
from tkinter import messagebox


class JoesAutomotiveBillCalculator:
    def __init__(self):
        
        #Create the Main Window
        self.main_window = tk.Tk()
        self.main_window.geometry('575x325')
        self.main_window.title("Joe's Automotive")
        
        
        #Prices of Services
        self.OilChange           = 30.00
        self.LubeJob             = 20.00
        self.RadiatorFlush       = 40.00
        self.TransmissionFlush   = 100.00
        self.Inspection          = 35.00
        self.MufflerReplacement  = 200.00
        self.TireRotation        = 20.00

        #Create Frames
        self.header_frame = tk.Frame(self.main_window)
        self.boxone_frame   = tk.Frame(self.main_window)
        self.boxtwo_frame   = tk.Frame(self.main_window)
        self.boxthree_frame = tk.Frame(self.main_window)
        self.boxfour_frame  = tk.Frame(self.main_window)
        self.boxfive_frame  = tk.Frame(self.main_window)
        self.boxsix_frame   = tk.Frame(self.main_window)
        self.boxseven_frame = tk.Frame(self.main_window)
        self.boxeight_frame = tk.Frame(self.main_window)
        self.total_frame    = tk.Frame(self.main_window)
        self.buttons_frame  = tk.Frame(self.main_window)

        
        #Create Price Labels with Spacing and Formating for Currency
        self.Oil_Price = tk.Label(self.boxone_frame,text='$' + str(format(self.OilChange,'.2f')),width=175,anchor='e')
        self.Lube_Price = tk.Label(self.boxtwo_frame,text='$' + str(format(self.LubeJob,'.2f')),width=200,anchor='e')
        self.Radiator_Price = tk.Label(self.boxthree_frame,text='$' + str(format(self.RadiatorFlush,'.2f')),width=200,anchor='e')
        self.Transmission_Price = tk.Label(self.boxfour_frame,text='$' + str(format(self.TransmissionFlush,'.2f')),width=200,anchor='e')
        self.Inspection_Price = tk.Label(self.boxfive_frame,text='$' + str(format(self.Inspection,'.2f')),width=200,anchor='e')
        self.Muffler_Price = tk.Label(self.boxsix_frame,text='$' + str(format(self.MufflerReplacement,'.2f')),width=200,anchor='e')
        self.Rotation_Price = tk.Label(self.boxseven_frame,text='$' + str(format(self.TireRotation,'.2f')),width=200,anchor='e')


        #Create Label for Type of Service (Radio buttons)
        self.service_type = tk.Label(self.header_frame,text='Services',font=('Arial Bold',15)).pack()

        #Create Label for Type of Service (Radio buttons)
        self.header_label = tk.Label(self.boxeight_frame,text='Service Type',font=('Arial Bold',15)).pack() 

        #Create Total Cost Label Variable
        self.total_calculated_label_var = tk.StringVar()

        #Create Total and Result Labels
        self.Total_Title_Label = tk.Label(self.total_frame,text='Total:')
        self.Total_Calculated_Label = tk.Label(self.total_frame,textvariable = self.total_calculated_label_var)

        #Create Checkbox Variables
        self.check1_var = tk.IntVar()
        self.check2_var = tk.IntVar()
        self.check3_var = tk.IntVar()
        self.check4_var = tk.IntVar()
        self.check5_var = tk.IntVar()
        self.check6_var = tk.IntVar()
        self.check7_var = tk.IntVar()

        #Create the Checkboxes
        self.Oil_CB = tk.Checkbutton(self.boxone_frame, text='Oil Change',variable=self.check1_var)
        self.Lube_CB = tk.Checkbutton(self.boxtwo_frame,text='Lube Job',  variable=self.check2_var)
        self.Radiator_CB = tk.Checkbutton(self.boxthree_frame,text='Radiator Flush',variable=self.check3_var)
        self.Transmission_CB = tk.Checkbutton(self.boxfour_frame,text='Transmission Flush',variable=self.check4_var)
        self.Inspection_CB = tk.Checkbutton(self.boxfive_frame,text='Inspection',variable=self.check5_var)
        self.Muffler_CB = tk.Checkbutton(self.boxsix_frame, text='Muffler Replacement',variable=self.check6_var)
        self.Rotation_CB = tk.Checkbutton(self.boxseven_frame, text='Tire Rotation',variable=self.check7_var)

        #create the Radio button variables
        self.rb_var = tk.IntVar()

        #Create Radio buttons
        self.normal_RB = tk.Radiobutton(self.boxeight_frame,text='Normal, no additional charge',variable=self.rb_var, value=0)
        self.fast_RB = tk.Radiobutton(self.boxeight_frame,text='Fast, additional charge ($100)',variable=self.rb_var, value=100)
        self.express_RB = tk.Radiobutton(self.boxeight_frame,text='Express, aditional charge ($200)',variable=self.rb_var, value=200)

        #Pack the Checkboxes
        self.Oil_CB.pack(side='left')
        self.Lube_CB.pack(side='left')
        self.Radiator_CB.pack(side='left')
        self.Transmission_CB.pack(side='left')
        self.Inspection_CB.pack(side='left')
        self.Muffler_CB.pack(side='left')
        self.Rotation_CB.pack(side='left')

        #Pack the radio buttons
        self.normal_RB.pack(side='left')
        self.fast_RB.pack(side='left')
        self.express_RB.pack(side='left')
        
        #Create the Button Widgets for the Button Frame
        self.calc_button = tk.Button(self.buttons_frame,text='Calculate', command=self.Calculate_Total)
        self.clear_button = tk.Button(self.buttons_frame,text='Clear', command=self.Clear_Checkboxes)
        self.quit_button = tk.Button(self.buttons_frame,text='Quit', command=self.main_window.destroy)
        
        #Pack the Buttons
        self.clear_button.pack(side='left')
        self.calc_button.pack(side='left',padx=30)
        self.quit_button.pack(side='left')
        
        #Pack the Lables
        self.Oil_Price.pack()
        self.Lube_Price.pack()
        self.Radiator_Price.pack()
        self.Transmission_Price.pack()
        self.Inspection_Price.pack()
        self.Muffler_Price.pack()
        self.Rotation_Price.pack()
        self.Total_Title_Label.pack(side='left')
        self.Total_Calculated_Label.pack(side='left')
        
        #Pack the Frames
        self.header_frame.pack()
        self.boxone_frame.pack()
        self.boxtwo_frame.pack()
        self.boxthree_frame.pack()
        self.boxfour_frame.pack()
        self.boxfive_frame.pack()
        self.boxsix_frame.pack()
        self.boxseven_frame.pack()
        self.boxeight_frame.pack()
        self.total_frame.pack()
        self.buttons_frame.pack()

        #Enter the tkinter main loop
        tk.mainloop()

        
    def Calculate_Total(self):

                Total = float(self.rb_var.get())
                if float(self.check1_var.get()) == 1:
                    Total += 30
                if float(self.check2_var.get()) == 1:
                    Total += 20
                if float(self.check3_var.get()) == 1:
                    Total += 40
                if float(self.check4_var.get()) == 1:
                    Total += 100
                if float(self.check5_var.get()) == 1:
                    Total += 35
                if float(self.check6_var.get()) == 1:
                    Total += 200
                if float(self.check7_var.get()) == 1:
                    Total += 20
                
                tk.messagebox.showinfo('Total', format(Total,".2f"))

        
    def Clear_Checkboxes(self):
        #NOTE: remove the below code 'pass' to continue
        pass

    
        #Uncheck Boxes

        
        #Clear Total

        
#Create an Instance to Run the Program
My_BillCalculator = JoesAutomotiveBillCalculator()
