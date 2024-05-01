"""
/*
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */
```
"""
# Función sin parámetros ni retorno
def saludar():
    print("¡Hola!")

# Función con un parámetro y retorno
def cuadrado(numero):
    return numero * numero

# Función con varios parámetros y retorno
def suma(a, b):
    return a + b

# Función que crea funciones dentro de funciones
def crear_funcion():
    def funcion_interna():
        print("¡Soy una función dentro de otra función!")
    return funcion_interna

# Utilización de una función ya creada en Python
import math

# Función que prueba el concepto de variable LOCAL y GLOBAL
def prueba_variables():
    global variable_global
    variable_local = 10
    variable_global = 20
    print("Variable local dentro de la función:", variable_local)
    print("Variable global dentro de la función:", variable_global)

# Llamada a las funciones y pruebas
saludar()
print("El cuadrado de 4 es:", cuadrado(4))
print("La suma de 3 y 5 es:", suma(3, 5))

# Crear y llamar una función interna
nueva_funcion = crear_funcion()
nueva_funcion()

# Utilización de una función de la librería math
print("El valor de PI es:", math.pi)

# Prueba de variables locales y globales
variable_global = 0
prueba_variables()
print("Variable global fuera de la función:", variable_global)
