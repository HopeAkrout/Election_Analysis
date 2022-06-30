#Determine winner of election
# Add our dependencies.
import csv
import os


# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assigns a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")





#starts count at zero
total_votes = 0

#lists all candidates
candidate_options = []

#declare empty dictionary
candidate_votes = {}

#opens file
with open(file_to_load) as election_data:                           
    file_reader = csv.reader(election_data)

    
    # Reads header row.
    headers = next(file_reader)                                    

    #prints each row in file
    for row in file_reader:
        #adds to the total vote count                                         
        total_votes += 1

        
        #finds candidates in each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options: 

            #add candidate to list as new one found
            candidate_options.append(candidate_name)

            #set candidates starting vote to 0
            candidate_votes[candidate_name] = 0

        #add votes to total count
        candidate_votes[candidate_name] += 1

#Prints list of candidates
print(candidate_votes)

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Determine the percentage of votes for each candidate by looping through the counts.
# Iterate through the candidate list.
for candidate_name in candidate_votes:
    # Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100

    #  To do: print out each candidate's name, vote count, and percentage of
    # votes to the terminal.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent =
         # vote_percentage.
         winning_count = votes
         winning_percentage = vote_percentage
         # And, set the winning_candidate equal to the candidate's name.
         winning_candidate = candidate_name

#  To do: print out the winning candidate, vote count and percentage to
#   terminal.
winning_candidate_summary = (
    f"----------------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"----------------------------------\n")

#print name and percentage
print(winning_candidate_summary)