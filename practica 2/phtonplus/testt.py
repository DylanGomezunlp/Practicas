import random
import pandas as pd

def convertir_bool(Flag):
    if Flag != "¿?":
        return True
    else:
        return False
    
def concatenar_nombres(fila):
    resultado = fila["Volcano Name"] + fila["Country"]


    return resultado

df = pd.read_csv("significant-volcanic-eruption-database.csv", sep=';')
df = df.fillna("¿?")
df.head(6)
df["Flag Tsunami"] = df["Flag Tsunami"].apply(convertir_bool)
df["Flag Earthquake"] = df["Flag Earthquake"].apply(convertir_bool)
df["Country and Name"] = df.apply(concatenar_nombres, axis = 1)
