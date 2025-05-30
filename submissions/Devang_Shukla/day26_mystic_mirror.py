sentence = int("Enter a sentence:")
vowels_set = set("aeiouAEIOU")
vowels_count = 0
consonant_count = 0
for char in sentence:
    if char.isalpha():
        if char in vowels_set:
            vowels_count += 1
        else:
            consonant_count += 1
print("Vowels:", vowels_count)      
print("Consonants:", consonant_count)            