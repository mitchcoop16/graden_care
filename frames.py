import tkinter as tk
from tkinter import ttk
from tkinter.constants import *
from time import *

#initialize default variables
ph_value = "?"
moisture_value= "?"
humidity_value= "?"
frame_number = "reveal me"

#vegetable dictionary with their needs
vegetable_needs = {
    'Tomato': {'ph': '6', 'moisture': '60', 'humidity': '70'},
    'Bell pepper': {'ph': '9', 'moisture': '61', 'humidity': '71'},
    'Cucumber': {'ph': '2', 'moisture': '62', 'humidity': '72'},
    'Broccoli': {'ph': '4', 'moisture': '63', 'humidity': '73'},
    'Green Bean': {'ph': '1', 'moisture': '64', 'humidity': '74'},
    'Zucchini': {'ph': '5', 'moisture': '65', 'humidity': '75'},
    'Sweet potatoe': {'ph': '3', 'moisture': '66', 'humidity': '76'}
    }

#temp list to compare previous zone number input
zone_number_list = [1]


class MyGarden:

    #Contructor
    def __init__(self, container):
        self.container = container

        self.container.title("The Garden")
        
        #Set default number of zones
        self.zones = 1
        self.zone_number = tk.IntVar()
        self.zone_number.set(self.zones)

        #User input to get the number of zones wanted
        self.zone_label = tk.Label(self.container, text='Enter the amount of zones: ')
        self.zone_label.grid(column=0, row=0)
        self.zone_entry = tk.Entry(self.container, textvariable=self.zone_number)
        self.zone_entry.grid(column=1, row=0)
        self.zone_button = tk.Button(self.container, command=self.update_zones, text='Update')
        self.zone_button.grid(column=2, row=0)
        self.reset_button = tk.Button(self.container, command=self.reset_frame, text='Reset All')
        self.reset_button.grid(column=3, row=0)

    def reset_frame(self):
        for child in self.master.winfo_children():
            if child != self.zone_label and child != self.zone_entry and child != self.zone_button and child != self.reset_button:
                child.destroy()

    def create_input_frame(self, master):
        """
        Purpose: create a frame with vegetable selections and the recommended needs to keep it healthy
        Returns: frame
        """
        self.master = master
        #declare string variables
        vegetable = tk.StringVar()

        #Create frame
        self.frame = tk.Frame(self.master, borderwidth=1, relief=RIDGE, padx=15, pady=10)
        #Get the frame number
        def get_frame(event):
            frame_number = str(event.widget).split(".!")[-2]
            frame_label.configure(text=frame_number)
        
        frame_number_label = ttk.Label(self.frame, text='Frame Number: ')
        frame_number_label.grid(column=0, row=0)
        frame_label = ttk.Label(self.frame, text=frame_number)
        frame_label.grid(column=1, row=0)
        frame_label.bind("<Motion>", get_frame)

        
        #Create combobox and options to choose from
        options = ttk.Combobox(self.frame, width = 20, textvariable = vegetable)
        
        #list of veggies to choose from
        options['values'] = (
        "Tomato",
        "Bell pepper",
        "Cucumber",
        "Broccoli",
        "Green Bean",
        "Zucchini",
        "Sweet potatoe"
        )
        #makes the options non-adjustable
        options['state'] = 'readonly'

        veggie_label = ttk.Label(self.frame, text = "Select a veggie: ", font = ("Times New Roman", 10))
        veggie_label.grid(column=0, row=1, padx=5, pady=0)
        options.grid(column = 1, row = 1)
        options.current()
        

        def get_sensor_levels(event):
            #current = options.current()
            if options.current != -1:
                
                #Change the PH recommendation
                ph_level = vegetable_needs[vegetable.get()]['ph']
                ph_value = ph_level
                ph_label.config(text=ph_value)
                
                #Change the moisture recommendation based of vegetable chosen
                moisture_level = vegetable_needs[vegetable.get()]['moisture']
                moisture_value = moisture_level
                moisture_label.config(text=moisture_value)

                #Change the humidity recommendation based of vegetable chosen
                humidity_level = vegetable_needs[vegetable.get()]['humidity']
                humidity_value = humidity_level
                humidity_label.config(text=humidity_value)
        
        
        options.bind('<<ComboboxSelected>>', get_sensor_levels)
        
        #Shows the recommended PH level based off vegetable chosen
        ph_label_show = ttk.Label(self.frame, text='PH Level')
        ph_label_show.grid(column=0, row=2)
        ph_label = ttk.Label(self.frame, text=ph_value)
        ph_label.grid(column=1, row=2)

        #Shows the recommended moisture level based off vegetable chosen
        moisture_label_show = ttk.Label(self.frame, text='Moisture')
        moisture_label_show.grid(column=0, row=3)
        moisture_label = ttk.Label(self.frame, text=moisture_value)
        moisture_label.grid(column=1, row=3)

        #Shows the recommended humidity level based off vegetable chosen
        humidity_label_show = ttk.Label(self.frame, text='Humidity')
        humidity_label_show.grid(column=0, row=4)
        humidity_label = ttk.Label(self.frame, text=humidity_value)
        humidity_label.grid(column=1, row=4)
        
        return self.frame
    

    def hide_error(self):
        """
        Purpose: Function to destory the 'error' frame that pops up when an invalid input is given
        Returns: none
        """
        self.error.destroy()
        
    def destroy_current_frames(self):
        #Delete all frames before creating new ones if there are some present already
        for child in root.winfo_children():
                if child != self.zone_label and child != self.zone_entry and child != self.zone_button and child != self.reset_button:
                    child.destroy()

    def update_zones(self):
        """
        Purpose: Creates an new frame for the amount of zones requested. Each zone will be its own frame. Handles errors if an invalid input is submitted
        Returns: none
        """
        
        #Capture current input of the number of zones wanted and print out
        self.zone_numbers = self.zone_number.get()
        self.zone_numbers= int(self.zone_numbers)
        zone_number_list.append(self.zone_numbers)
        print("Amount of zones being created: ", self.zone_numbers)

        
        self.destroy_current_frames()

        #Create zones 1-5 row 0
        if self.zone_numbers >= 1 and self.zone_numbers <= 5:
            for self.c1 in range(self.zone_numbers):
                self.input_frame = self.create_input_frame(root)
                self.input_frame.grid(column=self.c1, row=1)
                self.c1+=1

        #Create zones 6-10 rows 0-1
        elif self.zone_numbers > 5 and self.zone_numbers <=10:
            for self.c1 in range(5):
                self.input_frame = self.create_input_frame(root)
                self.input_frame.grid(column=self.c1, row=1)
                self.c1+=1
            for self.c2 in range(self.zone_numbers - 5):
                self.input_frame = self.create_input_frame(root)
                self.input_frame.grid(column=self.c2, row=2)
                self.c2+=1

        #Create zones 11-15 rows 0-2
        elif self.zone_numbers > 10 and self.zone_numbers <=15:
            for self.c1 in range(5):
                self.input_frame = self.create_input_frame(root)
                self.input_frame.grid(column=self.c1, row=1)
                self.c1+=1
            for self.c2 in range(5):
                self.input_frame = self.create_input_frame(root)
                self.input_frame.grid(column=self.c2, row=2)
                self.c2+=1
            for self.c3 in range(self.zone_numbers - 10):
                self.input_frame = self.create_input_frame(root)
                self.input_frame.grid(column=self.c3, row=3)
                self.c3+=1
        
        #Output an error if zone is out of range
        else:
            self.error = tk.Tk()
            self.error.title('ERROR')
            self.error_label = tk.Label(self.error, text="Enter a valid amount between 1 and 15")
            self.error_label.grid(column=0, row=0)
            self.error_button =tk.Button(self.error, text = "Acknowledge", command=self.hide_error)
            self.error_button.grid(column=0, row=2, padx=5, pady=5)

        
#Initialize main window
root = tk.Tk()

#Create class object
create_garden = MyGarden(root)

#Create main window
root.mainloop()
