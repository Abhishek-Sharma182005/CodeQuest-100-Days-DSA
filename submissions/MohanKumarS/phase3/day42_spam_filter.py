word = input("Enter email subjects (comma-separated): ")
word = list(word.split(","))

spam = input("Enter spam keywords (comma-separated): ")
spam = list(spam.split(","))

word = [w.strip() for w in word]
spam = [s.strip() for s in spam]


print("Filtered emails:")
for i in word:
    if not any(s.lower() in i.lower() for s in spam):
        print(" -", i)
