# Spreadsheet Reader Python Script - NYC Restaurant Analyzer


This Python script processes and analyzes NYC restaurant inspection data to provide valuable insights. Using pandas, it reads and processes a CSV file of restaurant inspection results, organizes the data by boroughs, and offers various tools for data visualization and export. 
## Features
- **Analyze Borough Trends**
  - Identify which borough has the most grade "A" restaurants.
- **Visualize Data with Charts**
  - Generate a pie chart showing the distribution of grade "A" restaurants across NYC boroughs.
- **Export Rating-Based Data**
  - Export a CSV file sorted by ratings, showing all restaurants and their grades.
- **Highlight Top-Rated Restaurants**
  - Export a list of the best restaurants (with perfect scores) for each borough.
- **Interactive Menu**
  - Navigate through various options to analyze and export data with ease.

## Tech Stack
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)

## Prerequisites

### For this only install **brew**, Install anything below **brew**, through **brew**.
- [brew](https://brew.sh/)
- [python](https://www.python.org)
  
### Install brew

```bash

bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

```

### Install Python

```bash
brew install python
```
### Check Python 3 and Pip Version
```bash
python3 --version
pip3 --version
```
---
## Setup
- Clone the repository:

```bash
git clone https://github.com/AleHS01/nyc-restaurant-analyzer.git
cd nyc-restaurant-analyzer.
```
- Since there’s no requirements.txt, you’ll need to install each dependency manually:
```bash
pip install pandas matplotlib tkinter
```
---
## Run the script
- Run the script directly using Python:
```bash
python main.py

```
