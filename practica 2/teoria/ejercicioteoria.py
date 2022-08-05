import csv

import os
ruta_archivos = 'archivos'   
os.getcwd()
ruta_completa = os.path.join(os.getcwd(), ruta_archivos)
archivo_netflix = os.path.join(os.getcwd(), 'netflix_titles.csv')
titulos_2021 = os.path.join(os.getcwd(), 'titulos2021.csv')
with open(archivo_netflix, encoding='utf-8') as data_set:
    reader = csv.reader(data_set, delimiter=',')
    with open(titulos_2021, 'w', encoding='utf-8') as salida:
            writer = csv.writer(salida)
            reader.__next__()
            writer.writerows(map(lambda titulo: titulo[5].split(','), reader))//en lugar de writerow va el list con lo que se usa para que no haya elementos repetidos
    
