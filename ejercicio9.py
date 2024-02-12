class Gasto:
    def __init__(self, categoria, monto):
        self.categoria = categoria
        self.monto = monto

class SistemaGastos:
    def __init__(self):
        self.gastos = []

    def ingresar_gasto(self, categoria, monto):
        nuevo_gasto = Gasto(categoria, monto)
        self.gastos.append(nuevo_gasto)

    def calcular_total_categoria(self, categoria):
        total = 0
        for gasto in self.gastos:
            if gasto.categoria == categoria:
                total += gasto.monto
        return total

    def generar_reporte(self):
        categorias = set(gasto.categoria for gasto in self.gastos)
        print("Reporte de gastos:")
        for categoria in categorias:
            total_categoria = self.calcular_total_categoria(categoria)
            print(f"{categoria}: ${total_categoria}")

    def establecer_presupuesto(self, categoria, presupuesto):
        total_categoria = self.calcular_total_categoria(categoria)
        if total_categoria > presupuesto:
            print(f"¡Cuidado! Has excedido el presupuesto para la categoría {categoria}")
        else:
            print(f"¡Bien hecho! Estás dentro del presupuesto para la categoría {categoria}")

# Ejemplo de uso del sistema de gastos
sistema = SistemaGastos()
sistema.ingresar_gasto("Comida", 20000)
sistema.ingresar_gasto("Transporte", 2700)
sistema.ingresar_gasto("Comida", 25000)
sistema.ingresar_gasto("Entretenimiento", 100)

sistema.generar_reporte()
sistema.establecer_presupuesto("Comida", 50000)