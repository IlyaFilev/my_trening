# Произвольное число параметров - "Однокоренные"
def single_root_words(root_word, *other_words):
    same_words=[]
    for i in range(len(other_words)):
        if root_word.lower() in other_words[i].lower() or other_words[i].lower() in root_word.lower():
            same_words.append(other_words[i])
    return same_words


result1 = (single_root_words('rich', 'Richiest', 'Griffin', 'orichalcum', 'Richies','apple', 'ric'))
print(result1)
result2 = (single_root_words('Cline', 'Inclination', 'Incline', 'recline'))
print(result2)



# с оператором count()
def single_root_words(root_word, *other_words):
    same_words=[]
    for i in range(len(other_words)):
        counter = other_words[i].lower().count(root_word.lower())
        if counter > 0:
            same_words.append(other_words[i])

    return f'{root_word} найден в следующих словах : {same_words}'

print(single_root_words('rich', 'Richiest', 'Griffin', 'orichalcum', 'Richies','apple', 'ric'))
print(single_root_words('Cline', 'Inclination', 'Incline', 'recline'))