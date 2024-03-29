import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
archivo_csv = 'data.csv'
df = pd.read_csv(archivo_csv)
# Asegúrate de que la columna 'Penalties' está en el formato correcto (numérico)
df['Penalties'] = pd.to_numeric(df['Penalties'], errors='coerce')

# Calcula el percentil 90 de la valoración
percentile_90 = df['Overall'].quantile(0.9)

# Encuentra el jugador que tiene más valoración que el 90% de los jugadores[^1^][1]
player_90 = df[df['Overall'] > percentile_90]

# Valoración en penalties del jugador
penalties_value = player_90['Penalties'].max()

print(f"La valoración en penalties del jugador que tiene más valoración que el 90% de los jugadores es {penalties_value}")

# Calcula el porcentaje de jugadores que tienen más de 85 de valoración en penalties
players_above_85 = df[df['Penalties'] > 85]
percentage = (len(players_above_85) / len(df)) * 100

print(f"El {percentage}% de los jugadores tiene más de 85 de valoración en penalties")

