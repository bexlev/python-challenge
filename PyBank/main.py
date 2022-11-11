#import dependencies

import csv
import os



#Set Variables
total_months = 0
month_of_change = []
net_change_list =[]
Greatest_Profit_Increase = ["",0]
Greatest_Profit_Decrease = ["",99999999999999999999]
total_net = 0

#read csv file

path = "/Users/Rebecca Levine/Desktop/python-challenge/"

csvpath = os.path.join(path, "PyBank","Resources","budget_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    header = next(csvreader) 

    first_row = next(reader)
    total_months += 1
    total_net += int(first_row[1])
    prev_net = int(first_row[1])

        #min
for row in csvreader:
    total_months += 1
    total_net += int(row[1])

        #net change
    net_change = int(row[1]) - prev_net
    prev_net = int(row[1])
    net_change_list += [net_change]
    month_of_change += [row[0]]

        #greatest increase
    if net_change > greatest_increase[1]:
        greatest_increase[0] = row[0]
        greatest_increase[1] = net_change

        #greatest decrease
    if net_change < greatest_decrease[1]:
        greatest_decrease[0] = row[0]
        greatest_decrease[1] = net_change

# Calculate the Average Net Change
    net_monthly_avg = sum(net_change_list) / len(net_change_list)    
    

    if number_of_votes in votes:
        votes[number_of_votes] = votes[number_of_votes] + 1
    else:
        votes[number_of_votes] = 1
        
        '''votes = {
            "Charles Casper Stockham"=3, 
            "Diana DeGette" =2, "Raymon Anthony Doane" =1}'''

#print results in text file

with open ("analysis.txt", "w") as txt_file:
    output = "votes\n-----"
    print(output)
    txt_file.write(output + '\n')
    for key, value in votes.items():

        if value > most_vote_count:
            most_vote_count = key
            most_vote_count = value
            output = key + ":" + str(value)
            print(output)
            txt_file.write(output + '\n')
        
        print('\nmost_vote:')
        txt_file.write('\nmost_vote:')
        output = most_votes_candidate + "" + str(most_vote_count)
        print(output)
        txt_file.write(output)

