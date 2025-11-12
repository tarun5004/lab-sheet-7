# 🧾 MCA I Semester – Python for Beginners (MCA101T)
## Assignment-07: File Handling and CSV Operations

This repository contains **30 Python programs** based on **File Handling** and **CSV Operations** as per the MCA I Semester lab sheet.  
Each program uses relative file paths, closes files properly, and includes clear comments.

---

## 📂 Folder Structure
File_Handling_Lab/
│
├── txt_programs/
│ ├── files/
│ │ ├── sample.txt
│ │ ├── numbers.txt
│ │ └── text2.txt
│ │
│ ├── 01_write_file.py
│ ├── 02_read_file.py
│ ├── ...
│ └── 20_merge_text_files.py
│
├── csv_programs/
│ ├── data.csv
│ ├── 21_write_csv.py
│ ├── 22_read_csv.py
│ ├── ...
│ └── 30_merge_csv_files.py
│
└── README.md


---

## 📘 Text File Programs (1–20)

1. Create and write text into a file  
2. Read entire content of a file  
3. Read file line by line  
4. Count words in a text file  
5. Count lines and characters in a file  
6. Display even-numbered lines  
7. Write multiple lines of input from user  
8. Append new content to an existing file  
9. Copy contents from one file to another  
10. Convert content to uppercase  
11. Search for a particular word  
12. Count occurrences of a specific word  
13. Read numbers and display sum and average  
14. Display the longest line  
15. Replace a word with another  
16. Display first and last lines  
17. Remove blank lines  
18. Store only unique words in another file  
19. Sort words alphabetically and save to new file  
20. Merge two text files into one  

---

## 📗 CSV File Programs (21–30)

21. Create and write data into a CSV file  
22. Read data from a CSV file  
23. Calculate average of numeric columns  
24. Count number of rows and columns  
25. Append a new record to existing CSV file  
26. Copy data from one CSV file to another  
27. Display specific columns (Name and Marks)  
28. Find and display highest marks  
29. Search record based on student name  
30. Combine multiple CSV files into one  

---

## ⚙️ Key Points

- No `def` or `try-except` used.  
- Uses **relative paths** like `files/sample.txt`.  
- Files are always closed using `.close()`.  
- Each program has short, clear comments.  
- CSV programs use the built-in **`csv`** module.  
- Ready to run directly on any system.

---

## ▶️ How to Run

```bash
# Clone repository
git clone https://github.com/<your-username>/File_Handling_Lab.git

# Open folder
cd File_Handling_Lab

# Run any program
python txt_programs/01_write_file.py

this file