import config_file, os
import tkinter as tk

file_path = 'config.ini'

def check_file_size():
    """
    Purpose: checks to see if the txt file is empty or not
    Returns: boolean
    """
    if os.path.getsize(file_path) == 0:
        return True
    else:
        return False

def find_veggie():
    """
    Purpose: Asks user what veggie they want to search for.
    If veggie if not in the json file, user will be able to add it if desired.
    Returns: none
    """
    new_veg = tk.Tk()

    ns = tk.StringVar()
    phs = tk.StringVar()
    ms = tk.StringVar()
    hs = tk.StringVar()

    new_veg.title('Create a new veggie')
    new_veg_label = tk.Label(new_veg, text="Enter the veggie you want")
    new_veg_label.grid(column=0, row=0)

    new_veg_label_name = tk.Label(new_veg, text="Name")
    new_veg_label_name.grid(column=0, row=1)
    new_veg_entry_name = tk.Entry(new_veg, textvariable = ns, bd =3)
    new_veg_entry_name.grid(column=1, row=1)

    new_veg_label_ph = tk.Label(new_veg, text="PH")
    new_veg_label_ph.grid(column=0, row=2)
    new_veg_entry_ph = tk.Entry(new_veg, textvariable = phs, bd =3)
    new_veg_entry_ph.grid(column=1, row=2)

    new_veg_label_m = tk.Label(new_veg, text="Moisture")
    new_veg_label_m.grid(column=0, row=3)
    new_veg_entry_m = tk.Entry(new_veg, textvariable = ms, bd =3)
    new_veg_entry_m.grid(column=1, row=3)

    new_veg_label_humidty = tk.Label(new_veg, text="Humidity")
    new_veg_label_humidty.grid(column=0, row=4)
    new_veg_entry_humidty = tk.Entry(new_veg, textvariable = hs, bd =3)
    new_veg_entry_humidty.grid(column=1, row=4)

    def hide_new_veg():
        """
        Purpose: Function to destory the 'new_veg' frame that pops up when an invalid input is given
        Returns: none
        """
        new_veg.destroy()

    def submit():
        """
        Purpose: Will take entries and append to the config file
        Returns: none
        """
        n = new_veg_entry_name.get()
        p = new_veg_entry_ph.get()
        m = new_veg_entry_m.get()
        h = new_veg_entry_humidty.get()

        append_file(n,p,m,h)
    
    new_veg_button =tk.Button(new_veg, text = "Submit", command=submit)
    new_veg_button.grid(column=2, row=0, padx=5, pady=5)

    exit_button =tk.Button(new_veg, text = "Close", command=hide_new_veg)
    exit_button.grid(column=3, row=0, padx=5, pady=5)

def append_file(name, ph, moisture, humidity):
    """
    Purpose: appends to the ini file if a new veggie is added
    Returns: none
    """
    try:
        config_file.config.add_section(name)
        with open(file_path, 'w') as cf:
            config_file.config.write(cf)
        
    finally:
        config_file.config.set(name, 'ph', ph)
        config_file.config.set(name, 'moisture', moisture)
        config_file.config.set(name, 'humidity', humidity)
        with open(file_path, 'w') as cf:
            config_file.config.write(cf)
