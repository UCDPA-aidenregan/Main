# Finance Project
import numpy as np
import matplotlib as plt
# Notes for next steps
print("Begin of project, 18 April 2022")
print("GitHub is set up as UCDPA Aiden Regan")
# Project now set as Main.py on UCDPA Aiden Regan
import pandas as pd
Sales2018 = pd.read_csv(r"C:\Users\Sarah\Downloads\passengercars2018.csv")
Sales2019 = pd.read_csv(r"C:\Users\Sarah\Downloads\passengercars 2019.csv")
# Plug in needed for csv read
print('The dimensions of these data sets are: ')
print(Sales2019.shape)
print(Sales2018.shape)
print("Sample of typical data: ")
print(Sales2019.head())
print(Sales2018.head())
print("Indexing of the data: ")
print(Sales2019.index)
print(Sales2018.index)
print('Here is a summary analysis of the sets including their size: ')
print(Sales2019.info())
print(Sales2018.info())
print("Sorting values by Engine Type & Count of Sales :")
print(Sales2019.sort_values(["Engine type", "Car registration count"]))
Green19 = Sales2019[(Sales2019["Engine type"] == "Electric") | (Sales2019["Engine type"] == "Hybrid")]
print(Sales2018.sort_values(["Engine type", "Car registration count"]))
Green18 = Sales2018[(Sales2018["Engine type"] == "Electric") | (Sales2018["Engine type"] == "Hybrid")]
print("Subsetting to Eco Friendly Cars: ")
print(Green19.head())
print(Green18.head())
print("Grouping the data for initial review: ")
Totals19 = Sales2019.groupby("Engine type")["Car registration count"].agg([min, max, sum])
Overall19= Sales2019["Car registration count"].agg(sum)
print(Totals19)
print(Overall19)
Totals18 = Sales2018.groupby("Engine type")["Car registration count"].agg([min, max, sum])
Overall18= Sales2019["Car registration count"].agg(sum)
print(Totals18)
print(Totals18)
# Use of Numpy and Pivot functions to explore the data
print("Pivot table for a deeper analysis of each County's habits 2019")
print(Sales2019.pivot_table(values="Car registration count", index = "County", columns = "Engine type", aggfunc=[np.sum, np.median] fill_value=0, margins=True))
print("Pivot table for a deeper analysis of each County's habits 2018")
print(Sales2018.pivot_table(values="Car registration count", index = "County", columns = "Engine type", aggfunc=[np.sum, np.median] , fill_value=0, margins=True))













