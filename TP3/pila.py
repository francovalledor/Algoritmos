class Pila:
    """
    Clase Pila
    ----------
    parametros:
    lista, de, elementos,...
    """
    def __init__(self, *lista):
        self.elementos = list(lista)
        
    def push(self, elemento):
        """
        Agregar un elemento a la pila
        """
        self.elementos.append(elemento)

    def pop(self):
        """
        Devolver el siguiente elemento de la pila
        """
        try:
            return self.elementos.pop()
        except IndexError:
            raise IndexError("No quedan elementos en la lista")
   
    def isEmpty(self):
        """
        Determinar si la pila esta vacia
        """
        if not self.elementos:
            return True
        else:
            return False

    def ocurrencias(self, que_cosa):
        """
        Determinar el número de ocurrencias de un determinado elemento en la pila
        """
        nro_ocurrencias = 0

        #Comprabaciones antes de ciclar
        # Si la pila esta vacia devuelve 0 
        if not self.elementos:
            return 0

        #Comprabaciones antes de ciclar 
        #si que_cosa no esta en la pila devuelve 0
        if not (que_cosa in self.elementos):
            return 0

        for elemento in self.elementos:
            if elemento == que_cosa:
                nro_ocurrencias += 1

        return nro_ocurrencias
    
    
    def eliminar_impares(self):
        """
        Eliminar de una pila todos los elementos impares, 
        es decir que en la misma solo queden numeros pares
        """
        for elemento in self.elementos:
            if isinstance(elemento, int) or isinstance(elemento, float) :
                if (elemento % 2 != 0) and (elemento % 1 == 0)   :
                    self.elementos.remove(elemento)
    
    def reemplazar(self, este_elemento, por_este_otro):
        """
        Reemplazar todas las ocurrencias de un determinado elemento en la pila
        """
        if (este_elemento in self.elementos):
            for i in range(0, len(self.elementos)):
                if self.elementos[i] == este_elemento:
                    self.elementos[i] = por_este_otro
        else:
            raise ValueError("El elemento a reemplazar no se encuentra en la lista")
    
    def invertir(self):
        """
        Invertir el orden de la pila
        """
        self.elementos.reverse()
    
    def eliminar(self, indice):
        """
        Eliminar el i-ésimo elemento debajo de la cima.
        """
        if not isinstance(indice, int):
            raise TypeError("El indice debe ser de tipo int")
        
        if len(self.elementos) < indice:
            raise IndexError("Indice fuera de rango")
        
        del self.elementos[-(1 + indice)]
    





def es_palindromo(palabra):
    """
    Determinar si una cadena de caracteres es un palindromo
    """
    if isinstance(palabra, str):
        palindromo = True
        for i in range(0, (len(palabra) // 2)) :
            if not (palabra[i] == palabra[-(i+1)]):
                palindromo = False
                break
        return palindromo
    else:
        raise TypeError("el argumento debe ser una palabra")            


def mostrar_al_reves():
    """
    Leer una palabra y visualizarla en forma inversa
    """
    palabra = input('Ingrese una palabra: ')
    print(palabra[::-1])

