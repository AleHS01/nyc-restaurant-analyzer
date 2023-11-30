import pandas as pd
import  tkinter as tk;
from tkinter import filedialog
import os
from pprint import pprint
from restaurant_data import RestaurantData
from time import sleep

# -------------------------- Initial Set-Up --------------------------
# tk.Tk().withdraw() # prevents an empty tkinter window from appearing

# Opening up CSV file choosen by user

# initial_dir = os.path.expanduser("~/Desktop")
# file_path = filedialog.askopenfilename(initialdir=initial_dir)
file_path = "/Users/alehs/Downloads/DOHMH_New_York_City_Restaurant_Inspection_Results.csv"

# -------------------------- Processing the Data --------------------------

print("Processing Data...")

resturant_data = RestaurantData(file_path)
resturant_data.sort_by_rating()

data_frame = resturant_data.get_dataframe()

boroughs = resturant_data.get_boroughs()

# -------------------------- Operations --------------------------

def default_case():
    print("Wrong Choice, Please Try Again")
    sleep(1.5)

def most_A_grade():

    boro = ""
    most = 0

    for borough in boroughs:
        if( most <  len(boroughs[borough])):
            most = len(boroughs[borough])
            boro = borough

    print(f"Borough: {boro}\nA Grade Restaurants: {most}")

def rating_base_data():
    print("")

def boroughs_restaurants():
    print()



# -------------------------- Main Menu --------------------------
quit = False

options = {
    1: most_A_grade,
    2: rating_base_data,
    3: boroughs_restaurants,    
}

while not quit:

    print("Main Menu".center(50, "-"))
    print("\nSelect and option by entering the number or character:\n")
    print("\t1: Get Borough with most grade A restaurants")
    print("\t2: Export data of restaurant withing each borough base on rating")
    print("\t3: Export data of best restaurants from each borough")
    print("\tq: Exit")
    choice = input("Enter Choice: ")
    if choice == "q":
        quit = True
        continue
    
    print("\n")
    print("-" * 50 )
    options.get(int(choice), default_case)()
    print("-" * 50 )
    sleep(1)



