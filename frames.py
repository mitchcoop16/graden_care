import tkinter as tk
from tkinter import ttk
from tkinter.constants import *
import json, os
import pandas as pd

#initial list of veggies (name, ph, humidty)
veggies = """Tomato,1,5
Bell pepper,3,4
Cucumber,7,2
Broccoli,2,1
Green Bean,5,7
Zucchini,6,4
Sweet potatoe,23,5"""

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

        #User input to get the number of zones wanted
        self.zone_label = tk.Label(self.container, text='Enter the amount of zones: ')
        self.zone_label.grid(column=0, row=0, sticky='nwse') #label will fill column
        self.zone_entry = tk.Entry(self.container, textvariable=self.zone_number)
        self.zone_entry.grid(column=1, row=0, stick='nwse') #label will fill column
        self.zone_button = tk.Button(self.container, command=self.update_zones, text='Update')
        self.zone_button.grid(column=2, row=0, sticky='nswe') #button will fill column
        self.reset_button = tk.Button(self.container, command=self.reset_frame, text='Reset All')
        self.reset_button.grid(column=3, row=0, sticky='nswe') #button will fill column

        self.filepath_txt = 'read.txt'
        self.filepath_json = 'text.json'

        #dictionary for veggie names to create the json file
        self.dict1 = {}

        #temp list to hold veggie names. Gets cleared everytime the frame gets updated
        #if new veggie is added, it will be appended
        self.list1 = []

        self.description = []
        
        #label for when table of veggies prints out
        self.fields =['NAME', 'PH', 'HUMIDITY']

        #check to see if txt file is empty or not. If it is, the default values will be written
        if self.check_file_size() == True:
            with open('read.txt', 'w') as file:
                file.writelines(veggies)
        self.convert_to_json()

    def check_file_size(self):
        """
        Purpose: checks to see if the txt file is empty or not
        Returns: boolean
        """
        if os.path.getsize(self.filepath_txt) == 0:
            return True
        else:
            return False

    def append_file(self, name, ph, humidity):
        """
        Purpose: appends to the txt file if a new veggie is added, converts txt to json
        Returns: none
        """
        with open(self.filepath_txt, 'a') as file:
            file.writelines('\n'+name+','+ph+','+humidity)

        #resets the frame
        self.reset_frame

    def convert_to_json(self):
        """
        Purpose: Convert txt file to json file
        Returns: none
        """
        with open(self.filepath_txt) as f:
            
            for line in f:
                l = 1
                # reading line by line from the text file
                self.description = list(line.strip().split(",", 3))
                
                #first key will be the veggie name
                self.sno = self.description[0]
                self.list1.append(self.sno)
                # loop variable
                i = 0
                # intermediate dictionary
                self.dict2 = {}

                while i<len(self.fields):
                    
                    # creating dictionary for each veggie
                    self.dict2[self.fields[i]]= self.description[i]
                    i = i + 1
                        
                # appending the record of each veggie to the main dictionary
                self.dict1[self.sno]= self.dict2
                l = l + 1

        self.out_file = open(self.filepath_json, "w")
        json.dump(self.dict1, self.out_file, indent=4)
        self.out_file.close()

    def print_table(self):
        """
        Purpose: Prints pretty table of veggies and their values
        Returns: none
        """
        with open(self.filepath_json, "r") as readfile:
            self.x = json.load(readfile)

            self.df = pd.DataFrame.from_dict(self.x, orient='index')
            print(self.df)

    def find_veggie(self):
        """
        Purpose: Asks user what veggie they want to search for.
        If veggie if not in the json file, user will be able to add it if desired.
        Returns: none
        """
        self.new_veg = tk.Tk()

        ns = tk.StringVar()
        phs = tk.StringVar()
        hs = tk.StringVar()

        self.new_veg.title('Create a new veggie')
        self.new_veg_label = tk.Label(self.new_veg, text="Enter the veggie you want")
        self.new_veg_label.grid(column=0, row=0)

        self.new_veg_label_name = tk.Label(self.new_veg, text="Name")
        self.new_veg_label_name.grid(column=0, row=1)
        self.new_veg_entry_name = tk.Entry(self.new_veg, textvariable = ns, bd =3)
        self.new_veg_entry_name.grid(column=1, row=1)

        self.new_veg_label_ph = tk.Label(self.new_veg, text="PH")
        self.new_veg_label_ph.grid(column=0, row=2)
        self.new_veg_entry_ph = tk.Entry(self.new_veg, textvariable = phs, bd =3)
        self.new_veg_entry_ph.grid(column=1, row=2)

        self.new_veg_label_humidty = tk.Label(self.new_veg, text="Humidity")
        self.new_veg_label_humidty.grid(column=0, row=3)
        self.new_veg_entry_humidty = tk.Entry(self.new_veg, textvariable = hs, bd =3)
        self.new_veg_entry_humidty.grid(column=1, row=3)

       
        self.new_veg_button =tk.Button(self.new_veg, text = "Submit", command=self.submit)
        self.new_veg_button.grid(column=2, row=0, padx=5, pady=5)

        self.exit_button =tk.Button(self.new_veg, text = "Close", command=self.hide_new_veg)
        self.exit_button.grid(column=3, row=0, padx=5, pady=5)
        
    def submit(self):
        n = self.new_veg_entry_name.get()
        p = self.new_veg_entry_ph.get()
        h = self.new_veg_entry_humidty.get()

        self.append_file(n,p,h)

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

        
        #Create combobox and options to choose from
        options = ttk.Combobox(self.frame, width = 20, textvariable = vegetable)
        
        #list of veggies to choose from
        options['values'] = (self.list1)

        #makes the options non-adjustable
        #options['state'] = 'readonly'

        veggie_label = ttk.Label(self.frame, text = "Select a veggie: ", font = ("Times New Roman", 10))
        veggie_label.grid(column=0, row=1, padx=5, pady=0)
        options.grid(column = 1, row = 1)
        options.current()
        

        def get_sensor_levels(event):
            """
            Purpose: update the frame with values from the dictionary 'vegetable needs'
            Returns: none
            """
            if vegetable.get() == "Add new":
                self.find_veggie()

            else:
                
                #Change the PH recommendation
                ph_level = self.dict1[vegetable.get()]['NAME']
                ph_value = ph_level
                ph_label.config(text=ph_value)
                
                #Change the moisture recommendation based of vegetable chosen
                moisture_level = self.dict1[vegetable.get()]['PH']
                moisture_value = moisture_level
                moisture_label.config(text=moisture_value)

                #Change the humidity recommendation based of vegetable chosen
                humidity_level = self.dict1[vegetable.get()]['HUMIDITY']
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

    def hide_new_veg(self):
        """
        Purpose: Function to destory the 'new_veg' frame that pops up when an invalid input is given
        Returns: none
        """
        self.new_veg.destroy()
     
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
            #clear the temp list of veggie names and update with newlist
            self.list1.clear()
            self.convert_to_json()
            #create 'add new' option in list
            self.list1.insert(0, "Add new")
            self.zone_numbers = self.zone_number.get()
            self.zone_numbers= int(self.zone_numbers)
            zone_number_list.append(self.zone_numbers)
            print("\nAmount of zones being created: ", self.zone_numbers)
            #prints a table of all the items listed and their values in the terminal
            print("\nHere's a list of available veggies and their values")
            print("-----------------------------------------------------")
            self.print_table()
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

#Create main window
root.mainloop()
