

# Definimos la clase empresa
class empresa:
    def __init__(self):
        self.edificio_A = "edificio_A"
        self.edificio_B = "edificio_B"
        self.edificio_C = "edificio_C"

        self.empleados_NewYork = ["Martin", "Salim"]
        self.empleados_LosAngeles = ["Xing"]
        

class destruir(empresa):
    def __init__(self):
        super().__init__()

    def destruir_NewYork(self):
        print(f"Al destruir New York se destruyen los edificios {self.edificio_A} y {self.edificio_B} y los empleados {self.empleados_NewYork}")
