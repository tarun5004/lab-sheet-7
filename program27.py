# csv_specific_columns.py
import csv

f = open("students.csv", "r")
reader = csv.reader(f)
next(reader)  # Skip header

for row in reader:
    print("Name:", row[0], "| Marks:", row[2])

f.close()
