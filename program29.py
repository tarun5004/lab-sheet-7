# csv_search.py
import csv

name = input("Enter student name to search: ")

f = open("students.csv", "r")
reader = csv.reader(f)
next(reader)

found = False
for row in reader:
    if row[0].lower() == name.lower():
        print("Record found:", row)
        found = True
        break

if not found:
    print("Record not found.")

f.close()
