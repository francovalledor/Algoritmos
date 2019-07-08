
class Carta:
    def __init__(self, palo, numero):
        if palo in ("espada", "basto", "oro", "copa"):
            self.palo = palo
        else:
            raise TypeError('palo debe ser ["espada", "basto", "oro", "copa"]')
        
        if isinstance(numero, int) and (numero > 0) and ( numero <= 12 ):
            self.numero = numero
        else:
            raise TypeError('palo debe ser ["espada", "basto", "oro", "copa"]')
        
class Mazo:
    def __init__(self):
        self.cartas = list() # = []
    
    def quedan(self):
        """
        Cuantas cartas quedan en el mazo
        """
        return len(self.cartas)
    
    def sacar(self):
        """
        Sacar una carta del mazo
        """
        if self.cartas:
            self.cartas.pop()
        else:
            raise IndexError("No quedan cartas")
    
    def mezclar(self):
        """
        Mezclar las cartas que quedan en el mazo
        """
        from random import shuffle
        shuffle(self.cartas)
    
    def rellenar(self):
        """
        Volver a llenar el mazo
        """
        self.cartas = list()

        for palo in ("espada", "basto", "oro", "copa"):
            for numero in range(1,13):
                self.cartas.append(Carta(palo, numero))
            self.mezclar()

    def partir_en_cuatro    
