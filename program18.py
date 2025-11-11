# unique_words.py
f = open("sample.txt", "r")
words = f.read().split()
unique = set(words)
f.close()

out = open("unique_words.txt", "w")
out.write(" ".join(unique))
out.close()
print("Unique words saved.")
