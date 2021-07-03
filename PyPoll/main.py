'''
Import libraries, Open File, and Analysis
'''
# Import Libraries
import os
import csv

# Directory Path to Election Data
csvpath = os.path.join("PyPoll/Resources","election_data.csv")

# Open File and Create Empty List Variables to Store Data
with open(csvpath) as csvfile:
    election = csv.reader(csvfile, delimiter=',')
    header = next(election)
    ID = []
    county = []
    candidate = []
    votedCandidates = []
    candidateVotes = []
    candidateVotesPercent = []

    # Save Data to Lists
    for row in election:
        ID.append(row[0])
        county.append(row[1])
        candidate.append(row[2])


    ### Election Data Analysis for Total Votes, List of Candidates with Votes, Candidate Vote Percentages, Candidate Total Votes, and Election Winner
    def votes(CandidateName):
        """
        Calculate the total amount of votes depending on the candidate's name inputted to the function 
        """
        total = 0 
        for row in candidate:
            if row == CandidateName:
                total += 1
        return total
    def voted_candidate():
        """
        Unique list of Candidates with votes
        """
        for row in candidate: 
            if row not in votedCandidates:
                votedCandidates.append(row)
        return votedCandidates  
    def vote_percent():
        """
        List of the vote percent for each candidate with a 3 decimal format
        """
        for vote_amount in candidateVotes: 
            votePercent = '{:.3f}'.format(float(vote_amount/TotalVotes)*100)
            candidateVotesPercent.append(votePercent)
        return candidateVotesPercent
    def candidate_votes():
        """
        List of the total votes for each candidate
        """
        for name in votedCandidates: 
            candidateVotes.append(votes(name))
        return candidateVotes

    TotalVotes = len(ID)
    voted_candidate(), vote_percent(), candidate_votes() #Call the voted candidates, vote percent, and candidate vote functions to create lists
    candidate_dict = {"name":voted_candidate(),"votePercent":vote_percent(),"votes":candidate_votes()} #Create a dictionary of the candidate names, candidate vote percentages, and candidate total votes
    sorted(candidate_dict, key=lambda x: x[2], reverse=True) #Sort candidate dictionary by largest total votes
    electionWinner = candidate_dict['name'][0]
    

    ### Print Election Analysis Summary Table
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {TotalVotes}")
    print("-------------------------")
    for n in range(len(votedCandidates)):
        print(f"{candidate_dict['name'][n]}: {candidate_dict['votePercent'][n]}% ({candidate_dict['votes'][n]})")
    print("-------------------------")
    print(f"Winner: {electionWinner}")
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
    