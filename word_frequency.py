#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)
# 1. Prompt the user: Ask the user to enter a sentence.
# 2. Split the sentence
# 3. Create lists to store words and their corresponding frequencies.
# 4. Iterate through words and update frequencies

import string

user_sentence = input("Enter a sentence: ")
words = user_sentence.split()

unique_words = []
frequencies = []

for word in words:
    normalized = ""
    for char in word:
        if char not in string.punctuation:
            normalized += char.lower()
    if normalized == "":
        continue  # skip empty results
    if normalized in unique_words:
        index = unique_words.index(normalized)
        frequencies[index] = frequencies[index] + 1
    else:
        unique_words.append(normalized)
        frequencies.append(1)

for i in range(len(unique_words)):
    print(f"{unique_words[i]}: {frequencies[i]}")

