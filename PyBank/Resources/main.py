import os
import csv


csvpath = os.path.join("..","PyBank","Resources","budget_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")



#Your task is to create a Python script that analyzes the records to calculate each of the following:

#* The total number of months included in the dataset

#* The net total amount of "Profit/Losses" over the entire period

#* The changes in "Profit/Losses" over the entire period, and then the average of those changes

#* The greatest increase in profits (date and amount) over the entire period

#* The greatest decrease in profits (date and amount) over the entire period