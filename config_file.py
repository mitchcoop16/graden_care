import configparser
 
config = configparser.ConfigParser()

config['DEFAULT'] = {"ph" : "1", "moisture" : "1",
"humidity" : "1"}

config['Tomato'] = {"ph" : "8", "moisture" : "17",
"humidity" : "8"}

config['Bell Pepper'] = {"ph" : "2", "moisture" : "15",
"humidity" : "18"}

config['Cucumber'] = {"ph" : "3", "moisture" : "32",
"humidity" : "53"}

config['Broccoli'] = {"ph" : "1", "moisture" : "35",
"humidity" : "6"}

config['Green Bean'] = {"ph" : "5", "moisture" : "65",
"humidity" : "84"}

config['Zucchini'] = {"ph" : "1", "moisture" : "42",
"humidity" : "23"}