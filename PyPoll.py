#Determine winner of election and voter turnout
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


# Track the winning candidate, vote count, and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0


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


#save the results to text file
with open(file_to_save, "w") as txt_file:

    #Print the final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")

    print(election_results, end="")
    
    # After printing the final vote count to the terminal save the final vote count to the text file.
    #txt_file.write(election_results)
    
for candidate_name in candidate_votes:

    # Retrieve vote count and percentage.
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes) / float(total_votes) * 100
    candidate_results = (
        f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")


    # Print each candidate's voter count and percentage to the terminal.
    print(candidate_results)
    
    #  Save the candidate results to our text file.
    #txt_file.write(candidate_results)
    
    # Determine winning vote count, winning percentage, and winning candidate.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_candidate = candidate_name
        winning_percentage = vote_percentage


# Print the winning candidate's and highest county turnout results to the terminal.
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")

print(winning_candidate_summary)


# Save the winning candidate's results to the text file.
#txt_file.write(winning_candidate_summary)


#starts count at zero
total_votes = 0

#lists all countys
county_options = []

#declare empty dictionary
county_votes = {}

# Track the county with highest turnout, vote count, and percentage
winning_county = ""
winning_count = 0
winning_percentage = 0

#opens file
with open(file_to_load) as election_data:                           
    file_reader = csv.reader(election_data)

    # Reads header row.
    headers = next(file_reader)                                    

    #prints each row in file
    for row in file_reader:
        #adds to the total vote count                                         
        total_votes += 1
        
        #finds counties in each row
        county_name = row[1]

        # If the county does not match any existing county...
        if county_name not in county_options: 

            #add county to list as new one found
            county_options.append(county_name)

            #set countys starting vote to 0
            county_votes[county_name] = 0

        #add votes to total count
        county_votes[county_name] += 1

#save the results to text file
with open(file_to_save, "w") as txt_file:

    #Print the final vote count to the terminal
    voting_results = (
        f"\nCounty Turnout Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")

print(voting_results, end="")

# After printing the final vote count to the terminal save the final vote count to the text file.
#txt_file.write(voting_results)

for county_name in county_votes:

    # Retrieve vote count and percentage.
    votes = county_votes[county_name]
    vote_percentage = float(votes) / float(total_votes) * 100
    county_results = (
        f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n")


    # Print each county's voter count and percentage to the terminal.
    print(county_results)
    
    #  Save the county results to our text file.
    #txt_file.write(county_results)
    
    # Determine winning vote count, winning percentage, and winning county.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_county = county_name
        winning_percentage = vote_percentage

# Print the winning county's results to the terminal.
winning_county_summary = (
    f"-------------------------\n"
    f"County with highest turnout: {winning_county}\n"
    f"Vote Count of {winning_county} county: {winning_count:,}\n"
    f"Percentage of overall votes cast in {winning_county} county: {winning_percentage:.1f}%\n"
    f"-------------------------\n")

print(winning_county_summary)

# Save the winning county's results to the text file.
#txt_file.write(winning_county_summary)

with open(file_to_save, "w") as txt_file:
    txt_file.write(election_results)
    txt_file.write(candidate_results)
    txt_file.write(winning_candidate_summary)
    txt_file.write(voting_results)
    txt_file.write(county_results)
    txt_file.write(winning_county_summary)