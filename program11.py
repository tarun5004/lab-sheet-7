# search_word.py
f = open("sample.txt", "r")
word = input("Enter word to search: ")
found = False
for line in f:
    if word in line:
        found = True
        break
f.close()

if found:
    print("Word found in file.")
else:
    print("Word not found.")
