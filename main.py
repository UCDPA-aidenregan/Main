# Finance Project
import numpy as np
import matplotlib as plt
import pandas as pd

# Notes for next steps
print("Begin of project, 18 April 2022")
print("sent draft to github attempt two")
# Project now set as Main.py on UCDPA Aiden Regan
Sales2018 = pd.read.csv(r"C:\Users\Sarah\Downloads\passengercars2018.csv")
# Plug in needed for csv read
print(Sales2018.head())
missing_values_count = Sales2018.isnull().sum
print(missing_values_count[0:5])
