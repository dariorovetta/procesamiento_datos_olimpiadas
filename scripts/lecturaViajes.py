# Importamos librerias necesarias
import pandas as pd
import os
from datetime import datetime

# Acceder a la ruta donde se encuentra los archivos
ruta = os.getcwd()

# Leemos el archivo .csv
df = pd.read_csv(ruta+r"\Sheet Originales\Viajes.csv")

# Crear una nueva columna, con los datos de otra
mesViaje = df["fecha_origen_recorrido"]
df = df.assign(mes_de_viaje=mesViaje.values)


# Transformar los datos en "str"
df["mes_de_viaje"] = df['mes_de_viaje'].apply(lambda _: str(_))

# Quedarme solo con el mes
df["mes_de_viaje"] = df["mes_de_viaje"].apply(lambda x: x[5:7])

# Dejamos solo los campos del mes "06"
df = df.drop(df.loc[df["mes_de_viaje"]!="06"].index)

# Eliminar columna de 'mes_de_viaje'
df = df.drop(columns=['mes_de_viaje'])

# Quitar la parte final "BAEcobici" de la columna "id_usuario"
df["id_usuario"] = df["id_usuario"].apply(lambda x: x.replace("BAEcobici",""))

# Transformar los datos en "int"
df["id_usuario"] = df['id_usuario'].apply(lambda _: int(_))

# Exportamos el archivo .csv (con los datos modificados)
df.to_csv("UsuariosEditados.csv", index=False)