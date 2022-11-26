import pandas as pd
import numpy as np

zonas = pd.read_excel('Matrices/Códigos de Zonas_tp.xlsx')
df_distancias = pd.read_excel('Matrices/Matriz distancias_tp.xlsx')


df_camion = pd.read_excel('Matrices/Matrices Grupo Mineria_tp.xlsx', sheet_name='Total Toneladas Mineria 2014', usecols=(range(1,10)))

#print(df_camion) ccccc

lista = []
x = 0
y = 0
while y < 9:
        while x < 10:
            conjunto = {}
            conjunto['Origen'] = zonas.iat[x,3]
            conjunto['ID origen'] = zonas.iat[x,0]
            conjunto['Destino'] = zonas.iat[y,3]
            conjunto['ID destino'] = zonas.iat[y,0]
            conjunto['Carga'] = df_camion[(y+1)][x]
            conjunto['Distancia'] = df_distancias[(y+1)][x]
            lista.append(conjunto)
            x += 1
        x = 0
        y += 1

#print(lista) 

""" Lee un la pesteña deseada dentro del excel con criterios de derivabilidad
"""

criterio = pd.read_excel('Matrices/Criterios de derivabilidad_tp.xlsx', sheet_name='MINERIA') 

#print(criterio)

""" 
Calcular Derivabilidad, hacer una lista
    Lee una lista de bibliotecas con informacion de cargas, origen, destino y distancia
    y utiliza criterios de derivavilidad al FFCC para crear una lista nueva similar pero
    con las cargas derivables.
"""

derivable = []
for i in lista:
        con_dic = {}
        con_dic['Origen'] = i['Origen']
        con_dic['ID origen'] = i['ID origen']
        con_dic['Distancia'] = i['Distancia']
        con_dic['ID destino'] = i['ID destino']
        con_dic['Destino'] = i['Destino']
        if 300 > i['Distancia'] >= 200:
            if criterio.iat[2,0] > i['Carga'] >= criterio.iat[3,0] :
                conjunto['Carga'] = i['Carga']*criterio.iat[3,4]
            elif criterio.iat[1,0] > i['Carga'] >= criterio.iat[2,0]:
                conjunto['Carga'] = i['Carga']*criterio.iat[2,4]
            elif criterio.iat[0,0] > i['Carga'] >= criterio.iat[1,0]:
                conjunto['Carga'] = i['Carga']*criterio.iat[1,4]
            elif i['Carga'] >= criterio.iat[0,0]:
                conjunto['Carga'] = i['Carga']*criterio.iat[0,4]
            else:
                con_dic['Carga'] = 0
        elif 400 > i['Distancia'] >= 300:
            if criterio.iat[2,0] > i['Carga'] >= criterio.iat[3,0] :
                con_dic['Carga'] = i['Carga']*criterio.iat[3,3]
            elif criterio.iat[1,0] > i['Carga'] >= criterio.iat[2,0]:
                con_dic['Carga'] = i['Carga']*criterio.iat[2,3]
            elif criterio.iat[0,0] > i['Carga'] >= criterio.iat[1,0]:
                con_dic['Carga'] = i['Carga']*criterio.iat[1,3]
            elif i['Carga'] >= criterio.iat[0,0]:
                con_dic['Carga'] = i['Carga']*criterio.iat[0,3]
            else:
                con_dic['Carga'] = 0
        elif 500 > i['Distancia'] >= 400:
            if criterio.iat[2,0] > i['Carga'] >= criterio.iat[3,0] :
                con_dic['Carga'] = i['Carga']*criterio.iat[3,2]
            elif criterio.iat[1,0] > i['Carga'] >= criterio.iat[2,0]:
                con_dic['Carga'] = i['Carga']*criterio.iat[2,2]
            elif criterio.iat[0,0] > i['Carga'] >= criterio.iat[1,0]:
                con_dic['Carga'] = i['Carga']*criterio.iat[1,2]
            elif i['Carga'] >= criterio.iat[0,0]:
                con_dic['Carga'] = i['Carga']*criterio.iat[0,2]
            else:
                con_dic['Carga'] = 0
        elif i['Distancia'] >= 500:
            if criterio.iat[2,0] > i['Carga'] >= criterio.iat[3,0] :
                con_dic['Carga'] = i['Carga']*criterio.iat[3,1]
            elif criterio.iat[1,0] > i['Carga'] >= criterio.iat[2,0]:
                con_dic['Carga'] = i['Carga']*criterio.iat[2,1]
            elif criterio.iat[0,0] > i['Carga'] >= criterio.iat[1,0]:
                con_dic['Carga'] = i['Carga']*criterio.iat[1,1]
            elif i['Carga'] >= criterio.iat[0,0]:
                con_dic['Carga'] = i['Carga']*criterio.iat[0,1]
            else:
                con_dic['Carga'] = 0
        else:
            con_dic['Carga'] = 0
        derivable.append(con_dic)

#print(derivable)  

""" Lee una lista de biblioteca con información de cargas, origen y destino
    y la transforma en una matriz para poder realizar operación sobre ella.
"""      
matriz = np.zeros((10,10))
for x in derivable:
        q = ((x['ID destino'])-1)
        w = ((x['ID origen'])-1)
        #print(x['ID destino']-1)
        #print(q,w)
        matriz[w][q] = x['Carga']
        
nueva_fila = []
for j in range(10):
    suma = sum([fila[j] for fila in matriz])
    nueva_fila.append(suma)
print(nueva_fila)    

'''
for f in range(10):
    suma= sum(matriz[f])
    print(suma)

'''
#print(matriz)


"""Crea una excel a partir de una matriz OD
    """
df = pd.DataFrame(matriz, index=(range(1,11)), columns=(range(1,11)))

print(len(df))

#df.to_excel('Matrices/Derivabilidad_mineria_4.xlsx')
                          