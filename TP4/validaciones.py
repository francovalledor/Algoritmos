def es_una_palabra(cadena):
    """
    Comprueba si un objeto es una palabra
    """
    LETRAS_VALIDAS = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

    if not (type(cadena) == str):
        return False

    for caracter in cadena:
        if caracter not in LETRAS_VALIDAS:
            return False

    return True

def es_entero(elemento):
    """
    Determinar si el elemento es un numero entero
    """
    if not ((type(elemento) == int) or (type(elemento) == float)):
        return False
    elif (elemento % 1 != 0):
        return False   
    elif (elemento % 1 == 0):
        return True

def es_numero(elemento):
    """
    Determinar si un elemento es un numero
    """
    if not ((type(elemento) == int) or (type(elemento) == float)):
        return False
    else:
        return True

    