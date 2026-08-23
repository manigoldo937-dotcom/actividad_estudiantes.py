import pandas as pd

archivo = r"C:\Users\hecto\Downloads\Base_Estudiantes.xlsx"

df = pd.read_excel(archivo)

print(df.head())
print("\nInformación de la base:")
print(df.info())
print("\nValores nulos:")
print(df.isnull().sum())
duplicados = df.duplicated().sum()

print("\nRegistros duplicados:")
print(duplicados)
df.to_excel(
    "Base_Estudiantes_Limpia.xlsx",
    index=False
)

print("\nArchivo limpio creado correctamente.")
promedio_general = df["Promedio"].mean()

print("\nPromedio general del curso:")
print(round(promedio_general, 2))
print("\nEstado de estudiantes:")
print(df["Estado"].value_counts())
import pandas as pd

archivo = r"C:\Users\hecto\Downloads\Base_Estudiantes.xlsx"

df = pd.read_excel(archivo)

print(df.head())

print("\nInformación de la base:")
print(df.info())

print("\nValores nulos:")
print(df.isnull().sum())

duplicados = df.duplicated().sum()

print("\nRegistros duplicados:")
print(duplicados)

promedio_general = df["Promedio"].mean()

print("\nPromedio general:")
print(round(promedio_general, 2))

print("\nEstado de estudiantes:")
print(df["Estado"].value_counts())

df.to_excel(
    "Base_Estudiantes_Limpia.xlsx",
    index=False
)

print("\nArchivo limpio creado correctamente.")