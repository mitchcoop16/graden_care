import tkinter as tk
from tkinter import ttk
from tkinter.constants import *
from time import *

#veggies and their needs
vegetable_needs = {
    'Tomato': {'ph': '6', 'moisture': '60', 'humidity': '70'},
    'Bell pepper': {'ph': '9', 'moisture': '61', 'humidity': '71'},
    'Cucumber': {'ph': '2', 'moisture': '62', 'humidity': '72'},
    'Broccoli': {'ph': '4', 'moisture': '63', 'humidity': '73'},
    'Green Bean': {'ph': '1', 'moisture': '64', 'humidity': '74'},
    'Zucchini': {'ph': '5', 'moisture': '65', 'humidity': '75'},
    'Sweet potatoe': {'ph': '3', 'moisture': '66', 'humidity': '76'}
}

#Create Frame
def create_input_frame(container):
    #declare string variables
    vegetable = tk.StringVar()

    #Create frame
    frame = tk.Frame(container, borderwidth=1, relief=RIDGE, padx=15, pady=10)

    #Get the frame number
    def get_frame(event):
        frame_number = str(event.widget).split(".!")[-2]
        frame_label.configure(text=frame_number)
    
    frame_number_label = ttk.Label(frame, text='Frame Number: ')
    frame_number_label.grid(column=0, row=0)
    frame_label = ttk.Label(frame, text=frame_number)
    frame_label.grid(column=1, row=0)
    frame_label.bind("<Motion>", get_frame)

    
    #Create combobox and options to choose from
    options = ttk.Combobox(frame, width = 20, textvariable = vegetable)
    
    #list of veggies
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

    veggie_label = ttk.Label(frame, text = "Select a veggie: ", font = ("Times New Roman", 10))
    veggie_label.grid(column=0, row=1, padx=5, pady=0)
    options.grid(column = 1, row = 1)
    options.current()
    

    def get_sensor_levels(event):
        current = options.current()
        if current != -1:
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
    ph_label_show = ttk.Label(frame, text='PH Level')
    ph_label_show.grid(column=0, row=2)
    ph_label = ttk.Label(frame, text=ph_value)
    ph_label.grid(column=1, row=2)

    #Shows the recommended moisture level based off vegetable chosen
    moisture_label_show = ttk.Label(frame, text='Moisture')
    moisture_label_show.grid(column=0, row=3)
    moisture_label = ttk.Label(frame, text=moisture_value)
    moisture_label.grid(column=1, row=3)

    #Shows the recommended humidity level based off vegetable chosen
    humidity_label_show = ttk.Label(frame, text='Humidity')
    humidity_label_show.grid(column=0, row=4)
    humidity_label = ttk.Label(frame, text=humidity_value)
    humidity_label.grid(column=1, row=4)

    return frame



#Create the main window
def create_main_window():
    root = tk.Tk()
    root.title('Growing Veggies')

    zone_number = tk.IntVar()
    
    def submit():
        #variable for column numbers
        c1=0
        c2=0
        c3=0

        #Get the amount of zones wanting to create
        zone_numbers = zone_number.get()
        number_of_zones = int(zone_numbers)

        print("Number of zones being created: ", number_of_zones)
        #Create zones 1-5 row 0
        if number_of_zones >= 1 and number_of_zones <= 5:
            for c1 in range(number_of_zones):
                input_frame = create_input_frame(root)
                input_frame.grid(column=c1, row=1)
                c1+=1
        #Create zones 6-10 rows 0-1
        elif number_of_zones > 5 and number_of_zones <=10:
            for c1 in range(5):
                input_frame = create_input_frame(root)
                input_frame.grid(column=c1, row=1)
                c1+=1
            for c2 in range(number_of_zones - 5):
                input_frame = create_input_frame(root)
                input_frame.grid(column=c2, row=2)
                c2+=1
        #Create zones 11-15 rows 0-2
        elif number_of_zones > 10 and number_of_zones <=15:
            for c1 in range(5):
                input_frame = create_input_frame(root)
                input_frame.grid(column=c1, row=1)
                c1+=1
            for c2 in range(5):
                input_frame = create_input_frame(root)
                input_frame.grid(column=c2, row=2)
                c2+=1
            for c2 in range(number_of_zones - 10):
                input_frame = create_input_frame(root)
                input_frame.grid(column=c2, row=3)
                c3+=1

        #Output an error if zone is out of range
        else:
            root.title('ERROR')
            error_label = ttk.Label(root, text = "Please enter a valid number between 1 and 15")
            error_label.grid(column=1, row=1, padx=15, pady=5)
            ttk.Button(root, text = "Acknowledge", command=quit).grid(column=1, row=2, padx=5, pady=5)

    zone_label = tk.Label(root, text='Enter the amount of zones: ')
    zone_label.grid(column=0, row=0)
    zone_entry = tk.Entry(root, textvariable=zone_number)
    zone_entry.grid(column=1, row=0)

    submit_button = tk.Button(root, text='Submit', command=submit)
    submit_button.grid(column=2, row=0)

    
    
    
    root.mainloop()

if __name__ == "__main__":

    ph_value = "?"
    moisture_value= "?"
    humidity_value= "?"
    frame_number = "place cursor on me"
    #number_of_zones = int(input("Enter the number of zones wanted: "))
    #number_of_zones = 1
    create_main_window()
