import csv
import os




path = "/Users/Rebecca Levine/Desktop/python-challenge/"

csvpath = os.path.join(path, "PyPoll","Resources","election_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")

    header = next(csvreader) 

#Your task is to create a Python script that analyzes the votes and calculates each of the following:
#* The total number of votes cast
#* A complete list of candidates who received votes
#* The percentage of votes each candidate won
#* The total number of votes each candidate won
#* The winner of the election based on popular vote.

#Variables
votes =  {}
total_votes_cast = 0

most_votes_count = 0
most_votes_candidate = ""


for row in csvreader:
    number_of_votes = row[2]

    total_votes_cast = total_votes_cast + 1

    if number_of_votes in votes:
        votes[number_of_votes] = votes[number_of_votes] + 1
    else:
        votes[number_of_votes] = 1
        
        '''votes = {
            "Charles Casper Stockham"=3, 
            "Diana DeGette" =2, "Raymon Anthony Doane" =1}'''

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

