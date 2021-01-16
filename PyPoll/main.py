import csv
import os
import collections
from collections import Counter

row_count=0
candidates_list=[]
candidate_votes=[]

with open('PyPoll/Resources/election_data.csv','r') as my_data2:
    reader=csv.reader(my_data2)
    header=next(reader)
    
    first_row=next(reader)

    for row in reader:    
        candidate_votes.append(row[2])
        if row[2] not in candidates_list:
            candidates_list.append(row[2])
              
Total_votes = (len(candidate_votes))

Votes_tally = Counter(candidate_votes)
print(Votes_tally)

votes_winner = Votes_tally.most_common()
Votes_tally.most_common(1)[0][0]
print(votes_winner)

Khan_votes = Votes_tally['Khan']
Correy_votes = Votes_tally['Correy']
Li_votes = Votes_tally['Li']
OTooley_votes = Votes_tally["O'Tooley"]

        
print('-----------------------------------------------------')
print('Election Results')
print('Candidates:', candidates_list)
print('-----------------------------------------------------')
print('Total Votes=','{:,}'.format(Total_votes))
print('-----------------------------------------------------')
print('Votes for Khan =', '{:,}'.format(Votes_tally['Khan']), "Percent of Votes:",'{:.2f}'.format(Khan_votes/Total_votes*100),'%')
print('Votes for Correy =', '{:,}'.format(Votes_tally['Correy']), "Percent of Votes:",'{:.2f}'.format(Correy_votes/Total_votes*100),'%')
print('Votes for Li =', '{:,}'.format(Votes_tally['Li']), "Percent of Votes:",'{:.2f}'.format(Li_votes/Total_votes*100),'%')
print("Votes for O'Tooley =", '{:,}'.format(Votes_tally["O'Tooley"]), "Percent of Votes:",'{:.2f}'.format(OTooley_votes/Total_votes*100),'%')

with open('PyPoll/Resources/election_results.txt','w') as txt_file:
    txt_file.write("Election Results" + "\n" + "--------------------------" + "\n" + "Total Votes =" + str(Total_votes)+ "\n")
    txt_file.write("--------------------------"+ "\n")
    txt_file.write("Votes for Khan =" + str(Khan_votes) + "Percent Votes="+ str(Khan_votes/Total_votes*100) + "%" + "\n")
    txt_file.write("Votes for Correy =" + str(Correy_votes) + "Percent Votes="+ str(Correy_votes/Total_votes*100) + "%" + "\n")
    txt_file.write("Votes for Li =" + str(Li_votes) + "Percent Votes="+ str(Li_votes/Total_votes*100) + "%" + "\n")
    txt_file.write("Votes for O'Tooley =" + str(OTooley_votes) + "Percent Votes="+ str(OTooley_votes/Total_votes*100) + "%" + "\n")
    txt_file.write("Election Winner =  " + str(votes_winner) + "\n")
    txt_file.write("--------------------------"+ "\n")
   