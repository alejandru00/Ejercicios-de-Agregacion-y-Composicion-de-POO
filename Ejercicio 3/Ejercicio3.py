
"""
Enunciado 1: comenzando con el mismo código que el ejercicio sobre herencia múltiple, 
    cree una clase que agrupe el comportamiento común entre las clases Ventana y ParedCortina.
"""

# Creamos la clase Pared:
class pared:
    def __init__(self, orientacion):
        self.orientacion = orientacion
        self.ventana = []

#Creamos la clase Cristal:
class cristal:
    def __init__(self, tipo):
        self.tipo = tipo

#Creamos la clase Ventana:
class ventana:
    def __init__(self, pared, superficie, cristal):
        self.oared = pared
        self.superficie = superficie
        self-pared.ventana.append(self)
        if cristal is None:
            raise Exception("Es obligatorio el cristal")    

#Creamos la clase Casa:
class casa:
    def __init__(self, paredes):
        self.paredes = paredes

    def superficie_acristalada(self):
        return sum([v.superficie for p in self.paredes for v in p.ventanas])
    
#Creamos paredcortina:
class paredcortina(pared, cristal):
    def __init__(self, orientacion, superficie, tipo_cristal):
        pared.__init__(self, orientacion)
        cristal.__init__(self, tipo_cristal)
        self.superficie = superficie


"""
Enunciado 2: modifique las clases Ventana y ParedCortina para que usen esta nueva clase-interfaz Cristal.
"""
pared_norte = pared("norte")
pared_sur = pared("sur")
pared_este = pared("este")
pared_oeste = pared("oeste")

cristal_simple = cristal("simple")  
cristal_doble = cristal("doble")

ventana_norte = ventana(pared_norte, 0.5, cristal_simple)
ventana_sur = ventana(pared_sur, 2, cristal_doble)
ventana_este = ventana(pared_este, 1, cristal_simple)
ventana_oeste = ventana(pared_oeste, 1, cristal_doble)

pared_cortina = paredcortina("sur", 3, cristal_simple)

casa = casa([pared_norte, pared_sur, pared_este, pared_oeste, pared_cortina])


""" 
Enunciado 3: modifique el código para que el programa funcione de nuevo.
"""
print(casa.superficie_acristalada())