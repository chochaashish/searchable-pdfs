import os
import csv
import config

PASSWORD_DATA = config.PASSWORD_DATA

def load_password():
    with open(PASSWORD_DATA) as f:
        lis = [line.split() for line in f]        # create a list of lists
        for i, x in enumerate(lis):
            if x:
                file_name, password = x[0].split(',')            #print the list items
                config.PASSWORD_DICT[file_name] = password
