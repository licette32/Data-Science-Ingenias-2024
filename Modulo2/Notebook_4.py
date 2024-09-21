# Introducción a Numpy

#Importar numpy
import numpy as np

#creo un array
arr = np.array([10, 11, 12, 13, 14, 15, 16, 17, 18, 19])

#crea una lista llamada mi_lista que contenga 10 numeros

mi_lista = [45,123,89,3,45,2,99,56,34,10]

#Ahora transforma tu lista en un array usando np.array y asignalo a la variable mi_array

mi_array = np.array(mi_lista)
#Imprimi mi_array
print(mi_array)

#Aplica type sobre mi_array para mostrar que tipo de estructura de datos es
type(mi_array)

#Suma 2 a cada elemento de mi_array
mi_lista2 = [i + 2 for i in mi_lista]
print(mi_lista2)


#Corre el siguiente codigo y fijate que pasa
print(mi_lista * 2)


#Ahora multiplica por dos cada elemento de mi_array
mi_lista3 =  [i * 2 for i in mi_lista]
print(mi_lista3)


#Corre el siguiente codigo
lista1 = [1, 2, 3, 4, 5]
lista2 = [5, 4, 3, 2, 1]
#Concatena las dos listas
lista1 + lista2



#Suma los elementos de los dos arrays

#lista3 = []
#for i in lista1:
#  for j in lista2:
#    lista3.append(i + j)
#print(lista3)
lista1 = [1,2,3,4]
lista2 = [9,2,3,4]
array1 = np.array(lista1)
array2 = np.array(lista2)
print(array1 + array2)


# Suma elemento a elemento
suma = array1 + array2
print("Suma:", suma)

# Multiplicación elemento a elemento
multiplicacion = array1 * array2
print("Multiplicación:", multiplicacion)

# Resta elemento a elemento
resta = array1 - array2
print("Resta:", resta)

# División elemento a elemento
division = array1 / array2
print("División:", division)

# Potencia elemento a elemento
potencia = array1 ** array2
print("Potencia:", potencia)

# Obtener el último elemento de array1
ultimo_elemento = array1[-1]
print("Último elemento:", ultimo_elemento)


'''
Para acceder a los elementos de los arrays de una dimension se utilizan los indices como las listas.
'''


#Corre el siguiente codigo
print(lista1[0], arr1[0])


#Obtene el 3er elemento de arr1
print(lista1[2], arr1[2])

#Obtene el 5to elemento de arr2
print (lista2[4], arr2[4])


'''
Asi tambien obtenemos una porción del array de la misma manera que obtenemos una parte de una lista. 
A su vez podemos reasignar nuevos valores a una porción del array.
'''
#Corre el siguiente codigo
array1[2:5] = [22, 23, 24]
#Imprimi el arr1
print(arr1)

'''
## Arreglos multidimensionales
Las listas son cadenas unidimensionales de elementos. Los arreglos pueden ser multidimensionales. 
Para comprender mejor que son, miremos el siguiente ejemplo:
'''
#Corre el siguiente codigo
lista = [[0, 1, 3], [3, 4, 5]]
arr2d = np.array(lista)
arr2d
#Veamos cuantas dimensiones tiene el array
print(arr2d.ndim)
#Veamos cuantos elementos tiene el array
print(arr2d.size)


#Arma ahora un array de 3 dimensiones.
coso = [[[2,4,6],[1,3,5],[8,10,12]]]
arr3d = np.array(coso)
arr3d
#Chequea usando ndim que efectivamente tenga tres dimensiones
print(arr3d.ndim)

'''
**¿Como accedemos entonces a un array de mas de una dimension?**
'''

#definamos un nuevo array
lista2 = [[0, 1, 3], [3, 4, 5], [9, 10, 4], [2, 5, 6]]
nuevo_array = np.array(lista2)

'''
¿Cuantas dimensiones tiene el array `nuevo_array`? Comprobalo usando `ndim`.'''

#Dimensiones de nuevo_array
print(nuevo_array.ndim)
#Mostra nuevo_array
print(nuevo_array)

# Nuevo array multidimensional
lista2 = [[0, 1, 3], [3, 4, 5], [9, 10, 4], [2, 5, 6]]
nuevo_array = np.array(lista2)

# Acceder al tercer elemento de la segunda fila
elemento = nuevo_array[1, 2]
print("Elemento:", elemento)

# Acceder a un subarray
subarray = nuevo_array[1:3, 0:2]
print("Subarray:", subarray)

'''
Si para un array de 1 dimension, usabamos un indice, para un array de n dimensiones tenemos que usar n indices.
 En el caso de 2 dimensiones, usaremos 2 indices. 
El primero indica la fila y el segundo la columna.
'''
#Corre el siguiente codigo
print(nuevo_array[0, 1])
#Accede al tercer elemento de la segunda fila de nuevo_array
print(nuevo_array[1,2])
#Accede al cuarto elemento de la segunda columna de nuevo_array
print(nuevo_array[3,2])
#Accedo a toda la segunda columna
nuevo_array[:, 1]
#Accede a un subarray que vaya desde el segundo elemento de la
#primer columna hasta el cuarto elemento de la tercer
#columna de nuevo_array
print(nuevo_array[: , 2])

'''
CREACIÓN DE ARREGLOS
'''
#**np.zeros(shape, dtype, order)**: Crea un array con todos ceros en sus posiciones
#Corre el siguiente codigo
print(np.zeros((2, 2, 2)))
# **np.ones(shape, dtype, order)**: Crea un array con todos unos en sus posiciones
#Corre el siguiente codigo
print(np.ones(10))

# **np.random.rand(d0, d1, ..., dn)**: Genera un array con valores al azar con una distribución `[0, 1)` y segun las dimensiones pasada como argumento.
#Genera un array con valores al azar
print(np.random.randn(10))



#Genera un array con enteros al azar
np.random.randint(5)
#Corre esta linea de codigo y comprende como funciona np.arange
np.arange(2, 16, 2)

'''
FUNCIONES ESTADISTICAS
'''
#Volvamos a ver como era nuestro array nuevo_array
print(nuevo_array)
#usa la funcion mean para obtener el promedio de los valores en nuevo_array
np.mean(nuevo_array)
#usa la funcion var para obtener la varianza de los valores en nuevo_array
np.var(nuevo_array)
#Muestra la suma de los valores en nuevo_array
np.sum(nuevo_array)

#Muestra el minimo y maximo valor en nuevo array

np.min(nuevo_array)
np.max(nuevo_array)

