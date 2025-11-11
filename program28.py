# csv_highest_marks.py
import csv

f = open("students.csv", "r")
reader = csv.reader(f)
next(reader)

highest = 0
topper = ""

for row in reader:
    marks = int(row[2])
    if marks > highest:
        highest = marks
        topper = row[0]

print("Highest Marks:", highest, "by", topper)
f.close()
