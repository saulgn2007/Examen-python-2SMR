# Ejercicio 1
# Escribe una función que reciba tres números y devuelva el mayor de ellos en un 
# mensaje impreso en pantalla.

def mayor(a,b,c):
    if (a > b & a > c):
        print ("El numero mayor es: " , a )
    elif (b > a & b > c):
        print ("El numero mayor es: " , b)
    else:
        print ("El numero mayor es: ", c)
mayor(5,2,10)

# Ejercicio 2
# Escribe una función que reciba dos números enteros e imprima todos los números pares 
# en ese rango, incluídos los dos extremos.

def pares(a,b):
    for i in range(a,b+1):
        if (i % 2 == 0):
            return "Numero pares: " , i
print(pares(3,10))
            
            
# Ejercicio 3 
# Escribe una función que reciba una lista de números y devuelva una nueva lista 
# con cada número multiplicado por 2.

def duplicar_lista():
    lista = [2,4,6,8]
    for i in range(lista+1):
        i = lista * 2
        return i
    
print(duplicar_lista)


# Ejercicio 4
# Crea una función que reciba un diccionario y devuelva otro con claves y 
# valores intercambiados.

def valores_intercambiados():
    diccionario = { "a":1,"b":2}
    for i in (diccionario):
        
        return i
print(valores_intercambiados())


# Ejercicio 5
# Escribe una función recursiva que reciba una cadena y un índice incrementable, y 
# cuente la longitud de la cadena.

# def longitud_cadena():

# pritn (longitud_cadena())
