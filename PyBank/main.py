import os
import csv

budgetdata_csv = os.path.join("C:\\Users\\winst\\Desktop\\python-challenge", "budget_data.csv")

with open(budgetdata_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvfile)

    months = 0
    total = 0
    prev_rev = 0
    total_change = 0
    rev_change = 0
    max_profit = 0
    max_loss = 0
    avg_change = 0

    for row in csvreader:

        months = months + 1
        total = total + int(row[1])
        #average revenue change
        rev_change = int(row[1]) - prev_rev
        total_change = total_change + rev_change
        prev_rev = int(row[1])
        #greatest profit increase
        if(rev_change > max_profit):
            max_profit = rev_change
            max_profit_date = row[0]
        #greatest profit decrease 
        if(rev_change < max_loss):
            max_loss = rev_change
            max_loss_date = row[0]   

        avg_change = total_change / months

print(f"Total Months: {months}")
print(f"Total Profit: ${total}")
print(f"Average Change over Time: ${round(avg_change,2)}")
print(f"Greatest Increase in Profits: ${max_profit} during {max_profit_date}")
print(f"Greatest Decrease in Losses: ${max_loss} during {max_loss_date}")

#I struggled a bit with the logic on calculating average change over time. I tried referencing stackoverflow /
#for inspiration but had a hard time filtering through code that was using pandas or numby modules


