# csv_average.py
import csv

f = open("students.csv", "r")
reader = csv.reader(f)
next(reader)  # Skip header

total = 0
count = 0
for row in reader:
    total += int(row[2])
    count += 1

print("Average Marks:", total / count)
f.close()
