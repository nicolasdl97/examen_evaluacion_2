import pandas as pd
import matplotlib.pyplot as plt

def leer_datos(path:str):
    '''A través de una dirección ("path") se realiza la lectura de datos. Después, corrige el tipo de la 
    variable TS a datetime. '''
    df=pd.read_csv(path)
    df['TS']=pd.to_datetime(df['TS'])
    return df

if __name__ == "__main__":
    leer_datos(path)

def filtrar_calcular_media(df)->str:
    '''Se toma como input el dataframe elaborado en la función leer_datos(), através del método groupby,
    se obtiene la media de la columna 'Value' en función de cada valor único en la columna 'Tag'. '''
    result = df.groupby('Tag')['Value'].mean()
    return result
    
if __name__ == "__main__":
    filtrar_calcular_media(df)
    
def grafico_barras(df)->str:

    '''Se toma como input el dataframe elaborado en la función leer_datos(), através de la función creada
    previamente de filtrar_calcular_media(df) método groupby, se obtiene la media de la columna 'Value'
    en función de cada valor único en la columna 'Tag'. Finalmente, haciendo uso de la libreria matplotlib,
    realizamos un gráfico de barras del mismo. '''

    result = filtrar_calcular_media(leer_datos('C:/Users/nicol/OneDrive/Documentos/examen_evaluacion/examen_evaluacion/Data/datos_examen.csv'))

    plt.figure(figsize=(10, 6)) 

    result.plot(kind='bar')

    plt.title('Media de valores por Tag')
    plt.xlabel('Tag')
    plt.ylabel('Media de valores')
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()
    
if __name__ == "__main__":
    grafico_barras(df)

