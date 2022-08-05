
cadena = input("Ingresa la clave (debe tener menos de 10 caracteres y no␣ ,→contener los símbolos:@ y !):")

if len(cadena) > 10:
    print("Ingresaste más de 10 carcateres")
elif map(lambda c: c in cadena, ('@' or '!')):
    print('ingresaste un @ o un !')
else:
    print('clave valida')


