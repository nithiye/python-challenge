# The dataset is composed of three columns: Voter ID, County, and Candidate. 
#Your task is to create a Python script that analyzes the votes and calculates each of the following:


import os
import csv

#csvpath
election_path_csv = os.path.join('..','03-PYTHON','Instructions','PyPoll','Resources','election_data.csv')
total_votes = 0
candidates = []
vote_counts = []

percentages = []
max_votes = vote_counts
max_index = 0

with open(election_path_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)  

    for row in csvreader:
        # The total number of votes cast
        total_votes = total_votes + 1
       
        # A complete list of candidates who received votes 
        candidate = row[2] 
        if candidate in candidates:
           candidate_index = candidates.index(candidate)
           vote_counts[candidate_index] = vote_counts[candidate_index] + 1
        else:
            candidates.append(candidate)
            vote_counts.append(1)
    
    # The percentage of votes each candidate won
    for count in range(len(candidates)):
        vote_percentage = round(vote_counts[count]/total_votes*100)
        percentages.append(vote_percentage)

        # The total number of votes each candidate won  
        if vote_counts > max_votes:
            max_votes = vote_counts[count]
            max_index = count
   # The winner of the election based on popular vote.
    winner = candidates[max_index]

    results = f"Election Results:\n\
    Total Votes: {total_votes}\n\
    Total Candidates: {candidates:}, {percentages:}%, {vote_counts}\n\
    Winner: {winner}"
    
    print(results)
    print(results,file = open('election.txt','a'))