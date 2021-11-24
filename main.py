import file_handler, config_file, frame_handler

if __name__ == '__main__':
    #sees if ini is empty. If it is, the default values will be loaded
    if file_handler.check_file_size() == True:
        with open(file_handler.file_path, 'w') as file:
            config_file.config.write(file)
        frame_handler.root.mainloop()
    else:
        #Create main window
        frame_handler.root.mainloop()