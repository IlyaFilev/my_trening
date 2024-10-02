import random
from http.cookiejar import join_header_words
from pprint import pprint

Dano = random.choice(range(3, 21))
shifr = []
for i in range(1, 20):
    for j in range(1, 20):
            if Dano % (i + j) == 0:
                if i != j and [i, j] not in shifr and [j, i] not in shifr:
                    shifr.append([i, j])

print(shifr)
#print(Dano,'-', .join(shifr))
Parole = '-'
for i in range(0, len(shifr)):
    for j in range(0,2):
        Parole += str(shifr[i][j])

print(Dano,Parole)