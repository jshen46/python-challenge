import os
import csv
output=("Financial Analysis\n")

output+=("-------------------------------------\n")

date=[]
profit_losses=[]
change_value=[]
# create path to open csvfile
filepath=("/Users/16478/OneDrive/bootcamp/challenge-uploads/python-challenge/PyBank/Resources/budget_data.csv")
myanalysis=("/Users/16478/OneDrive/bootcamp/challenge-uploads/python-challenge/PyBank/analysis/myanalysis.txt")
#filepath=("python-challenge/PyBank/Resources/budget_data.csv")
with open(filepath, 'r') as csvfile:
    mybudget=csv.reader(csvfile,delimiter=",")

    pre_value = 0
    # Populate all items 
    next(mybudget)
    for row in mybudget:
        date.append(row[0])
        profit_losses.append(int(row[1]))
        # changes of the value period is the difference between current period and previous period
        change_valPeriod = int(row[1]) - pre_value
    
        change_value.append(change_valPeriod)
        pre_value = int(row[1])
    # Calculate all date rows 
    Total_number = len(date)
    output+=(f"Total Months: {Total_number}\n")
    # Calculate all profit_losses
    Total = sum(profit_losses)
    output+= (f"Total: ${Total}\n")
    # Calculate average change
    Average_change = (profit_losses[len(date)-1] - profit_losses[0])/(len(date)-1)
    output+= ('Average Change: ${0:.2f}'.format(Average_change))
    # greatest increase and decrease
    max_val = max(change_value)
    index = change_value.index(max_val)
    output+= (f"\nGreatest Increase in Profits: {date[index]} (${max_val})\n")
    min_val = min(change_value)
    index = change_value.index(min_val)
    output+= (f"Greatest Decrease in Profits: {date[index]} (${min_val})\n")

with open(myanalysis,"w") as text_file:
    text_file.write(output)

    print(output)