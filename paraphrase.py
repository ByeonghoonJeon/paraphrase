# Dictionary of Synonyms
import random

synonym_dictionary = {
    "Hello": ["Nice", "Good"]
} 

phrase = input("Type your phrases.\n")
words = phrase.split()

newPhrase = []

print(words)

for i in words:
    if i in synonym_dictionary:
        newPhrase.append(random.choice(synonym_dictionary[f"{i}"]))
    else: 
        newPhrase.append(i)

print (" ".join(newPhrase))


