# count_word_occurrence.py
f = open("sample.txt", "r")
word = input("Enter word to count: ")
text = f.read().split()
count = text.count(word)
print("Occurrences of", word, ":", count)
f.close()
