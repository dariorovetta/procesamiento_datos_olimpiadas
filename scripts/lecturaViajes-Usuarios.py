# Importamos librerias necesarias
import pandas as pd
import os
from datetime import datetime

# Acceder a la ruta donde se encuentra los archivos
ruta = os.getcwd()

# Leemos el archivo .csv
df = pd.read_csv(ruta+r"\Sheet Combinados\Merge Viajes - Usuarios.csv")
#print(df.columns)

# Transformar los datos en "str"
df["id_estacion_origen"] = df['id_estacion_origen'].apply(lambda _: str(_))
df["id_estacion_destino"] = df['id_estacion_destino'].apply(lambda _: str(_))
df["genero_usuario"] = df['genero_usuario'].apply(lambda _: str(_))
df["nombre_estacion_origen"] = df['nombre_estacion_origen'].apply(lambda _: str(_))
df["nombre_estacion_destino"] = df['nombre_estacion_destino'].apply(lambda _: str(_))
df["edad_usuario"] = df['edad_usuario'].apply(lambda _: str(_))
df["long_estacion_origen"] = df['long_estacion_origen'].apply(lambda _: str(_))
df["long_estacion_destino"] = df['long_estacion_destino'].apply(lambda _: str(_))
df["lat_estacion_origen"] = df['lat_estacion_origen'].apply(lambda _: str(_))
df["lat_estacion_destino"] = df['lat_estacion_destino'].apply(lambda _: str(_))

# Quitar la parte final "BAEcobici" de las columnas
df["id_estacion_origen"] = df["id_estacion_origen"].apply(lambda x: x.replace("BAEcobici",""))
df["id_estacion_destino"] = df["id_estacion_destino"].apply(lambda x: x.replace("BAEcobici",""))
df["id_recorrido"] = df["id_recorrido"].apply(lambda x: x.replace("BAEcobici",""))

# Quitar los numeros del ID y dejar solo el nombre
df["nombre_estacion_origen"] = df["nombre_estacion_origen"].apply(lambda x: x[6:])
df["nombre_estacion_destino"] = df["nombre_estacion_destino"].apply(lambda x: x[6:])

# Quitar ".0" de la edad
df["edad_usuario"] = df["edad_usuario"].apply(lambda x: x[:-2])
#print(df["edad_usuario"].head(10))

# Eliminar columnas
df = df.drop(columns=['fecha_alta'])
df = df.drop(columns=['hora_alta'])
df = df.drop(columns=['modelo_bicicleta'])

# Traducir los generos de la columna "genero_usuario"
df["genero_usuario"] = df["genero_usuario"].apply(lambda x: x.replace("FEMALE","Femenino"))
df["genero_usuario"] = df["genero_usuario"].apply(lambda x: x.replace("MALE","Masculino"))
df["genero_usuario"] = df["genero_usuario"].apply(lambda x: x.replace("OTHER","Otro"))

# Reemplazar el punto por la coma de las coordenadas
df["long_estacion_origen"] = df["long_estacion_origen"].apply(lambda x: x.replace(".",","))
df["long_estacion_destino"] = df["long_estacion_destino"].apply(lambda x: x.replace(".",","))
df["lat_estacion_origen"] = df["lat_estacion_origen"].apply(lambda x: x.replace(".",","))
df["lat_estacion_destino"] = df["lat_estacion_destino"].apply(lambda x: x.replace(".",","))

# Exportamos el archivo .csv (con los datos modificados)
df.to_csv("Viajes y Usuarios Editado.csv",encoding="utf-8", index=False)
