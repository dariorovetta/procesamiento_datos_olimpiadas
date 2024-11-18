# Importamos librerias necesarias
import pandas as pd
import os

# Acceder a la ruta donde se encuentra los archivos
ruta = os.getcwd()

# Leemos el archivo .csv
df = pd.read_csv(ruta+r"\Sheet Originales\Usuarios.csv")

# Leer los nombres de las columnas
print(df.columns)

# Hacemos una impresión para verificar que se leyo el archivo
#print(df)

# Quitamos las filas de la columna "LINEA DE PEDIDO" que su valor sea mayor a 1
#df_quitar = df.drop(df.loc[df["LINEA DE PEDIDO"]>1].index)

# Hacemos una impresión para verificar que se quitaron las filas
# print(df_quitar)

# Exportamos el archivo .xlsx (con los datos modificados)
#df_quitar.to_excel("Ventas Joined Modificado.xlsx", index=False)