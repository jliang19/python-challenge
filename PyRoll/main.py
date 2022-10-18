import os, csv

election_data = os.path.join("election_data.csv")

# candidates names
candidates = []

#number of votes each candidate receives
votes_per = []

#percentage of votes each candidate receives
percent_votes = []

#total vote counts
total_votes = 0

#each candidate's vote counts
charles_total_votes = 0
diana_total_votes = 0
rayman_total_votes = 0

# Open csv in default read mode with context manager
with open("election_data.csv") as election_data:
    csvreader = csv.reader(election_data, delimiter = ",")
    csv_header = next(csvreader)

    for row in csvreader:
        # vote counter
        total_votes +=1

        
        #count the votes from each candidates
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            votes_per.append(1)
        else:
            index = candidates.index(row[2])
            votes_per[index] += 1
    
    #add to percent_votes
    for votes in  votes_per:
        percentage = (votes/total_votes)*100
        percentage = "%.3f%%" % percentage
        percent_votes.append(percentage)

    #find the winner
    most_votes = max(votes_per)
    index = votes_per.index(most_votes)
    winner= candidates[index]

# Printing results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {str(total_votes)}")
print("--------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(percent_votes[i])} ({str(votes_per[i])})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

#exporting files
output = open("analysis.txt", "w")
line1 = "Election Results"
line2 = "-------------------------"
line3 = str(f"Total Votes: {str(total_votes)}")
line4 = "-------------------------"
output.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))
for i in range(len(candidates)):
    line = str(f"{candidates[i]}: {str(percent_votes[i])} ({str(votes_per[i])})")
    output.write('{}\n'.format(line))
line5 = "-------------------------"
line6 = str(f"Winner: {winner}")
line7 = "-------------------------"
output.write('{}\n{}\n{}\n'.format(line5, line6, line7))
