import pandas as pd
from pathlib import Path

# Get the current working directory
current_directory = Path.cwd()
# Print the current directory
print("Current Directory:", current_directory)
#Set file paths for menu_data.csv and sales_data.csv
menu_filepath = current_directory / "Resources/menu_data.csv"
sales_filepath = current_directory / "Resources/sales_data.csv"

# Print the file paths
print("Menu File Path:", menu_filepath)
print("Sales File Path:", sales_filepath)

# Read in the menu data into a DataFrame
menu_df = pd.read_csv(menu_filepath)

# Read in the sales data into a DataFrame
sales_df = pd.read_csv(sales_filepath)


# Initialize dict object to hold our key-value pairs of items and metrics
report = {}

# Initialize a row counter variable
row_count = 0

# Loop over every row in the sales list object
# Loop over every row in the sales DataFrame
for index, sale in sales_df.iterrows():
    # Initialize sales data variables
    quantity = int(sale["Quantity"])
    menu_item = sale["Menu_Item"]

    # If the item value is not in the report, add it as a new entry with initialized metrics
    if menu_item not in report:
        report[menu_item] = {
            "01-count": 0,
            "02-revenue": 0,
            "03-cogs": 0,
            "04-profit": 0,
        }

    # Find the corresponding menu data for this item
    menu_data = menu_df[menu_df["item"] == menu_item]
    if not menu_data.empty:
        price = float(menu_data["price"])
        cost = float(menu_data["cost"])
        profit = (price - cost) * quantity

        # Update the item metrics in the report dictionary
        report[menu_item]["01-count"] += quantity
        report[menu_item]["02-revenue"] += price * quantity
        report[menu_item]["03-cogs"] += cost * quantity
        report[menu_item]["04-profit"] += profit

    # Increment the row counter
    row_count += 1

# Set the output file path for the report
report_dict_output_file = current_directory / "report_dict_output.txt"

# Open the output file in write mode ('w')
with open(report_dict_output_file, 'w') as output_file:
    # Loop over the report dictionary and write its contents to the file
    output_file.write("Report:\n")
    for item, metrics in report.items():
        output_file.write(f"Item: {item}\n")
        output_file.write(f"Metrics: {metrics}\n\n")

# Set the output file path for the matching menu data report
matching_menu_data_report = current_directory / "matching_menu_data_report.txt"

# Open the output file in write mode ('w') to clear any previous content
with open(matching_menu_data_report, 'w') as output_file:
    output_file.write("")  # Clear previous content

# Loop through the sales DataFrame
for index, sale in sales_df.iterrows():
    # Initialize sales data variables
    quantity = int(sale["Quantity"])
    menu_item = sale["Menu_Item"]

    # Initialize a flag to check if a match is found in the menu data
    match_found = False

    # Loop over the menu DataFrame to determine a match
    for _, menu_item_data in menu_df.iterrows():
        item_name = menu_item_data["item"]
        price = float(menu_item_data["price"])
        cost = float(menu_item_data["cost"])
        menu_item_profit = (price - cost) * quantity

        if menu_item == item_name:
            # Set match_found flag to True
            match_found = True

            # Append matching menu data to the file
            with open(matching_menu_data_report, 'a') as output_file:
                output_file.write(f"Matching Menu Item: {menu_item}\n")
                output_file.write(f"Item: {item_name}\n")
                output_file.write(f"Price: {price}\n")
                output_file.write(f"Cost: {cost}\n")
                output_file.write(f"Profit: {menu_item_profit}\n\n")  # Add newline to separate entries

            # Cumulatively add up the metrics for each item key
            if menu_item not in report:
                report[menu_item] = {
                    "01-count": 0,
                    "02-revenue": 0,
                    "03-cogs": 0,
                    "04-profit": 0,
                }

            report[menu_item]["01-count"] += quantity
            report[menu_item]["02-revenue"] += price * quantity
            report[menu_item]["03-cogs"] += cost * quantity
            report[menu_item]["04-profit"] += menu_item_profit

            break  # No need to continue searching once a match is found

    # If the sales item does not equal any of the items in the menu data, there is no match
    if not match_found:
        with open(matching_menu_data_report, 'a') as output_file:
            output_file.write(f"No Match Found for Sales Item: {menu_item}\n")

    # Increment the row counter
    row_count += 1

# Print total number of records in sales data
print(f"Total Number of Records in Sales Data: {row_count}")

# Set the output file path for the sales report
output_file_path = current_directory / "sales_report.txt"

# Open the output file in write mode ('w')
with open(output_file_path, 'w') as output_file:
    output_file.write("Sales Report\n")
    output_file.write("-" * 40 + "\n")
    output_file.write(f"Total Number of Records in Sales Data: {row_count}\n")
    output_file.write("\nItem Metrics:\n")

    # Loop through the report dictionary and write metrics to the file
    for item, metrics in report.items():
        output_file.write(f"Item: {item}\n")
        for key, value in metrics.items():
            output_file.write(f"{key}: {value}\n")
        output_file.write("-" * 20 + "\n")

print(f"Report written to {output_file_path}")