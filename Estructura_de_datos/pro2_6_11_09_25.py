#practica de dataframe
import pandas as pd

#creacion de un dataframe
#diccionario de datos para el df 
dict_datos={"Peso":[87,78,45,22,90],"Estatura":[121,180,199,150,165]}

#asignacion de datos para la creacion del df
datos_df=pd.DataFrame(dict_datos)
print(datos_df)

#asignacion de etiquetas para los indices personalizados 
datos_df.index=["Carlos","Violeta","Fabi","Olga","Pedro"]
print(datos_df)

#uso de metodos de estadistica descriptiva por cada columna An:An|Bn:Bn
print(f'\n{datos_df.mean()}')
print(f'\n{datos_df.var()}')
print(f'\n{datos_df.max()}')

#uso de metodos de estadistica descriptiva por cada renglon
#usando el parametro axis, por default este parametro esta en 0, por cada columna,
#al cambiarlo a uno te dara elo promedio por cada renglon A0+B0/2
print("El promedio por cada renglon es: ")
print(datos_df.mean(axis=1))

#uso de metodos de estadistica descriptiva para una sola columna
media_pesos=datos_df["Peso"].mean()
print(f"\nLa media de los pesos es: {media_pesos}")
media_pesos_2=datos_df.mean()["Peso"]
print(f"\nLa media de los pesos es: {media_pesos_2}")

#persistencia y recuperacion de un dataframe
dict_datos={"Peso":[87,78,45,22,90],"Estatura":[121,180,199,150,165],"Edad":[22,19,18,34,67]}
datos_df=pd.DataFrame(dict_datos)
print(datos_df)

"""
Ejemplo que exporta el contenido de un DataFrame a un CSV incluyendo
encabezados y valores del índice
"""
datos_df.to_csv(r'df_en_csv.csv',header=True,index=True)
"""
Ejemplo que exporta el contenido de un DataFrame a un CSV incluyendo
encabezados pero no valores del índice
"""
datos_df.to_csv(r'df_en_csv_2.csv',header=True,index=False)