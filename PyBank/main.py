import pandas as pd
import os

# Set the file path
cwd = os.getcwd()
data = "Resources"
budget_data = os.path.join(cwd, data, 'budget_data.csv')

# Check if the file exists before proceeding
if os.path.exists(budget_data):
    print(f"File path: {budget_data}")
else:
    print("The 'budget_data.csv' file does not exist in the specified path.")

# Read the CSV file using Pandas
df = pd.read_csv(budget_data)

# Calculate the total number of months
total_months = df['Date'].count()

# Calculate the net total amount of Profit/Losses
net_total = df['Profit/Losses'].sum()

# Calculate the changes in Profit/Losses and add them as a new column
df['Change'] = df['Profit/Losses'].diff()

# Calculate the average of the changes in Profit/Losses
average_change = df['Change'].mean()

# Find the greatest increase in profits and the greatest decrease in losses
greatest_increase = df['Change'].max()
greatest_increase_month = df.loc[df['Change'] == greatest_increase, 'Date'].values[0]
greatest_decrease = df['Change'].min()
greatest_decrease_month = df.loc[df['Change'] == greatest_decrease, 'Date'].values[0]

# Print the results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase:.0f})")
print(f"Greatest Decrease in Losses: {greatest_decrease_month} (${greatest_decrease:.0f})")

# Save the results to a text file
with open("financial_analysis.txt", "w") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${net_total}\n")
    txtfile.write(f"Average Change: ${average_change:.2f}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase:.0f})\n")
    txtfile.write(f"Greatest Decrease in Losses: {greatest_decrease_month} (${greatest_decrease:.0f})\n")
