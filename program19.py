# sort_words.py
f = open("sample.txt", "r")
words = f.read().split()
words.sort()
f.close()

out = open("sorted_words.txt", "w")
out.write(" ".join(words))
out.close()
print("Words sorted and saved.")
