import colas
import pilas
import validaciones

def eliminar_vocales(cola):
    """
    Eliminar las vocales de una cola
    """
    VOCALES = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    colas.es_tipo_colas(cola)
    aux = colas.colas()
    while not colas.quedan(cola):
        elemento_actual = colas.obtener(cola)
        if not (elemento_actual in VOCALES):
            colas.agregar(aux, elemento_actual)
    cola = aux

def invertir_cola(cola):
    """
    Invertir el orden de una cola
    """
    cola_aux = colas.colas() 
    pila_aux = pilas.pilas()
    while colas.quedan(cola):
        ###Devolver cada elemento de la cola
        ### y agregarlo en una pila
        elemento_actual = colas.obtener(cola)
        pilas.agregar(pila_aux, elemento_actual)

    while pilas.quedan(pila_aux):
        ###Devolver cada elemento de la pila
        ### y agregarlo en una cola
        elemento_actual = pilas.obtener(pila_aux)
        colas.agregar(cola_aux, elemento_actual)

    cola = cola_aux


def es_palindromo(palabra):
    """
    Determinar si una palabra es un palindromo
    """
    
    if not validaciones.es_una_palabra(palabra):
        raise TypeError("El argumento no es una palabra")

    cola_palabra = colas.nueva()
    pila_palabra = pilas.nueva()
    
    for letra in palabra:
        colas.agregar(cola_palabra, letra)  
        pilas.agregar(pila_palabra, letra)
    
    while colas.quedan(cola_palabra) and pilas.quedan(pila_palabra):
        if (colas.obtener(cola_palabra) != pilas.obtener(pila_palabra)):
            return False
    
    return True

def eliminar_no_primos(cola):
    """
    Eliminar de una cola los elementos no primos
    """
    def es_primo(numero):
        """
        Determinar si un numero entero es primo
        """
        if not validaciones.es_entero(numero):
            return False
        
        for i in range(2, numero//2):
            if (numero % i == 0) :
                return False
        
        return True
        #FIN es_primo

    cola_aux = colas.colas()
    while colas.quedan(cola):
        elemento_actual = colas.obtener(cola)
        if es_primo(elemento_actual):
            colas.agregar(cola_aux, elemento_actual)


def invertir_pila(pila):
    """
    Invertir el orden de una pila
    """
    pila_aux = pilas.pilas()
    while pilas.quedan(pila):
        pilas.agregar(pila_aux, pilas.obtener(pila))
        ## Me gusta mas: 
        # elemento = pilas.obtener(pila)
        # pilas.agregar(pila_aux, elemento)
    pila = pila_aux


def contar_ocurrencias_cola(cola, elemento):
    """
    Contar la cantidad de ocurrencias de un determinado elemento en una cola, 
    sin utilizarninguna estructura auxiliar
    """
    contador = 0
    for i in range(0, len(cola)):
        actual = colas.obtener(cola) #use una variable para almacenar el elemento, no se si esta bien
        if (actual == elemento):
            contador += 1
        colas.agregar(cola, actual)
    return contador

def eliminar_iesimo(cola, iesimo):
    """
    Eliminar el i-esimo elemento después del frente de la cola.
    """
    if not validaciones.es_entero(iesimo):
        raise TypeError("iesimo debe ser un numero entero")

    ###A bajo nivel
    del cola[-(iesimo + 1)]

    ### Usando las interfaces de colas es un poquito mas complejo
    ### porque se debe obtener y agregar los elementos hasta llegar
    ### al elemento que queremos eliminar, luego se debe obtener y 
    ### agregar para dejar la cola en el mismo orden que estaba al 
    ### principio

    i = 0
    j = colas.quedan(cola) - 1
    while i <= j:
        if i == iesimo:
            colas.obtener(cola)
        else:
            colas.agregar(cola, colas.obtener(cola))
        i += 1

    