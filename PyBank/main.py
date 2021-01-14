import csv
row_count=0
total_sum=0
total_change=0
largest_increase=0
largest_decrease=0
with open('PyBank/Resources/budget_data.csv','r') as my_data:
    reader=csv.reader(my_data)
    header=next(reader)
    
    first_row=next(reader)
    last_month_value=first_row[1]
    row_count+=1
    total_sum+=int(first_row[1])

    for row in reader:
        monthly_change=int(row[1])-int(last_month_value)
        total_change += monthly_change
        average_change=total_change/row_count    
        largest_increase=max(largest_increase,monthly_change)
        largest_decrease=min(largest_decrease,monthly_change)

        row_count+=1
        total_sum+=int(row[1])
        last_month_value=int(row[1])

print(row_count)
print(total_sum)
print(average_change)
print(largest_increase)
print(largest_decrease)

with open('PyBank/Resources/analysis.txt','w') as txt_file:

    txt_file.write(f'Total Months : {row_count}\n')
    txt_file.write(f'Total : {total_sum}\n')
    txt_file.write(f'Average Change: {average_change}\n')
    txt_file.write(f'Greatest Increase in Profits : {largest_increase}\n')
    txt_file.write(f'Greatest Decrease in Profits : {largest_decrease}\n')

