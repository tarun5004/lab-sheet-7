# replace_word.py
f = open("sample.txt", "r")
data = f.read()
f.close()

old = input("Enter word to replace: ")
new = input("Enter new word: ")

data = data.replace(old, new)

f = open("sample.txt", "w")
f.write(data)
f.close()
print("Word replaced successfully.")
