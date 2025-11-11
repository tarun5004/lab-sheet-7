# even_lines.py
f = open("sample.txt", "r")
lines = f.readlines()
for i in range(1, len(lines), 2):   # index 1 = 2nd line
    print(lines[i].strip())
f.close()
