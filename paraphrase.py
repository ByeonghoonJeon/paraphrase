import random

# Dictionary of Synonyms
synonym_dictionary = {
    "초록색":["초록빛", "풀색", "녹색" ,"녹색 푸르른"],
    "good": ["nice", "perfect"],
    "많은": ["풍부한", "다양한"],
    "너무": ["정말", "참"],
    "살펴보도록":["알아보도록", "공부해보도록", "설명해보도록"],
    "들어있는":["함유되어있는", "함유된", "포함되어있는"],
    "아직":["아직까지도", "이제껏"],
    "붉은":["빨간"],
    "빨간":["붉은"],
    "흐린":["구름이 낀"],
    "날":["하루"],
    "날에":["하루에"],
    "날에는":["하루에는"],
    "오늘":["지금"],
    "오늘처럼":["지금처럼"],
    "오늘과 같이":["지금처럼"]

    
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
    if i.lower() in synonym_dictionary:
        newPhrase.append(random.choice(synonym_dictionary[i.lower()]))
    else: 
        newPhrase.append(i)

# Make list to string and print.
print (" ".join(newPhrase))


