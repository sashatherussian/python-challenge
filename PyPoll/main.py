import csv
row_count=0

with open('PyPoll/Resources/election_data.csv','r') as my_data2:
    reader=csv.reader(my_data2)
    header=next(reader)
    
    first_row=next(reader)
    row_count+=1
    candidates_list=[]

    for row in reader:
            
        candidate=row[2]
        
        if candidate not in candidates_list:
            candidates_list.append(candidate)
        
    

        row_count+=1

print(row_count)
print(candidates_list)

with open('PyPoll/Resources/analysis.txt','w') as txt_file:

    txt_file.write(f'Total Votes : {row_count}\n')