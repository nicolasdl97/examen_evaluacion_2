import pandas as pd

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
    


