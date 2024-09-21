# importar librerías necesarias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Leer el archivo CSV
blackfriday = pd.read_csv('blackfriday.csv')

# Exploración inicial de datos
print(blackfriday.head())
print(blackfriday.shape)
print(blackfriday.columns)
print(blackfriday.dtypes)
print(blackfriday.isna().sum())
print(blackfriday[blackfriday.isna().any(axis=1)])
print(blackfriday[blackfriday['Gender'].isna()])
print(blackfriday.describe())

# Análisis de columnas específicas
print(blackfriday["City_Category"].value_counts())
print(blackfriday["City_Category"].value_counts(normalize=True))
print(blackfriday["Marital_Status"].value_counts(normalize=True))
print(blackfriday['Stay_In_Current_City_Years'].unique())
print(blackfriday['Stay_In_Current_City_Years'].value_counts())

# Limpieza y transformación de datos
blackfriday['Stay_In_Current_City_Years'] = blackfriday['Stay_In_Current_City_Years'].str.replace('4+', '4', regex=False).astype(int)

# Consultas específicas
print(blackfriday[(blackfriday["City_Category"] == 'A') & (blackfriday["Marital_Status"] == 0)]["Purchase"].max())
print(blackfriday[(blackfriday["City_Category"] == 'A') & (blackfriday["Marital_Status"] == 0)]["Purchase"].min())
print(blackfriday[(blackfriday["Gender"] == 'F') & (blackfriday["Marital_Status"] == 0)]["Purchase"].max())

# Agrupación de datos
print(blackfriday.groupby(by=['City_Category', 'Gender'])['Purchase'].mean())

# Tablas cruzadas
print(pd.crosstab(blackfriday["City_Category"], blackfriday["Product_Category_1"]))

# Revisión de tipos de datos
print(blackfriday.dtypes)

# Visualización de datos

# 1. Histograma de compras
plt.figure()
plt.hist(blackfriday['Purchase'].dropna(), bins=10, color="blue", alpha=0.3)
plt.ylabel("Cantidad", size=14)
plt.xlabel("Monto de la compra", size=14)
plt.title("Distribución del monto de la compra realizado por los clientes", size=16, pad=25)
plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)
plt.grid(False)
plt.show()

# 2. Histograma de edades
plt.figure()
plt.hist(blackfriday['Age'].dropna(), bins=10, color="orange", alpha=0.3)
plt.ylabel("Cantidad", size=14)
plt.xlabel("Edad", size=14)
plt.title("Distribución de la edad de los clientes", size=16, pad=25)
plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)
plt.grid(False)
plt.show()

# 3. Distribución del monto de compra usando Seaborn
plt.figure()
sns.displot(blackfriday["Purchase"], color="#5ea88e", kde=True)
plt.xlabel('Monto de la compra')
plt.ylabel('Frecuencia')
sns.despine()
plt.show()

# 4. Boxplot de compras según categoría de ciudad
boxplot_blackfriday = blackfriday.melt(id_vars='City_Category', value_vars=['Purchase'])
plt.figure(figsize=(6, 4))
sns.boxplot(x="variable", y="value", data=boxplot_blackfriday, palette="Set2", hue='City_Category')
plt.title('Monto según categoría de ciudad', size=14, pad=15)
plt.legend(loc='best', frameon=False)
plt.xlabel('Ciudad', size=12)
plt.ylabel('Monto', size=12)
sns.despine()
plt.show()

# 5. Scatterplot de edad vs monto de compra
plt.figure()
sns.scatterplot(x="Age", y="Purchase", data=blackfriday, palette="spring")
sns.despine()
plt.show()

# 6. Gráfico de conteo por ocupación
plt.figure(figsize=(10,5))
sns.countplot(x="Occupation", data=blackfriday.sort_values('Occupation'), palette="Set3")
plt.ylabel("Eventos", size=14)
plt.xlabel("Ocupación", size=14)
plt.title("Distribución de la variable ocupación", size=16, pad=25)
plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)
plt.grid(False)
plt.show()

# 7. Gráfico de conteo por género
plt.figure(figsize=(10,5))
sns.countplot(x="Gender", data=blackfriday, palette="Set3")
plt.ylabel("Eventos", size=14)
plt.xlabel("Género", size=14)
plt.title("Distribución de la variable género", size=16, pad=25)
plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)
plt.grid(False)
plt.show()

# 8. Distribución de compras por categoría de ciudad
plt.figure()
sns.displot(blackfriday[blackfriday['City_Category'] == 'A']["Purchase"], color="#a8685e", kde=True)
sns.displot(blackfriday[blackfriday['City_Category'] == 'B']["Purchase"], color="#5ea88e", kde=True)
sns.displot(blackfriday[blackfriday['City_Category'] == 'C']["Purchase"], color="#0f0752", kde=True)
plt.xlabel('Monto de la compra')
plt.ylabel('Frecuencia')
sns.despine()
plt.show()

# 9. Subplots para diferentes categorías de ciudad
fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(10, 4))
ax[0].hist(blackfriday[blackfriday['City_Category'] == 'A']["Purchase"], color="#a8685e", alpha=0.5, bins=15)
ax[1].hist(blackfriday[blackfriday['City_Category'] == 'B']["Purchase"], color="#5ea88e", alpha=0.4, bins=20)
ax[2].hist(blackfriday[blackfriday['City_Category'] == 'C']["Purchase"], color="#0f0752", alpha=0.4,  bins=25)
for i in range(3):
    ax[i].spines["top"].set_visible(False)
    ax[i].spines["right"].set_visible(False)
plt.show()

# 10. Pairplot y heatmap de correlación
sns.pairplot(blackfriday[['Stay_In_Current_City_Years', 'Age', 'Purchase', 'Gender']], hue='Gender', palette='PuRd')
corr = blackfriday[['Age', 'Stay_In_Current_City_Years', 'Purchase']].corr(method='pearson')
sns.heatmap(corr, cmap='YlGnBu', annot=True)
plt.show()
