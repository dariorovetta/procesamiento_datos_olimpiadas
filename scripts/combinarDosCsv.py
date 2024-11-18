# Importamos librerias necesarias
import pandas as pd
import os

# Acceder a la ruta donde se encuentra los archivos
ruta = os.getcwd()

# Leemos el archivo .csv
leer1 = pd.read_excel(ruta+r"\Sheet Originales\Usuarios.xlsx")
#print(leer1.columns)

leer2 = pd.read_csv(ruta+r"\Sheet Editados\UsuariosEditados.csv")
#print(leer2.columns)

# Combinarlos con Merge
df = pd.merge(leer2, leer1, on="id_usuario")
df.to_csv("Merge Viajes - Usuarios.csv", index=False)