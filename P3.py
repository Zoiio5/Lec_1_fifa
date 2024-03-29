import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

archivo_csv = 'data.csv'
df = pd.read_csv(archivo_csv)

# Asegúrate de que las columnas 'Overall' y 'Value' están en el formato correcto (numérico)
df['Overall'] = pd.to_numeric(df['Overall'], errors='coerce')
df['Value'] = pd.to_numeric(df['Value'], errors='coerce')
# Estadísticos para 'Overall'
overall_stats = df['Overall'].describe()

# Estadísticos para 'Value'
value_stats = df['Value'].describe()

print("Estadísticas para Overall:\n", overall_stats)
print("\nEstadísticas para Value:\n", value_stats)
# Histograma para 'Overall'
plt.figure(figsize=(10, 6))
sns.histplot(df['Overall'], kde=True)
plt.title('Histograma de Overall')
plt.show()

# Histograma para 'Value'
plt.figure(figsize=(10, 6))
sns.histplot(df['Value'], kde=True)
plt.title('Histograma de Value')
plt.show()

# Boxplot para 'Overall'
plt.figure(figsize=(10, 6))
sns.boxplot(x=df['Overall'])
plt.title('Boxplot de Overall')
plt.show()

# Boxplot para 'Value'
plt.figure(figsize=(10, 6))
sns.boxplot(x=df['Value'])
plt.title('Boxplot de Value')
plt.show()
