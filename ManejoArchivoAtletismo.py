import os
import pandas as pd

def guardar_pruebas_de_campo(df,nombre):
    path_completo = os.path.join('Pruebas de campo', nombre)
    if (len(df) != 0 ):
        df.to_csv(path_completo,index= False)

def ordenar_serie(df):
    
    # Crear una nueva columna para las filas
    df['Andanivel'] = 0

    # Asignar las filas según el orden especificado
    orden_filas = [4, 5, 3, 6, 2, 7, 1, 8]
    num_atletas = len(df)
    num_filas = len(orden_filas)

    # Asignar a cada atleta a una fila basándose en su tiempo
    for i in range(num_atletas):
        # El índice en orden_filas es el resto de la división i / num_filas
        indice = i % num_filas
        df.iloc[i, df.columns.get_loc('Andanivel')] = orden_filas[indice]

    # Ordenar el DataFrame por la columna de fila
    df = df.sort_values('Andanivel')
    return df

def series(df,parametro,tamanio_filas = 8):
    if (not os.path.exists(parametro)):
        os.makedirs(parametro)

    '''if (len(df) % 8 == 0): tamanio_filas = 8
    elif (len(df) % 7 == 0):tamanio_filas = 7
    else : tamanio_filas = 6'''

    filas_divididas = [df[i:i + tamanio_filas] for i in range(0, len(df), tamanio_filas)] 

    for i, df_split in enumerate(filas_divididas):
        #df_split = df_split.sample(frac=1, random_state=42)
        nombre = (f'Serie {i + 1} {parametro}.csv')
        path_completo = os.path.join(parametro,nombre)
        if ('100' in parametro or '400' in parametro or '110' in parametro):
            df_split = ordenar_serie(df_split)
        df_split.to_csv(path_completo, index=False)
           
def filtrar_100Metros(archivo):
    datos = archivo[archivo["100 Metros"] != None]
    columnas_borrar = ['Marca temporal', 'Seleccione su género',
        'Apto Médico', '400 Metros', '1500 Metros', '3000 Metros',
        '100/110 C/V','Pruebas de campo']
    datos = datos.drop(columnas_borrar,axis=1)
    datos = datos.dropna()
    datos = datos.sort_values(by="100 Metros", ascending =True)
    datos.rename(columns= {'100 Metros': 'Marca'},inplace=True)
    return datos

def filtrar_400Metros(archivo):
    datos = archivo[archivo["400 Metros"] != None]
    columnas_borrar = ['Marca temporal', 'Seleccione su género',
        'Apto Médico', '100 Metros', '1500 Metros', '3000 Metros',
        '100/110 C/V','Pruebas de campo']
    datos = datos.drop(columnas_borrar,axis=1)
    datos = datos.dropna()
    datos = datos.sort_values(by= "400 Metros", ascending=True)
    datos.rename(columns= {'400 Metros': 'Marca'},inplace=True)
    return datos

def filtrar_1500Metros(archivo):
    datos = archivo[archivo["1500 Metros"] != None]
    columnas_borrar = ['Marca temporal', 'Seleccione su género',
        'Apto Médico', '100 Metros', '400 Metros', '3000 Metros',
        '100/110 C/V','Pruebas de campo']
    datos = datos.drop(columnas_borrar,axis=1)
    datos = datos.dropna()
    datos.rename(columns= {'1500 Metros': 'Marca'},inplace=True)
    datos = datos.sort_values(by= "Marca",ascending=True)
    return datos

def filtrar_3000Metros(archivo):
    datos = archivo[archivo["3000 Metros"] != None]
    columnas_borrar = ['Marca temporal', 'Seleccione su género',
        'Apto Médico', '100 Metros', '1500 Metros', '400 Metros',
        '100/110 C/V','Pruebas de campo']
    datos = datos.drop(columnas_borrar,axis=1)
    datos = datos.dropna()
    datos = datos.sort_values(by= "3000 Metros",ascending=True)
    datos.rename(columns= {'3000 Metros': 'Marca'},inplace=True)
    return datos

def filtrar_vallas(archivo):
    datos = archivo[archivo["100/110 C/V"] != None]
    columnas_borrar = ['Marca temporal', 'Seleccione su género',
        'Apto Médico', '100 Metros', '1500 Metros', '3000 Metros',
        '400 Metros','Pruebas de campo']
    datos = datos.drop(columnas_borrar,axis=1)
    datos = datos.dropna()
    datos = datos.sort_values(by= "100/110 C/V",ascending=True)
    datos.rename(columns= {'100/110 C/V': 'Marca'},inplace=True)
    return datos

def filtrar_largo(archivo):
    archivo["Pruebas de campo"] = archivo["Pruebas de campo"].fillna("")
    datos = archivo[archivo["Pruebas de campo"].str.contains("LARGO", case=False)]
    columnas_borrar = ['Marca temporal', 'Seleccione su género',
        'Apto Médico', '100 Metros', '1500 Metros', '3000 Metros',
        '400 Metros', '100/110 C/V','Pruebas de campo']
    datos = datos.drop(columnas_borrar,axis=1)
    datos = datos.dropna()
    return datos

def filtrar_garrocha(archivo):
    datos = archivo[archivo["Pruebas de campo"].str.contains('GARROCHA')]
    columnas_borrar = ['Marca temporal', 'Seleccione su género',
        'Apto Médico', '100 Metros', '1500 Metros', '3000 Metros',
        '400 Metros', '100/110 C/V','Pruebas de campo']
    datos = datos.drop(columnas_borrar,axis=1)
    datos = datos.dropna()
    return datos

def filtrar_martillo(archivo):
    datos = archivo[archivo["Pruebas de campo"].str.contains('MARTILLO')]
    columnas_borrar = ['Marca temporal', 'Seleccione su género',
        'Apto Médico', '100 Metros', '1500 Metros', '3000 Metros',
        '400 Metros', '100/110 C/V','Pruebas de campo']
    datos = datos.drop(columnas_borrar,axis=1)
    datos = datos.dropna()
    return datos

def filtrar_bala(archivo):
    datos = archivo[archivo["Pruebas de campo"].str.contains('BALA')]
    columnas_borrar = ['Marca temporal', 'Seleccione su género',
        'Apto Médico', '100 Metros', '1500 Metros', '3000 Metros',
        '400 Metros', '100/110 C/V','Pruebas de campo']
    datos = datos.drop(columnas_borrar,axis=1)
    datos = datos.dropna()
    return datos

def filtrar_jabalina(archivo):
    datos = archivo[archivo["Pruebas de campo"].str.contains('JABALINA')]
    columnas_borrar = ['Marca temporal', 'Seleccione su género',
        'Apto Médico', '100 Metros', '1500 Metros', '3000 Metros',
        '400 Metros', '100/110 C/V','Pruebas de campo']
    datos = datos.drop(columnas_borrar,axis=1)
    datos = datos.dropna()
    return datos


path_files = os.path.dirname(os.path.realpath("."))
patch_arch = os.path.join(path_files)
inscriptos = open(os.path.join(patch_arch,"AtletismoUnlp", "Inscripción competencia UNLP.csv"),'r', encoding='utf8')
data_set = pd.read_csv(inscriptos, encoding='utf8')
data_set.rename(columns= {'Federación/ Asociación/Club': 'Club'},inplace=True)

#Inscriptos en data_set

masculino = data_set[data_set["Seleccione su género"]== "Masculino"]
femenino = data_set[data_set["Seleccione su género"]== "Femenino"]

#PRUEBAS DE PISTA
series(filtrar_100Metros(masculino),"100 Metros Masculino")
series(filtrar_100Metros(femenino),"100 Metros Femenino")

series(filtrar_400Metros(masculino),"400 Metros Masculino")
series(filtrar_400Metros(femenino),"400 Metros Femenino")

series(filtrar_1500Metros(masculino),"1500 Metros Masculino", 15)
series(filtrar_1500Metros(femenino),"1500 Metros Femenino",15)

series(filtrar_3000Metros(masculino),"3000 Metros Masculino",20)
series(filtrar_3000Metros(femenino),"3000 Metros Femenino",20)

series(filtrar_vallas(masculino),"110 con Vallas Masculino")
series(filtrar_vallas(femenino),"100 con Vallas Femenino")


#PRUEBAS DE CAMPO
if (not os.path.exists('Pruebas de campo')):
        os.makedirs('Pruebas de campo')
    
guardar_pruebas_de_campo(filtrar_largo(masculino),'Inscriptos Largo Masculino.csv')
guardar_pruebas_de_campo(filtrar_largo(femenino),'Inscriptos Largo Femenino.csv')

guardar_pruebas_de_campo(filtrar_garrocha(masculino),'Inscriptos Garrocha Masculino.csv')
guardar_pruebas_de_campo(filtrar_garrocha(femenino),'Inscriptos Garrocha Femenino.csv')

guardar_pruebas_de_campo(filtrar_martillo(masculino),'Inscriptos Martillo Masculino.csv')
guardar_pruebas_de_campo(filtrar_martillo(femenino),'Inscriptos Martillo Femenino.csv')

guardar_pruebas_de_campo(filtrar_bala(masculino),'Inscriptos Bala Masculino.csv')
guardar_pruebas_de_campo(filtrar_bala(femenino),'Inscriptos Bala Femenino.csv')

guardar_pruebas_de_campo(filtrar_jabalina(masculino),'Inscriptos Jabalina Masculino.csv')
guardar_pruebas_de_campo(filtrar_jabalina(femenino),'Inscriptos Jabalina Femenino.csv')



