import csv
import os
import json

def generarNuevo(reader,lista_bolleanos,lista_nombres,lista_traduccion, dicc):
    """Recorro una sola vez el archivo y creo 3 listas que vendrian a ser cada
    columna del archivo original


    Args:
        reader (): archivo original
        lista_bolleanos (list): lista de tuplas de las columnas de flags
        lista_nombres (list): listas que tendran este formato = "nombre(pais)"
        lista_traduccion (list): lista de nombres traducidos
        dicc (dict): diccionario con todos los nombres de volcanes traducidos que se tomo desde un archivo

    Returns:
        list: 3 listas antes mencionadas en este orden, lista_boleanos, lista_nombres, lista_de_traducciones
    """
    for l in reader:
        if l[3] == '' and l[4] == '': #LOS DOS VACIOS
            lista_bolleanos.append(['F', 'F'])
        elif l[3] == '' and l[4] != '': #PRIMERO = VACIO SEGUNDO = ALGO
            lista_bolleanos.append(['F', 'T'])
        elif l[3] != '' and l[4] == '':#PRIMERO = ALGO SEGUNDO = VACIO
            lista_bolleanos.append(['T', 'F'])
        elif l[3] != '' and l[4] != '':#PRIMERO = LLENO SEGUNDO = LLENO
            lista_bolleanos.append(['T', 'T'])

        lista_nombres.append(l[6] + ' ' + '(' + l[7] + ')')

        lista_traduccion.append(dicc[l[9]])

    return lista_bolleanos, lista_nombres, lista_traduccion


arch_traducciones = os.path.join(os.getcwd(), 'dicc_nombres.json')
encabezado = ['Year', 'Volcanic Explosivity Index', 'Volcano Type', 'Flag Tsunami', 'Flag Earthquake', 'Name and country']
aux = []
aux2 = []
aux3 = []
with open(arch_traducciones, 'r', encoding='utf-8') as f:
    dicc_nombres = json.load(f)
archivo_volcan = os.path.join(os.getcwd(), 'significant-volcanic-eruption-database.csv')
archivo_volcan_nuevo = os.path.join(os.getcwd(), 'archivo_volcanes_nuevo.csv');
with open(archivo_volcan, 'r', encoding='utf-8') as volcanes:
    reader = csv.reader(volcanes, delimiter=';')
    header = next(reader)
    with open(archivo_volcan_nuevo, 'w', newline = '') as nuevo:
        writer = csv.writer(nuevo, delimiter = ';')
        generarNuevo(reader,aux,aux2,aux3,dicc_nombres)
        volcanes.seek(0)
        writer.writerow(encabezado)
        next(reader)
        for elem in zip(aux, aux2, aux3, reader):
            writer.writerow([elem[3][0],elem[3][11] if elem[3][11]!='' 
                                else '??',elem[2], elem[0][0] if elem[0][0] != '' else '??', elem[0][1] if 
                                elem[0][1] != '' else '??', elem[1]])