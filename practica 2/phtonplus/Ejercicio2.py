claves_acceso = {
			'Banco': 'EstAesMiClave2021',
			'Facebook':'REdAmigos', 
			'Instagram': 'PaRApasarTiempo',
			'TicToc': 'Conociendote'
				  }
def agrego_claves (claves_acceso):
	try:
		aplicacion = input('Ingresanos nombre de la aplicación: ')
		clave = input('Ingresanos clave de la aplicación: ')
		claves_acceso [aplicacion] = clave
	except:
		print ('Se produjo un error!')
	
def muestro_claves (claves_acceso):
	aplicacion = input('Ingresanos nombre de la aplicación: ')
	print (claves_acceso [aplicacion])
		
#Gestionando claves
resp = input('Querés gestionar las claves? S/N ').upper()

while resp == 'S':
    try:
        opcion = int(input("""Qué querés hacer:
                            1- Agregar/modificar claves
                            2- Mostrar clave  """))
        if opcion == 1:
            agrego_claves(claves_acceso)
        elif opcion == 2:
            muestro_claves(claves_acceso)
        resp = input('Querés gestionar las claves? S/N ').upper()
    except (KeyError, ValueError):
        print ('Ups algún error se produjo..')
        resp = input('Querés gestionar las claves? S/N ').upper()
