# write_multiple_lines.py
f = open("user_input.txt", "w")
print("Enter multiple lines (type 'end' to stop):")
while True:
    line = input()
    if line.lower() == "end":
        break
    f.write(line + "\n")
f.close()
