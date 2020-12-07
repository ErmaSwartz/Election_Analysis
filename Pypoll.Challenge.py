# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

total_votes = 0 
# initialize a county list 
County_list= []
#initialize a dictionary for voters per county 
County_votes = {} 
# initialize an empty string that will hold the county name for the county with the largest turnout 
best_county_turnout = ""
winning_count= 0
winning_percentage = 0
# initialize a variable that will hold the number of votes of the county that has the largest turnout 
best_county_turnout_12 = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    #write a script that get the county name inside a for loop 
    headers = next(file_reader)
    for row in file_reader:
        # Get the county name 
        county_name = row[1]
        # Add to the total vote count.
        total_votes += 1
        #Decision statement to check if the county name is acquired 
        if county_name not in County_list: 
            #if the county is not in the list, add it to the list of county names 
            County_list.append(county_name)
            #write a script that initialized the county vote to zero 
            County_votes[county_name] = 0 
            #write a script that add a vote to the county's vout count 
        County_votes[county_name] += 1 
        #write a repition statment to get the county from the county dictionary 
    print("Election Results")
    print("Total Votes: 369,711")
    print("County Votes:")
for county_name in County_votes:
    #intialize a variable to hold the county's votes as they are retrieved from the county votes dictionary 
    votes = County_votes[county_name]
    # write a script that calculates the county's votes as a percentage of the total votes 
    county_votes_percentage = float(votes)/ float(total_votes) * 100
    print(f"{county_name}: {county_votes_percentage:.1f}% ({votes:,})\n")

    ## # Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)
    for county_name in County_votes:
        # Retrieve vote count and percentage.
        votes = County_votes[county_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        county_results = (
            f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n")
# Print each candidate's voter count and percentage to the terminal.
        print(county_results)
        #  Save the candidate results to our text file.
        txt_file.write(county_results)
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_county = county_name
            winning_percentage = vote_percentage
    # Print the winning candidate's results to the terminal.
    winning_county_summary = (
        f"-------------------------\n"
        f"County with the Highest Turnout: {winning_county}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_county_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_county_summary)
 # Print each county's voter count and percentage to the terminal.
    print(county_results)
     #  Save the results to our text file.
    txt_file.write(county_results)
        # Determine winning vote count, winning percentage, and winning county.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_county = county_name
        winning_percentage = vote_percentage
    ## write a decision statemnet that determines the county with the largest vote count 
    print ("Largest County Turnout:")
    if (votes > winning_count) and (county_votes_percentage > winning_percentage):
        winning_count = votes
        winning_county = county_name
        winning_percentage = county_votes_percentage
   
   # Write a print statement that prints out the county with largest turnout 
        winning_county_summary = (
        f"-------------------------\n"
        f"County: {winning_county}\n"
        f"Amount of Votes: {winning_count:,}\n"
        f"Percentage of Votes: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize a total vote counter.
total_votes = 0
# Candidate options and candidate votes.
candidate_options = []
candidate_votes = {}
# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Get the candidate name from each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate, add the
        # the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Save the results to our text file.
with open(file_to_save, "a") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)
    for candidate_name in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)