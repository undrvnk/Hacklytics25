import csv

# Open CSV file and read into a dictionary
with open('laptop_prices.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    data = [row for row in reader]  # List of dictionaries

print(data)  # Each row is a dictionary with column names as keys