import os 
import csv

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
outfile = open(file_to_save, "w")
# Write three counties to the file.
outfile.write("Counties in the election\n")
outfile.write("Arapahoe \n")
outfile.write("Denver \n")
outfile.write("Jefferson")

# Close the file
outfile.close()
