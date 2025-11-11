# csv_append.py
import csv

f = open("students.csv", "a", newline="")
writer = csv.writer(f)

writer.writerow(["Karan", 23, 88])

f.close()
print("New record appended successfully.")
