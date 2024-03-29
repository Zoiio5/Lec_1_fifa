import pandas as pd
archivo_csv = 'data.csv'
df = pd.read_csv(archivo_csv)

# Asegúrate de que la columna 'Age' sea numérica
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')

# Calcula la media y la desviación estándar
media = df['Age'].mean()
desviacion_estandar = df['Age'].std()

print(f'La media de las edades es: {media}')
print(f'La desviación estándar de las edades es: {desviacion_estandar}')
