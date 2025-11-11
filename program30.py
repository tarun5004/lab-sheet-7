# csv_merge_files.py
import csv

# List of CSV files to merge
files = ["students.csv", "students_copy.csv"]

out = open("merged_students.csv", "w", newline="")
writer = csv.writer(out)

header_written = False

for file in files:
    f = open(file, "r")
    reader = csv.reader(f)
    header = next(reader)
    if not header_written:
        writer.writerow(header)
        header_written = True
    for row in reader:
        writer.writerow(row)
    f.close()

out.close()
print("All CSV files merged successfully.")
