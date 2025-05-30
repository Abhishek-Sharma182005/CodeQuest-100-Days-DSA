import string
text = input("Enter text: ")
text = text.lower()
text = text.translate(str.maketrans('','',string.punctuation))
words = text.split()
word_freq = {}
for word in words:
    word_freq[word] = word_freq.get(word,0) + 1
for word, freq in word_freq.items():
    print(f"{word}: {freq}")    