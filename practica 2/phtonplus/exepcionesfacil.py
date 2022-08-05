import random
claves_acceso = {
        'Banco':'EstAesMiClave2021',
        'Facebook':'REdAmigos',
        'Instagram':'PaRApasarTiempo',
        'TicTic':'Conociendote'
                    }
def genero_claves():
    valores = 'abcdefghijklmñopqrstuvwxyz0123456789'
    clave = ''
    for valor in range(8):
        clave = clave + valores[random.randrange(35)]
    return(clave)
    
def muestro_claves(claves_acceso):
    try:
        aplicacion = input('Ingresamos nombre de la aplicacion: ')
        print(claves_acceso[aplicacion])
    except ValueError:
            print('Se produjo un error al mostrar la clave!')
    else:
        print('Se mostro con exito la clave!')

resp = input('queres gestiionar las claves? s/n').upper()
while resp == 'S':
    opcion = int(input("""
    Que queres hacer:
    1-Agregar/modificar clave
    2- Mostrar clave"""))
    try:
        if opcion == 1:
            aplicacion = input("ingresanos el nombre de la aplicacion: ")
            claves_acceso[aplicacion] = genero_claves()
        elif opcion == 2:
            muestro_claves(claves_acceso)
    except (KeyError, ValueError):
        print('se produjo un error...')
    finally:
        resp = input('queres gestionar claves? s/N').upper()