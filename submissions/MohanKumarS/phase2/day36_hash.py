def word_frequency_counter(word):
    word = word.lower()  # convert all the characters to lowercase
    words = word.split()     # split the sentence into words
    
    freq_map = {} # use dictionary for hash maps
    for word in words:
        if word in freq_map:
            freq_map[word] += 1
        else:
            freq_map[word] = 1
    
    # print
    for word, count in freq_map.items():
        print(f"{word}: {count}")

word = input("Enter the input: ")
word_frequency_counter(word)
