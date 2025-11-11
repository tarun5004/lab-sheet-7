# csv_rows_cols.py
import csv

f = open("students.csv", "r")
reader = list(csv.reader(f))

rows = len(reader)
cols = len(reader[0])

print("Rows:", rows)
print("Columns:", cols)
f.close()
