# csv_copy.py
import csv

source = open("students.csv", "r")
target = open("students_copy.csv", "w", newline="")

reader = csv.reader(source)
writer = csv.writer(target)

for row in reader:
    writer.writerow(row)

source.close()
target.close()
print("CSV file copied successfully.")
