import file_handler, config_file
import tkinter as tk
from tkinter import ttk
from tkinter.constants import *

#initialize default global variables
ph_value = moisture_value = humidity_value = "?"
frame_number = "reveal me"

#list of inputs entered
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

        self.veg_list = []

        #User input to get the number of zones wanted
        self.zone_label = tk.Label(self.container, text='Enter the amount of zones: ')
        self.zone_label.grid(column=0, row=0, sticky='nwse') #label will fill column
        self.zone_entry = tk.Entry(self.container, textvariable=self.zone_number)
        self.zone_entry.grid(column=1, row=0, stick='nwse') #label will fill column
        self.zone_button = tk.Button(self.container, command=self.update_zones, text='Update')
        self.zone_button.grid(column=2, row=0, sticky='nswe') #button will fill column
        self.reset_button = tk.Button(self.container, command=self.reset_frame, text='Reset All')
        self.reset_button.grid(column=3, row=0, sticky='nswe') #button will fill column

    def reset_frame(self):
        """
        Purpose: Destroy all frames except for zone input, update button, and reset button
        Returns: none
        """
        try:
            for child in self.master.winfo_children():
                if child != self.zone_label and child != self.zone_entry and child != self.zone_button and child != self.reset_button:
                    child.destroy()
        except:
            pass

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

        config_file.config.read(file_handler.file_path)
        section = config_file.config.sections()
        for sect in section:
            self.veg_list.append(sect)
            

        #Create combobox and options to choose from
        options = ttk.Combobox(self.frame, width = 20, textvariable = vegetable)
        
        #list of veggies to choose from
        options['values'] = (self.veg_list)

        #makes the options non-adjustable
        options['state'] = 'readonly'

        veggie_label = ttk.Label(self.frame, text = "Select a veggie: ", font = ("Times New Roman", 10))
        veggie_label.grid(column=0, row=1, padx=5, pady=0)
        options.grid(column = 1, row = 1)
        options.current()
        
        def get_sensor_levels(event):
            """
            Purpose: update the frame with values from the dictionary 'vegetable needs'
            Returns: none
            """
            if vegetable.get() == "Add New":
                file_handler.find_veggie()
            else:
                #Change the PH recommendation
                ph_level = config_file.config[vegetable.get()]['ph']
                ph_value = ph_level
                ph_label.config(text=ph_value)
                
                #Change the moisture recommendation based of vegetable chosen
                moisture_level = config_file.config[vegetable.get()]['moisture']
                moisture_value = moisture_level
                moisture_label.config(text=moisture_value)

                #Change the humidity recommendation based of vegetable chosen
                humidity_level = config_file.config[vegetable.get()]['humidity']
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
        """
        Purpose: Destroys all widgets within each frame
        Returns: none
        """
        #Delete all frames before creating new ones if there are some present already
        for child in root.winfo_children():
                if child != self.zone_label and child != self.zone_entry and child != self.zone_button and child != self.reset_button:
                    child.destroy()
    
    #Creates an error pop-up
    def create_error_window(self):
        """
        Purpose: create a new window to let user know to enter a valid input
        Returns: none
        """
        self.error = tk.Tk()
        self.error.title('ERROR')
        self.error_label = tk.Label(self.error, text="Enter a valid amount between 1 and 15")
        self.error_label.grid(column=0, row=0)
        self.error_button =tk.Button(self.error, text = "Acknowledge", command=self.hide_error)
        self.error_button.grid(column=0, row=2, padx=5, pady=5)
        

    def update_zones(self):
        """
        Purpose: Creates an new frame for the amount of zones requested. Each zone will be its own frame
        Returns: none
        """
        #Capture current input of the number of zones wanted and print out
        #Handles errors if an invalid input is submitted
        try:
            self.veg_list.clear()
            self.veg_list.insert(0, "Add New")
            self.zone_numbers = self.zone_number.get()
            self.zone_numbers= int(self.zone_numbers)
            zone_number_list.append(self.zone_numbers)
            print("\nAmount of zones being created: ", self.zone_numbers)
            
            
        #Throw an error if invalid input is detected
        except:
            self.create_error_window()
            
        #destroy all previous frames made if present
        self.destroy_current_frames()

        #Create zones 1-4 row 0
        if self.zone_numbers >= 1 and self.zone_numbers <= 4:
            for self.c1 in range(self.zone_numbers):
                self.input_frame = self.create_input_frame(root)
                self.input_frame.grid(column=self.c1, row=1, padx=1, pady=1)
                self.c1+=1

        #Create zones 5-8 rows 0-1
        elif self.zone_numbers > 4 and self.zone_numbers <=8:
            for self.c1 in range(4):
                self.input_frame = self.create_input_frame(root)
                self.input_frame.grid(column=self.c1, row=1, padx=1, pady=1)
                self.c1+=1
            for self.c2 in range(self.zone_numbers - 4):
                self.input_frame = self.create_input_frame(root)
                self.input_frame.grid(column=self.c2, row=2, padx=1, pady=1)
                self.c2+=1

        #Create zones 9-12 rows 0-2
        elif self.zone_numbers > 8 and self.zone_numbers <=12:
            for self.c1 in range(4):
                self.input_frame = self.create_input_frame(root)
                self.input_frame.grid(column=self.c1, row=1, padx=1, pady=1)
                self.c1+=1
            for self.c2 in range(4):
                self.input_frame = self.create_input_frame(root)
                self.input_frame.grid(column=self.c2, row=2, padx=1, pady=1)
                self.c2+=1
            for self.c3 in range(self.zone_numbers - 8):
                self.input_frame = self.create_input_frame(root)
                self.input_frame.grid(column=self.c3, row=3, padx=1, pady=1)
                self.c3+=1
        
        #Output an error if zone is out of range
        else:
            self.create_error_window()

#Initialize main window
root = tk.Tk()

#Create class object
create_garden = MyGarden(root)