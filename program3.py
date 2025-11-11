# read_line_by_line.py
f = open("sample.txt", "r")
for line in f:
    print(line.strip())
f.close()
