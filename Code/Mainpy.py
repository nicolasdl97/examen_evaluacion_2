import pandas as pd
import matplotlib.pyplot as plt
from Modulo import leer_datos, filtrar_calcular_media, grafico_barras

path='C:/Users/nicol/OneDrive/Documentos/examen_evaluacion/examen_evaluacion/Data/datos_examen.csv'

def main():
    df=leer_datos(path)
    display(df)
    print()
    print(filtrar_calcular_media(df))
    print()
    grafico_barras(df)

if __name__ == "__main__":
    main()