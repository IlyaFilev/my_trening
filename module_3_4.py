# "Произвольное число параметров"
def single_root_words(root_word, *other_words):
    same_words=[]
    for i in range(len(other_words)):
        if root_word.lower() in other_words[i].lower():
            same_words.append(other_words[i])
    return same_words


print(single_root_words('rich', 'Richiest', 'Griffin', 'orichalcum', 'Richies','apple'))
print(single_root_words('Cline', 'Inclination', 'Incline', 'recline'))

# с оператором count()
def single_root_words(root_word, *other_words):
    same_words=[]
    for i in range(len(other_words)):
        a = other_words[i].lower().count(root_word.lower())
        if a > 0:
            same_words.append(other_words[i])
    return same_words

print(single_root_words('rich', 'Richiest', 'Griffin', 'orichalcum', 'Richies','apple'))
print(single_root_words('Cline', 'Inclination', 'Incline', 'recline'))