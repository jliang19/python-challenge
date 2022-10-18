# Import Dependencies
import os, csv

budget_data = os.path.join("budget_data.csv")

# Create empty lists to iterate
total_months = []
total_profits = []
monthly_profits_change = []
 
# Open csv in default read mode
with open("budget_data.csv") as budget_data:

     # Store the contents of budget_data.csv in the variable csvreader
    csvreader = csv.reader(budget_data,delimiter=",") 

    # Skip the header labels to iterate with the values
    header = next(csvreader)  

    # Iterate through the rows
    for row in csvreader: 

        # Count the total months as total profits
        total_months.append(row[0])
        total_profits.append(int(row[1]))

    # Iterate through the profits to get monthly+profits_change
    for i in range(len(total_profits)-1):
        
        # Take the difference between two months and append to monthly profit change
        monthly_profits_change.append(total_profits[i+1]-total_profits[i])
        
# Calculate the greatest increase and greatest decrease in monthly_profits_chaneg
greatest_increase_value = max(monthly_profits_change)
greatest_decrease_value = min(monthly_profits_change)

greatest_increase_month = monthly_profits_change.index(max(monthly_profits_change)) + 1
greatest_decrease_month = monthly_profits_change.index(min(monthly_profits_change)) + 1 

# Print Statements
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profits)}")
print(f"Average Change: ${round(sum(monthly_profits_change)/len(monthly_profits_change),2)}")
print(f"Greatest Increase in Profits: {total_months[greatest_increase_month]} (${(str(greatest_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[greatest_decrease_month]} (${(str(greatest_decrease_value))})")

# exporting files
output = open("results.txt", "w")

# Write methods to print to Financial_Analysis_Summary 
line1 = "Financial Analysis"
line2 = "---------------------"
line3 = str(f"Total Months: {len(total_months)}")
line4 = str(f"Total: ${sum(total_profits)}")
line5 = str(f"Average Change: ${round(sum(monthly_profits_change)/len(monthly_profits_change),2)}")
line6 = str(f"Greatest Increase in Profits: {total_months[greatest_increase_month]} (${(str(greatest_increase_value))})")
line7 = str(f"Greatest Decrease in Profits: {total_months[greatest_decrease_month]} (${(str(greatest_decrease_value))})")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))