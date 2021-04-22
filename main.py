# Finance Project
import numpy as np
import matplotlib as plt
# Notes for next steps
print("Begin of project, 18 April 2022")
print("The code is sent to github")
# Project now set as Main.py on UCDPA Aiden Regan
import pandas as pd
Sales2018 = pd.read_csv(r"C:\Users\Sarah\Downloads\passengercars2018.csv")
# Plug in needed for csv read
print(Sales2018.head())
print(Sales2018.shape)
missing_values_count = Sales2018.isnull().sum
print(missing_values_count)
