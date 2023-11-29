import pandas as pd
import  tkinter as tk;
from tkinter import filedialog
import os
# Initial Set-Up
tk.Tk().withdraw() # prevents an empty tkinter window from appearing


# Working with CSV
initial_dir = os.path.expanduser("~/Desktop")
file_path = filedialog.askopenfilename(initialdir=initial_dir)
pd.read_csv()