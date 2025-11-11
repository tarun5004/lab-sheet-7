# write_csv.py
import csv

f = open("students.csv", "w", newline="")
writer = csv.writer(f)

writer.writerow(["Name", "Age", "Marks"])
writer.writerow(["Ravi", 20, 85])
writer.writerow(["Neha", 21, 90])
writer.writerow(["Amit", 22, 78])

f.close()
print("CSV file created and data written successfully.")
