# count_lines_chars.py
f = open("sample.txt", "r")
lines = f.readlines()
print("Number of lines:", len(lines))
print("Number of characters:", sum(len(line) for line in lines))
f.close()
