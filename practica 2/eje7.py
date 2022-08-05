from collections import Counter


print('ingrese una palabra o frase')
frase = input().lower()
if (Counter(frase).most_common()[0][1] == 1 ):
    print("es heterograma")
else:
    print("no es heterograma")

