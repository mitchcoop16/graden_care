import tkinter as tk
from tkinter import ttk

number_of_zones = 1

#Create Frame
def create_input_frame(container):
    n = tk.StringVar()
    frame = tk.Frame(container, bd=2, padx=5, pady=5)
    
    #Creates a combobox with dropdowns to choose from
    options = ttk.Combobox(frame, width = 20, textvariable = n)
    #list of veggies
    options['values'] = (
    "tomato",
    "bell pepper",
    "cucumber",
    "broccoli",
    "Green Bean",
    "Zucchini"
    )
    
    ttk.Label(frame, text = "Select a veggie: ", font = ("Times New Roman", 10)).grid(column=0, row=0, padx=5, pady=5)
    options.grid(column = 0, row = 1)
    options.current()

    return frame

#Create the main window
def create_main_window():
    root = tk.Tk()
    root.title('Frames')
    root.attributes('-toolwindow', False)
    column_number1=0
    column_number2=0
    column_number3=0
    
    #Create zones 1-5
    if number_of_zones >= 1 and number_of_zones <= 5:
        for column_number1 in range(number_of_zones):
            input_frame = create_input_frame(root)
            input_frame.grid(column=column_number1, row=0)
            column_number1+=1
    #Create zones 6-10
    elif number_of_zones > 5 and number_of_zones <=10:
        for column_number1 in range(5):
            input_frame = create_input_frame(root)
            input_frame.grid(column=column_number1, row=0)
            column_number1+=1
        for column_number2 in range(number_of_zones - 5):
            input_frame = create_input_frame(root)
            input_frame.grid(column=column_number2, row=3)
            column_number2+=1
    #Create zones 11-15
    elif number_of_zones > 10 and number_of_zones <=15:
        for column_number1 in range(5):
            input_frame = create_input_frame(root)
            input_frame.grid(column=column_number1, row=0)
            column_number1+=1
        for column_number2 in range(5):
            input_frame = create_input_frame(root)
            input_frame.grid(column=column_number2, row=3)
            column_number2+=1
        for column_number2 in range(number_of_zones - 10):
            input_frame = create_input_frame(root)
            input_frame.grid(column=column_number2, row=5)
            column_number3+=1 
    #Output an error
    else:
        root.title('ERROR')
        ttk.Label(root, text = "Please enter a valid number between 1 and 15").grid(column=1, row=1)
        ttk.Button(root, text = "Acknowledge", command=quit).grid(column=1, row=2)
        
    root.mainloop()

if __name__ == "__main__":

    number_of_zones = int(input("How many zones should be made? "))
    create_main_window()
