#Code for PyPoll

import os
import csv

#Setting csv path
election_csv = os.path.join("Resources", "election_data.csv")

#Print title of new document
print("Election Results")
print("----------------")

#Show the total number of votes
with open(election_csv) as csvfile:
    
    #Set csvfile to be read as 'dict'
    csvreader = csv.DictReader(csvfile)
    
    #Create empty list for amount of votes
    vdata = {}
    
    #Begin loop to fetch votes data
    for row in csvreader:
        
        #Reads over and copies all data past the 'header'
        for header, value in row.items():
            try:
                vdata[header].append(value)
            except KeyError:
                vdata[header] = [value]
                
#Sets the range for the data that the 
#previous loop will copy over    
votes = vdata["Candidate"]

#Print the total number of votes in "Candidate" column
print("Total Votes: " + str(len(votes)))
print("----------------")

#Find candidates in list and assign each one to a variable
candidates = list(set(votes))
c1 = (candidates[0])
c2 = (candidates[1])
c3 = (candidates[2])

#Count the number of votes each candidate has
#and assign those values to variables
c1votes = votes.count(c1)
c2votes = votes.count(c2)
c3votes = votes.count(c3)

#Find the percentage of the total number of
#votes each candidate holds
c1voteperc = round(c1votes/len(votes) * 100, 3)
c2voteperc = round(c2votes/len(votes) * 100, 3)
c3voteperc = round(c3votes/len(votes) * 100, 3)

#Print: Candidate name, vote percentage, vote count
print(c1 + ": " + str(c1voteperc) + "% " + "(" +
      str(c1votes) + ")")
print(c2 + ": " + str(c2voteperc) + "% " + "(" +
      str(c2votes) + ")")
print(c3 + ": " + str(c3voteperc) + "% " + "(" +
      str(c3votes) + ")")
print("----------------")

#Create a list of vote counts for each candidate
candidatestanding = [c1votes, c2votes, c3votes]

#Assign the highest value in votes list to a variable
mostvotes = max(candidatestanding)

#Go through list and find out which candidate
#won the election and print their name
if c1votes == mostvotes:
    print("Winner: " + c1)
if c2votes == mostvotes:
    print("Winner: " + c2)
if c3votes == mostvotes:
    print("Winner: " + c3)    
print("----------------")

#Print results in newly created .txt file
import sys
file = open(os.path.join("Analysis", "analysis.txt"), 'w')
sys.stdout = file
print("Election Results")
print("----------------")
print("Total Votes: " + str(len(votes)))
print("----------------")   
print(c1 + ": " + str(c1voteperc) + "% " + "(" +
      str(c1votes) + ")")
print(c2 + ": " + str(c2voteperc) + "% " + "(" +
      str(c2votes) + ")")
print(c3 + ": " + str(c3voteperc) + "% " + "(" +
      str(c3votes) + ")")
print("----------------")
if c1votes == mostvotes:
    print("Winner: " + c1)
if c2votes == mostvotes:
    print("Winner: " + c2)
if c3votes == mostvotes:
    print("Winner: " + c3)    
print("----------------")
file.close()
sys.stdout = sys.__stdout__