# copy_file.py
src = open("sample.txt", "r")
dest = open("copy_sample.txt", "w")
for line in src:
    dest.write(line)
src.close()
dest.close()
print("File copied successfully.")
