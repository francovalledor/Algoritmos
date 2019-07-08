class pilas(list):
    """
    Clase pilas
    """
    def __init__(self, *lista):
        self.elementos = list()
        for elemento in lista:
            self.elementos =  self.elementos + [elemento]
    
    def __len__(self):
        """
        Cuantos elementos quedan en la lista
        """
        return len(self.elementos)

    def __getitem__(self, key):
        """
        Sobrecarga de operadores []
        """
        return self.elementos[key]

    def __add__(self, otra):
        """
        Como se suman dos pilas
        """
        nueva_pila = pilas()
        nueva_pila.elementos =  self.elementos + otra.elementos[::-1] 
        return nueva_pila
    
    def __str__(self):
        """
        Como se imprime una pila
        """
        cadena = ""
        for elemento in self.elementos:
            cadena = cadena + ", " + str(elemento)
        return cadena


def es_tipo_pilas(pila):
    """
    Comprueba si el objeto es una instancia de pilas
    """
    if not (pila is pilas):
            raise TypeError("El primer argumento debe ser una instancia de  'pilas'")

def nueva(*lista):
    """
    Crea una nueva pila y la devuelve
    """
    pila = pilas()
    for elemento in lista:
        pila.elementos = pila.elementos + [elemento]
    return pila

def agregar(pila, elemento, *lista):
    """
    Agrega un elemento a la cima de la pila
    """
    es_tipo_pilas(pila)

    pila.elementos = pila.elementos + [elemento]
    for elemento in lista:
        pila.elementos = pila.elementos + [elemento]

def obtener(pila):
    """
    Devuelve el elemento de la cima de la pila
    """
    es_tipo_pilas(pila)
    elemento = pila.elementos[-1]
    del pila.elementos[-1]
    return elemento

def quedan(pila):
    """
    Cuantos elementos quedan en la pila?
    """
    es_tipo_pilas(pila)
    return len(pila.elementos)

def esta_vacia(pila):
    """
    La pila esta vacia?
    """
    es_tipo_pilas(pila)
    if pila.elementos:
        return True
    else:
        return False

