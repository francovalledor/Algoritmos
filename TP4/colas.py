class colas(list):
    """
    Clase colas
    """
    def __init__(self, *lista):
        self.elementos = list()
        for elemento in lista:
            self.elementos = [elemento] + self.elementos
    
    def __len__(self):
        return len(self.elementos)

    def __getitem__(self, key):
        return self.elementos[key]

    def __add__(self, otra):
        self.elementos = otra.elementos + self.elementos
    
    def __str__(self):
        cadena = ""
        for elemento in self.elementos[::-1]:
            cadena = cadena + ", " + str(elemento)
        return cadena


def es_tipo_colas(cola):
    """
    Comprueba si el objeto es una instancia de colas
    """
    if not (cola is colas):
            raise TypeError("El primer argumento debe ser una instancia de  'colas'")

def nueva(*lista):
    """
    Crea una nueva cola y la devuelve
    """
    cola = colas()
    for elemento in lista:
        cola.elementos = [elemento] + cola.elementos
    return cola

def agregar(cola, elemento, *lista):
    """
    Agrega un elemento al final de la cola
    """
    es_tipo_colas(cola)

    cola.elementos = [elemento] + cola.elementos
    for elemento in lista:
        cola.elementos = [elemento] + cola.elementos

def obtener(cola):
    """
    Devuelve el primer elemento de la cola
    """
    es_tipo_colas(cola)
    es_tipo_colas(cola)
    elemento = cola.elementos[-1]
    del cola.elementos[-1]
    return elemento

def quedan(cola):
    """
    Cuantos elementos quedan en la cola?
    """
    es_tipo_colas(cola)
    return len(cola.elementos)

def esta_vacia(cola):
    """
    La cola esta vacia?
    """
    es_tipo_colas(cola)
    if cola.elementos:
        return True
    else:
        return False

