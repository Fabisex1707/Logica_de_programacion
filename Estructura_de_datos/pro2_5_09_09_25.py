#uso de padas y la cotrcccio de series
#Una serie es un array, un array es un conjuto de datos del mismo tipo, se diferecia de la lista en que la lista acepta diferentes tipos de datos 
import pandas as pd
#datos para la serie
data_lista=[10,20,30]
#creacion de la serie
data_serie=pd.Series(data_lista)
#acceso a un dato de la serie por su indice
print(data_serie[0])
#Tipo de dato de un solo dato en la serie
print(type(data_serie[0]))
#creacion de la variable para guardar las etiquetas de los indices
index_personalizado=["Fabi","Marta","Carlos"]
#asigancion de las etiquetas a los indices
data_serie.index=index_personalizado
#vista con las etiquetas
print(data_serie)
#Acceso de a los datos por medio de las etiquetas
print(data_serie["Fabi"])
#Acceso a un dato inexistente por medio de etiquetas # KeyError
#data_serie["Felipe"]

