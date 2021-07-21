import random

# Dictionary of Synonyms
synonym_dictionary = {
    "Good": ["Nice", "Perfect"]
} 


# Request input
phrase = input("Type your phrases.\n")

# Split phrase to words.
words = phrase.split()

# Make empty list to save substituted words.
newPhrase = []

# If input has a corresponding word in the dictionary above, substitute to synonym and add to newPharse list.
# Otherwise, save as it is without change to newPhrase list.
for i in words:
    if i in synonym_dictionary:
        newPhrase.append(random.choice(synonym_dictionary[f"{i}"]))
    else: 
        newPhrase.append(i)

# Make list to string and print.
print (" ".join(newPhrase))


