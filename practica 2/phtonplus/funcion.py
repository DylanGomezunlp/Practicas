from telnetlib import NOP
import csv
import os


def pokemonesmenor(csvreader):
    """Recive un csv reader y retorna la lista con los pokemones con valor 
    total inferior a 500.

    Args:
        csvreader (csvreader): Archivo con los datos de los pokemones

    Returns:
        list: lista con los pokemones con valor total inferior a 500
    """
    lista_nueva  = []
    funcion = lambda a,lista_nueva: (lista_nueva.append(a) if (int(a[4]) < 500) else NOP)
    map(funcion(csvreader,lista_nueva), csvreader)
    return lista_nueva


nom_archivo = "Pokemon.csv"
with open(os.path.join(os.getcwd(), nom_archivo), "r", encoding="UTF-8"):
    csvreader = csv.reader(nom_archivo, delimiter=',')
    header = next(csvreader)
    lista_nueva = pokemonesmenor(csvreader)
    
lista_nueva