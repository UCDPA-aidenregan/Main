# 1. Finance Project looking at Car Sales in Ireland
import numpy as np
import matplotlib.pyplot as plt
# Notes for next steps
print("Begin of project, 18 April 2022")
print("GitHub is set up as UCDPA Aiden Regan")
# Project now set as Main.py on UCDPA Aiden Regan
import pandas as pd
# 2. Import of data via csv file from source on Kaggle
Sales2018 = pd.read_csv(r"C:\Users\Sarah\Downloads\passengercars2018.csv")
Sales2019 = pd.read_csv(r"C:\Users\Sarah\Downloads\passengercars 2019.csv")
VRT = pd.read_csv(r"C:\Users\Sarah\Downloads\vehicle-registration.csv")
# Plug in needed for csv read, import was successful
# 3. a. Sorting, Indexing, Grouping and Initial review of the set below
print('The dimensions of these data sets are: ')
print(VRT.shape)
print(Sales2019.shape)
print(Sales2018.shape)
print("Sample of typical data: ")
print(VRT.head())
print(Sales2019.head())
print(Sales2018.head())
print("Indexing of the data: ")
print(VRT.index)
print(Sales2019.index)
print(Sales2018.index)
print(VRT.columns)
print(Sales2019.columns)
print(Sales2018.columns)
# 4. c Using Dictionary or Lists to remove a Column
ColNA = ["Registration type"]
Sales2019.drop(columns=ColNA, axis=1, inplace=True)
Sales2018.drop(columns=ColNA, axis=1, inplace=True)
# Check this worked
print(Sales2019.columns)
print(Sales2018.columns)
#
print("Setting the Engine Type as the index")
Sales2019Eco=Sales2019.set_index("Engine type")
print(Sales2019Eco)
print('Here is a summary analysis of the sets including their size: ')
print(Sales2019.info())
print(Sales2018.info())
print("Sorting values by Engine Type & Count of Sales :")
print(Sales2019.sort_values(["Engine type", "Car registration count"], ascending=False))
Green19 = Sales2019[(Sales2019["Engine type"] == "Electric") | (Sales2019["Engine type"] == "Hybrid")]
print(Sales2018.sort_values(["Engine type", "Car registration count"], ascending=False))
Green18 = Sales2018[(Sales2018["Engine type"] == "Electric") | (Sales2018["Engine type"] == "Hybrid")]
print("Subsetting to Eco Friendly Cars: ")
print(Green19.head())
print(Green18.head())
print("Grouping the data for initial review 2019: ")
# 2019 Analysis first
Totals19 = Sales2019.groupby("Engine type")["Car registration count"].agg([min, max, sum])
Overall19= Sales2019["Car registration count"].agg(sum)
print(Totals19)
print("Total Car Sold in 2019:")
print(Overall19)
# Space
print("Grouping the data for initial review 2018: ")
# 2018 Analysis second
Totals18 = Sales2018.groupby("Engine type")["Car registration count"].agg([min, max, sum])
Overall18= Sales2018["Car registration count"].agg(sum)
print(Totals18)
print("Total Cars Sold in 2018")
print(Overall18)
# Analsys on trends in sales
print("Percentage growth in overall sales numbers - number of cars sold: ")
percentagetotalincrease = (((Overall19-Overall18)/Overall18)*100)
print(percentagetotalincrease)
#Now to look at the main finacial data of the VRT figures
TaxReceipt=VRT["vehicle_receipts_€"]
print("Mean of VRT Receipt = ", TaxReceipt.mean())
print("Median of VRT Receipts = ", TaxReceipt.median())
print("Mode of VRT Receipts =", TaxReceipt.mode())
#
# 4.b Use of Numpy and Pivot functions to explore the data
print("Pivot table for a deeper analysis of each County's habits 2019:")
print(Sales2019.pivot_table(values="Car registration count", index="County", columns="Engine type", aggfunc=[np.sum, np.median], fill_value=0, margins=True))
print("Summary by type")
Visial1=Sales2019.pivot_table(values="Car registration count", index="Engine type", columns="Year", aggfunc=(np.sum), fill_value=0, margins=True)
print(Visial1)
# Visualisation of the data
print("Pivot table for a deeper analysis of each County's habits 2018:")
print(Sales2018.pivot_table(values="Car registration count", index = "County", columns = "Engine type", aggfunc=[np.sum, np.median], fill_value=0, margins=True))


















