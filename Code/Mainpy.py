import pandas as pd
from Modulo import leer_datos, filtrar_calcular_media

path='C:/Users/nicol/OneDrive/Documentos/examen_evaluacion/examen_evaluacion/Data/datos_examen.csv'

def main():
    df=leer_datos(path)
    print(df)
    print()
    print(filtrar_calcular_media(df))

if __name__ == "__main__":
    main()