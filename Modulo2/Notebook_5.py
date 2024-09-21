


import numpy as np

# 1. Crear un arreglo de ceros de longitud 12
arreglo_ceros = np.zeros(12)
print("1. Arreglo de ceros:", arreglo_ceros)

# 2. Crear un arreglo de longitud 10 con ceros en todas sus posiciones y un 10 en la posición número 5
arreglo_diez = np.zeros(10)
arreglo_diez[5] = 10
print("2. Arreglo con un 10 en la posición 5:", arreglo_diez)

# 3. Crear un arreglo que tenga los números del 10 al 49
arreglo_10_49 = np.arange(10, 50)
print("3. Arreglo del 10 al 49:", arreglo_10_49)

# 4. Crear una arreglo 2D de shape (3, 3) que tenga los números del 0 al 8
arreglo_2d = np.arange(9).reshape(3, 3)
print("4. Arreglo 2D (3x3) del 0 al 8:\n", arreglo_2d)

# 5. Crear un arreglo de números aleatorios de longitud 100 y obtener su media y varianza
arreglo_aleatorio = np.random.rand(100)
media = np.mean(arreglo_aleatorio)
varianza = np.var(arreglo_aleatorio)
print(f"5. Arreglo aleatorio, Media: {media:.3f}, Varianza: {varianza:.3f}")

# 6. Calcular la media de un arreglo usando np.sum
media_sum = np.sum(arreglo_aleatorio) / len(arreglo_aleatorio)
print(f"6. Media usando np.sum: {media_sum:.3f}")

# 7. Calcular la varianza de un arreglo usando np.sum y np.mean
media_arreglo = np.mean(arreglo_aleatorio)
varianza_sum = np.sum((arreglo_aleatorio - media_arreglo) ** 2) / len(arreglo_aleatorio)
print(f"7. Varianza usando np.sum y np.mean: {varianza_sum:.3f}")

# 8. Crear un array de números aleatorios usando np.random.randn
arreglo_randn = np.random.randn(100)
print("8. Arreglo de números aleatorios con np.random.randn:", arreglo_randn)
