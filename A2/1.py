# Input w word
word = input("Enter a word: ")

# Empty string to store the new word
new_word = ""

# Loop to iterate over the word
for i in range(len(word)):
    # Check if the index is even or odd
    if i % 2 == 0:
        new_word += word[i]
    else:
        new_word += word[i].upper()

# Print the new word
print(new_word)