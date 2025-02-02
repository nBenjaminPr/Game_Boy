import pandas as pd

df = pd.read_csv ("C:/Users/Usuario/Desktop/Escriotrio Nico/PYTHON/CODE/Datos parte 2/best-selling-gameboy.csv")



# Dividiremos el DataFrame en dos.
# Primero, dividiremos el DataFrame en dos partes: una para los juegos de Nintendo
df_game_boy = df.query("Platform == 'Game Boy'")
# otra para los juegos de color.
df_game_boy_color = df.query("Platform == 'Game Boy Color'")

# Ordenamos por ventas de mayor a menor e indexamos las 10 primeras posiciones.
df = df_game_boy.sort_values(by = 'Sales', ascending = False).iloc[:10]

# Ordenamos por ventas de mayor a menor e indexamos las 10 primeras posiciones.
df = df_game_boy_color.sort_values(by = 'Sales', ascending = False).iloc[:10]



print (df)
