#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import csv
election_data = os.path.join("..", "Resources", "election_data.csv")


# In[2]:


candidates = []
num_votes = 0
vote_counts = []


# In[3]:


with open(election_data,newline="") as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvfile)
    
    for row in csvreader:
        num_votes = num_votes + 1
        candidate = row[2]
        
        if candidate in candidates:
            candidate_index = candidate.index(candidate)
            vote_counts[candidate_index] = vote_counts[candidate_index] + 1
        else:
            candidates.append(candidate)
            vote_counts.append(1)


# In[4]:


percentage = []
max_votes = vote_counts[0]
max_index = 0

for count in range(len(candidates)):
    vote_percentage = vote_counts[count]/num_votes*100
    percentage.append(vote_percentage)
    
    if vote_counts[count] > max_votes:
        max_votes = vote_counts[count]
        print(max_votes)
        max_index = count
        
winner = candidates[max_index]


# In[5]:


print("Election Results")
print("--------------------------")
print(f"Total Votes: {num_votes}")
for count in range(len(candidates)):
    print(f"{candidates[count]}: {percentage[count]}% ({vote_counts[count]})")
print("---------------------------")
print(f"Winner: {winner}")
print("---------------------------")


# In[ ]:




