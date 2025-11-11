# first_last_line.py
f = open("sample.txt", "r")
lines = f.readlines()
print("First line:", lines[0].strip())
print("Last line:", lines[-1].strip())
f.close()
