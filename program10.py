# uppercase_file.py
f = open("sample.txt", "r")
data = f.read().upper()
f.close()

f = open("uppercase.txt", "w")
f.write(data)
f.close()
print("File converted to uppercase.")
