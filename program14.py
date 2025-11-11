# longest_line.py
f = open("sample.txt", "r")
lines = f.readlines()
longest = max(lines, key=len)
print("Longest line:\n", longest)
f.close()
