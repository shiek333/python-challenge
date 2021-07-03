'''
Import libraries and Open File
'''
import os
import csv

csvpath = os.path.join("PyPoll/Resources","election_data.csv")

with open(csvpath) as csvfile:
    election = csv.reader(csvfile, delimiter=',')
    header = next(election)
    next(election)
    ID = []
    county = []
    candidate = []
    votedCandidates = []
    candidateVotes = []
    candidateVotesPercent = []

    #Save Data to Lists
    for row in election:
        ID.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

    #Analyze Election Data
    TotalVotes = len(ID)
    for row in candidate:
        if row not in votedCandidates:
            votedCandidates.append(row)       
    def votes(CandidateName):
        total = 0 
        for row in candidate:
            if row == CandidateName:
                total += 1
        return total
    for name in votedCandidates:
        candidateVotes.append(votes(name))
    for vote_amount in candidateVotes:
        votePercent = '{:.3f}'.format(float(vote_amount/TotalVotes)*100)
        candidateVotesPercent.append(votePercent)
    candidate_dict = {"name":votedCandidates,"votePercent":candidateVotesPercent,"votes":candidateVotes}
    sorted(candidate_dict, key=lambda x: x[2], reverse=True)
    
    #Print Election Analysis Summary Table
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {TotalVotes}")
    print("-------------------------")
    for n in range(len(votedCandidates)):
        print(f"{candidate_dict['name'][n]}: {candidate_dict['votePercent'][n]}% ({candidate_dict['votes'][n]})")
    print("-------------------------")
    print(f"Winner: {candidate_dict['name'][0]}")
    print("-------------------------")

'''
Export to Text File
''' 
output_path = os.path.join("PyPoll/Analysis","PyPoll_Analysis.txt")

with open(output_path, 'w') as text:
    text.write("Election Results" + "\n")
    text.write("-------------------------" + "\n")
    text.write(f"Total Votes: {TotalVotes}" + "\n")
    text.write("-------------------------" + "\n")
    for n in range(len(votedCandidates)):
        text.write(f"{candidate_dict['name'][n]}: {candidate_dict['votePercent'][n]}% ({candidate_dict['votes'][n]})" + "\n")
    text.write("-------------------------" + "\n")
    text.write(f"Winner: {candidate_dict['name'][0]}" + "\n")
    text.write("-------------------------" + "\n")
    