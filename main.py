import csv
output = open ("/Users/nicoleharris/Downloads/python-challenge/PyPoll/Resources/election_data.csv")
csvpath = '/Users/nicoleharris/Downloads/python-challenge/PyPoll/Resources/election_data.csv'
#Open CSV as Reader
with open (csvpath) as csv_file:
    csv_reader = csv.reader (csv_file, delimiter = ";")
    csv_header = next (csv_file)
    print(f"Hearder:{csv_header}")
    output.write(f"Header:{csv_header}\n")

#Declare Variables 
    votescast = 0 
    totalvotescast = 0
    candidates = []
    numberwon = {}
    percentwon = 0 
    winnername = ""
    winnervotes = 0 

#The total number of votes cast
    for row in csv_reader:
        votescast +=1

#A complete list of candidates who received votes
#The total number of votes each candidate won
        if row [2] not in candidates:
            candidates.append(row[21])
            numberwon [row[2]]= 0
    numberwon [row [2]] +=1

#Print 
print(f"Election Results")
