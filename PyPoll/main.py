import os
import csv
output=("Election Results\n")
output+=("----------------------------\n")
#initialize
Ballot_ID=[]
County=[]
Candidate=[]
winner=""

# open csv file
filepath="/Users/16478/OneDrive/bootcamp/challenge-uploads/python-challenge/PyPoll/Resources/election_data.csv"
pollanalysis="/Users/16478/OneDrive/bootcamp/challenge-uploads/python-challenge/PyPoll/analysis/pollanalysis.txt"

with open(filepath,'r') as csvfile:
    myvote=csv.reader(csvfile,delimiter=',')
    next(myvote)
    
    candidates={}
    # create a set of candidate list
    for row in myvote:
        Ballot_ID.append(row[0])
        County.append(row[1])
        Candidate.append(row[2])
        # print(Candidate)  
        candidate_name = row[2]
        if candidate_name in candidates:
            candidates[candidate_name] += 1
        else:
            candidates[candidate_name] = 1
        # print(f"{candidates}: {candidate_name}")

    # total votes calculate
    total_votes=len(Ballot_ID)
    output+=(f"Total Votes: {total_votes}\n")

    output+=("----------------------------\n")
    for candidate,votes in candidates.items():
        percent = (votes/total_votes) * 100
        output+=(f"{candidate}:{percent:.3f}% ({votes})\n")
    output+=("----------------------------\n")    
    # winner of election    

    winner=max(candidates, key = lambda x:candidates[x])
    output+=(f"Winner: {winner}\n")

    #print(f"Winner:{winner}")
    output+=("----------------------------")

with open(pollanalysis,'w') as text_file:
    text_file.write(output)
    print(output)