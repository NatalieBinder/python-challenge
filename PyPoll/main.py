# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
import numpy as np

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

results_list=[]

# Method 2: Improved Reading using CSV module
total_votes = 0
candidates = []
votes={}
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')



    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    for row in csvreader:
        total_votes = total_votes + 1 
        if row[2] not in candidates:
            candidates.append(row[2])
            votes[row[2]] = 0
        votes[row[2]] += 1
  
  
  
  
    #print("Total Votes:" + str(total_votes)) 
    #print(votes)
    res = {key:round( val / total_votes*100, 3) for key,val in votes.items()}
    #print (res)
    max_value = max(votes, key=votes.get)
    #print(max_value)
    
outputpath = os.path.join('analysis', 'election_analysis.txt')
with open(outputpath, "w") as outputfile:
    output1 = (f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n")

    print(output1)
    outputfile.write(output1)

    for k,v in votes.items():
        output2 = (f"{k}: {res[k]}% ({v})\n")
        print(output2)
        outputfile.write(output2)



    output3 = (f"-------------------------\n"
    f"Winner: {max_value}\n"
    f"-------------------------\n")

    print(output3)
    outputfile.write(output3)  
