import pandas as pd

# Ruta completa al archivo CSV
ruta_archivo = '/content/drive/MyDrive/JUMP/Propuestas/Clase 6 - Pandas/StudentsPerformance.csv'

# Leer el archivo CSV (asegúrate de definir 'ruta_archivo')
df = pd.read_csv(ruta_archivo)

# Mostrar las primeras filas del DataFrame
print(df.head())

# 1. Selecciona solo las filas donde math score sea mayor a 70
math_mayor_70 = df[df['math score'] > 70]
print("1. Math score mayor a 70:\n", math_mayor_70)

# 2. Selecciona solo las filas donde reading score sea menor a 60
reading_menor_60 = df[df['reading score'] < 60]
print("2. Reading score menor a 60:\n", reading_menor_60)

# 3. Selecciona solo las filas donde gender sea igual a female
female = df[df['gender'] == 'female']
print("3. Filas donde gender es female:\n", female)

# 4. Selecciona solo aquellas filas donde lunch sea distinto a standard
lunch_no_standard = df[df['lunch'] != 'standard']
print("4. Filas donde lunch es distinto a standard:\n", lunch_no_standard)

# 5. Muestra los valores de writing score para aquellos estudiantes que tengan reading score mayor a math score
writing_score_cond = df[df['reading score'] > df['math score']]['writing score']
print("5. Writing score donde reading > math:\n", writing_score_cond)

# 6. Selecciona aquellos estudiantes que posean reading y writing score mayor a 70
read_write_mayor_70 = df[(df['reading score'] > 70) & (df['writing score'] > 70)]
print("6. Estudiantes con reading y writing mayor a 70:\n", read_write_mayor_70)

# 7. Usa .isnull() para ver qué ocurre
null_values = df.isnull()
print("7. Valores nulos:\n", null_values)

# 8. Usa .isnull().sum() sobre tu dataframe para ver qué devuelve
null_values_sum = df.isnull().sum()
print("8. Suma de valores nulos:\n", null_values_sum)

# 9. Elimina todas las filas que tengan valores faltantes (inplace=True)
df.dropna(inplace=True)
print("9. DataFrame después de eliminar filas con valores nulos:\n", df)

# 10. Usa la función .describe() sobre students y describe qué información estadística proporciona
stats = df.describe()
print("10. Descripción estadística:\n", stats)

# 11. Calcula el promedio de la columna math score de students
promedio_math = df['math score'].mean()
print(f"11. Promedio de math score: {promedio_math:.2f}")

# 12. Calcula el mínimo, máximo, mediana y desviación estándar de la columna math score
min_math = df['math score'].min()
max_math = df['math score'].max()
mediana_math = df['math score'].median()
desvio_math = df['math score'].std()
print(f"12. Math score - Mínimo: {min_math}, Máximo: {max_math}, Mediana: {mediana_math}, Desviación estándar: {desvio_math}")

# 14. Aplicación de diferentes funciones de Pandas:

# .index: Devuelve los índices del DataFrame
print("14. Índices del DataFrame:\n", df.index)

# .drop(): Eliminar una columna o fila (ejemplo eliminando 'Unnamed: 0')
df.drop('Unnamed: 0', axis=1, inplace=True)
print("14. DataFrame después de .drop('Unnamed: 0'):\n", df)

# .groupby(): Agrupar los datos por 'gender' y calcular el promedio de math score
grouped = df.groupby('gender')['math score'].mean()
print("14. Promedio de math score por género:\n", grouped)

# .fillna(): Rellenar valores nulos con un valor específico (ejemplo con 0)
df_filled = df.fillna(0)
print("14. DataFrame con valores nulos rellenos:\n", df_filled)

# .rename(): Renombrar una columna (ejemplo 'gender' a 'sexo')
df.rename(columns={'gender': 'sexo'}, inplace=True)
print("14. DataFrame después de .rename('gender' a 'sexo'):\n", df)

# .astype(): Cambiar el tipo de una columna (ejemplo 'math score' a float)
df['math score'] = df['math score'].astype(float)
print("14. DataFrame después de cambiar el tipo de 'math score' a float:\n", df)

# .unique(): Obtener valores únicos de una columna (ejemplo 'sexo')
unique_genders = df['sexo'].unique()
print("14. Valores únicos en 'sexo':\n", unique_genders)

# .value_counts(): Contar la frecuencia de los valores en una columna (ejemplo 'sexo')
gender_counts = df['sexo'].value_counts()
print("14. Conteo de valores en 'sexo':\n", gender_counts)

# .count(): Contar valores no nulos en cada columna
non_null_counts = df.count()
print("14. Conteo de valores no nulos en cada columna:\n", non_null_counts)

# .reset_index(): Restablecer el índice del DataFrame
df_reset = df.reset_index(drop=True)
print("14. DataFrame después de .reset_index():\n", df_reset)
