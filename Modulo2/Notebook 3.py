# Funciones y Estructuras de control

# Escribi una función que tome dos números enteros y calcule su división, devolviendo si la división es exacta o no.

#def division():

def division(a, b):
  return f"La división es {'exacta' if a % b == 0 else 'inexacta'}. Cociente: {a // b}"
{}



def division(dividendo, divisor):
  """
  Calcula la división entre dos números enteros y determina si es exacta.

  Args:
    dividendo: El número que se va a dividir.
    divisor: El número por el que se va a dividir.

  Returns:
    Un mensaje indicando si la división es exacta o no, junto con el cociente y el resto.
  """

  cociente = dividendo // divisor
  resto = dividendo % divisor

  if resto == 0:
    return f"La división es exacta. Cociente: {cociente}"
  else:
    return f"La división no es exacta. Cociente: {cociente}, Resto: {resto}"

# Ejemplo de uso:
resultado = division(4, 2)
print(resultado)  # Imprime: La división es exacta. Cociente: 2



# Función para verificar si un año es bisiesto
def bisiesto(a):
    if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
        return True
    return False



# Función para resolver una ecuación de primer grado (ax + b = 0)
def solucion(a, b):
    if a == 0:
        return "No tiene solución" if b != 0 else "Infinitas soluciones"
    return -b / a



# Función que simula un juego de dados entre dos jugadores
import random
def juego(jugador1, jugador2):
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    print(f"{jugador1} tira: {dado1}")
    print(f"{jugador2} tira: {dado2}")
    if dado1 > dado2:
        return f"{jugador1} gana"
    elif dado2 > dado1:
        return f"{jugador2} gana"
    else:
        return "Empate"



# Función para determinar qué número es par y cuál impar
def par_impar(a, b):
    resultado = {}
    resultado[a] = "par" if a % 2 == 0 else "impar"
    resultado[b] = "par" if b % 2 == 0 else "impar"
    return resultado



# Función para sumar los números de una lista
def suma_numeros(lista):
    return sum(lista)



# Función que verifica si dos palabras riman
def riman(palabra1, palabra2):
    if palabra1[-3:] == palabra2[-3:]:
        return "Riman"
    elif palabra1[-2:] == palabra2[-2:]:
        return "Riman un poco"
    else:
        return "No riman"



# Función para convertir grados Celsius a Fahrenheit
def convert_grados(grados):
    return grados * 9/5 + 32



# Función que devuelve la serie de Fibonacci entre 0 y 50
def fibo():
    fibonacci = [0, 1]
    while True:
        proximo = fibonacci[-1] + fibonacci[-2]
        if proximo > 50:
            break
        fibonacci.append(proximo)
    return fibonacci
