---------------------------------------
# Calculadora Numeros Complejos

**Una calculadora construida apartir del lenguaje Python que tienen varias funcionalidades.**

Generalidades:

Un numero complejo es una expresion compuesta por numeros reales y un numero imaginario:

c = a + b * *i*


donde a, b son numeros que pertenecen a los reales.

En esta calculadora estan representados como:


c = ( a , b )


donde b es el termino real que acompaña a la parte imaginaria de la expresion.

# COMO USAR

Esta libreria esta programada en la version de Python 3.7.4 y funciona para las versiones 3.7.* 
Debe tener instalado un entorno de desarrollo o un editor de texto donde se pueda compilar el archivo.

Si no posee uno puede ingresar a https://www.python.org/ para descargar la ultima version.


Despues de tenerlo, puede crear un archivo .py en el mismo directorio del archivo Calculadora.py

Importe la libreria en el nuevo archivo y use las operaciones de manera directa
Por ejemplo el siguiente codigo le indicara la suma de 2 complejos:

`import Calculadora`

`a=Calculadora.suma((1,0),(2,1))`

`print(a)`

Producira un resultado:

`(3,1)`

En caso de que tenga problemas puede ejecutar el archivo Pruebas.py para ejecutar las pruebas establecidas.
En el repositorio existe un archivo Entradas_Manuales en las que puede ver codigo que le puede ayudar a hacer lectura de datos para la calculadora por teclado; tambien esta el archivo Casos_Prueba si desea usar el archivo de Entradas_Manuales para probar casos de prueba.

### Como usarlo por consola?

Si desea usarlo por consola, ubique la consola en la carpeta donde esta el archivo Calculadora.py y escriba en la consola

        $ py Calculadora.py

Para ejecutar las pruebas escriba en la consola

        $ py Pruebas.py
        
Puede ejecutar el idle de python si escribe

        $ py

Estando en el directorio puede ejecutar 

        import Calculadora
        Calculadora.suma((1,0),(2,1))
        
Y el resultado sera:

        (3, 1)

## FUNCIONALIDADES:
* Sencillas
    - Sumar
    - Restar
    - Multiplicar
    - Dividir
    - Conjugado
* Conversion
    - Fase
    - Modulo
    - De Polar a Cartesiano
    - De Cartesiano a Polar
* Espacios Vectoriales Complejos
    - Sumar vectores
    - Sumar matrices
    - Determinar Inverso (vector y matriz)
    - Multiplicar escalar por vector
    - Multiplicar escalar por matriz
    - Determinar Matriz Transpuesta
    - Determinar Matriz Conjugada
    - Determinar Matriz Adjunta
    - Multiplicar Matrices
    - Determinar la accion de una matriz sobre un vector
    - Hallar la suma de la diagonal de una matriz
    - Calcular el producto interno de 2 matrices
    - Hallar la norma de una matriz
    - Calcular la distancia entre 2 matrices
    - Generar una matriz Identidad por su tamaño
    - Determinar si una matriz es Unitaria
    - Determinar si una matriz es Hermitian
    - Hallar el producto tensor entre dos matrices
    
    
## BIBLIOGRAFIA:


        > Quantum Computing For Computer Scientists 
        Noson S. Yanofsky 
        Mirco A. Mannucci
    
    
    
*Por: Michael Ballesteros*
