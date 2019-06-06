#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import csv
election_data = os.path.join("..", "Resources", "election_data.csv")


# In[2]:


#set up my variables for counting all the votes
#setting up lists seems to make the most sense b/c there will be multiple candidates to track
candidates = []
total_votes = 0
vote_count = []


# In[3]:


#open and read file as csv
#skip the header
with open(election_data,newline="") as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvfile)

#loop through all the rows in the csv (format of data: voter id, county,candidate)
#add 1 to total_votes each time; len() could be alternative
#look @ list exercise from module lesson 3.1 -- can use .index to retrieve cand. name
#reference this: https://treyhunner.com/2016/04/how-to-loop-with-indexes-in-python/
    for row in csvreader:
        total_votes = total_votes + 1
        candidate = row[2]
        
        if candidate in candidates:
            cand_index = candidate.index(candidate)
            vote_count[cand_index] = vote_count[cand_index] + 1
        else:
            candidates.append(candidate)
            vote_count.append(1)


# In[33]:


#set up variables for getting voter %
#append percentages to list to keep track of each candidate
#round the percentages here or when I print the results...?
percentage = []
max_votes = vote_count[0]
max_index = 0

for votes in range(len(candidates)):
    vote_percentage = (vote_count[votes]/total_votes) * 100
    #vote_percentage = round(vote_percentage, 2)
    percentage.append(vote_percentage)
    
    if vote_count[votes] > max_votes:
        max_votes = vote_count[votes]
        print(max_votes)
        max_index = votes
        
winner = candidates[max_index]


# In[34]:


#print out all the results
#printing total votes will be tricky; 
# use f statements - don't do + concatenation
# use range(len()) again since I need the index
print("Election Results")
print("--------------------------")
print(f"Total Votes: {total_votes}")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {percentage[i]}% ({vote_count[i]})")
#for x in (candidates):
    #print(x)
print("---------------------------")
print(f"Winner: {winner}")
print("---------------------------")


# In[42]:


text_file = open("PyPoll_Output.txt", "w")
text_file.write(f"Election Results \n")
text_file.write(f"---------------")
text_file.write("\n")
text_file.write(f"Total Votes: {total_votes}")
text_file.write("\n")
for i in range(len(candidates)):
    text_file.write(f"{candidates[i]}: {percentage[i]}% ({vote_count[i]})")
text_file.write("\n")
text_file.write("---------------- \n")
text_file.write("\n")
text_file.write(f"Winner: {winner} \n")
text_file.write("----------------")


# In[ ]:




