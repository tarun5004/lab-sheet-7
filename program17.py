# remove_blank_lines.py
f = open("sample.txt", "r")
lines = f.readlines()
f.close()

f = open("no_blank.txt", "w")
for line in lines:
    if line.strip() != "":
        f.write(line)
f.close()
print("Blank lines removed.")
