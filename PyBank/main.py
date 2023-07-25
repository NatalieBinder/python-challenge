# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
import numpy as np

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

months_list=[]
print("Financial Analysis")
print("-----------------")

# Method 2: Improved Reading using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')



    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    first_row = next(csvreader)
    prev_row=int(first_row[1])
    total = prev_row
    change_list=[]
    greatest_increase = ["",-10000]
    greatest_decrease = ["",-10000]
    # Read each row of data after the header
    for row in csvreader:
        total += int(row[1])
        change=int(row[1])-prev_row
        change_list.append(change)
        months_list.append(row[0])
        prev_row=int(row[1])
        if change>greatest_increase[1]:
            greatest_increase[1]=change
            greatest_increase[0]=row[0]
        if change<greatest_decrease[1]:
            greatest_decrease[1]=change
            greatest_decrease[0]=row[0]
    avg = np.round(sum(change_list)/len(change_list),2)

outputpath = os.path.join('analysis', 'budget_analysis.txt')
with open(outputpath, "w") as outputfile:
    output1 = (f"Financial Analysis\n"
    f"-------------------------\n"
    f"Total Months: {len(months_list) + 1}\n"
    f"Total: ${total}\n"
    f"Average Change: ${avg}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
    )
    print(output1)
    outputfile.write(output1)
