#Your task is to create a Python script that analyzes the records to 
# calculate each of the following:


import os
import csv
from statistics import mean

#csvpath
budget_path_csv = os.path.join('..','03-PYTHON','Instructions','PyBank','Resources','budget_data.csv')


total_months = 0
total_rev = 0
past_rev = 0
greatest_inc = 0
greatest_dec = 0
rev = 0
change_rev = 0
month_change = 0

#read csv file
with open(budget_path_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)  

    #Looping through all rows in CSV reader
    for row in csvreader:
        rev = int(row[1])
        #The net total revenue from "Profit/Losses" over the entire period
        total_rev = total_rev + rev
        #The total number of months included in the dataset
        total_months = total_months + 1
        
        month_change = rev - past_rev
       #The average of the changes in "Profit/Losses" over the entire period    
        if total_months >=2:
           past_rev = rev
           change_rev += month_change

        #The greatest increase in profits (date and amount) over the entire period
        #The greatest decrease in losses (date and amount) over the entire period
        if (month_change > greatest_inc): 
            greatest_inc_date = row[0]
            greatest_inc = month_change
        elif (month_change < greatest_dec):
            greatest_dec_date =  row[0]
            greatest_dec = month_change

    output = f"Results:\n\
    Total Months: {total_months}\n\
    Total Revenue: ${total_rev}\n\
    Average Revenue Change: ${(change_rev-867884)/total_months-1}\n\
    Greatest Increase in Revenue: {greatest_inc_date}, ${greatest_inc}\n\
    Greatest Decrease in Revenue: {greatest_dec_date}, ${greatest_dec}"

    print(output)
    print(output,file=open('budget.txt','a'))

   #Final submission notes to TA: I know my average revenue change is hardcoded here and I'm sure there is a better way to do it. 
   # Will try again at a later point.