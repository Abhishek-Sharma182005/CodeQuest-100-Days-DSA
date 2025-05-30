sentence = int("Enter a sentence:")
words = sentence.split()
longest_word = ""
max_length = 0
for word in words:
    clean_word = ''.join(char for char in word if char.isalnum())
    if len(clean_word) > max_length:
        longest_word = clean_word
        max_length = len(clean_word)
print("Longest word:", longest_word)        