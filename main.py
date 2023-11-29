import pandas as pd
import  tkinter as tk;
from tkinter import filedialog
import os
from pprint import pprint

# -------------------------- Initial Set-Up --------------------------
# tk.Tk().withdraw() # prevents an empty tkinter window from appearing

# Opening up CSV file choosen by user

# initial_dir = os.path.expanduser("~/Desktop")
# file_path = filedialog.askopenfilename(initialdir=initial_dir)
file_path = "/Users/alehs/Downloads/DOHMH_New_York_City_Restaurant_Inspection_Results.csv"

data_frame = pd.read_csv(file_path)

# --------------------------- Working with the Data Frame ---------------------------

# Getting boroughs and their restaurant
boroughs = {
    "BRONX": [],
    "BROOKLYN": [],
    "MANHATTAN": [],
    "QUEENS": [],
    "STATEN ISLAND": []
}

# for borough in data_frame["BORO"]:
#     if borough not in boroughs.keys() and borough != "Missing":
#         boroughs[borough] = []

# print(data_frame[data_frame["GRADE"] == "A"])
# for restaurant in data_frame[data_frame["GRADE"] == "A"].iterrows():
#     pprint(restaurant)
#     break
