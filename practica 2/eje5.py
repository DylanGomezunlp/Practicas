from collections import Counter

frase = "Tres tristes tigres, tragaban trigo en un trigal, en tres tristes trastos, tragaban trigo tres tristes tigres."

print("ingrese una palabra: ")

palabra = input().lower()

frase = frase.lower().split()
cont = 0
for elem in frase:
    if (palabra == elem):
        cont += 1
print(f"la palabra elegida fue: ", {palabra}, " y tuvo: ", {cont}, " ocurrencias")

# print(Counter(frase.split())[palabra]) esta es la forma sencilla.


