from componentes.comun.imagen import Imagen

class ContenidoReglas():
    def __init__(self, root, canvas):
        self.root = root
        self.canvas = canvas

    def mostrarReglas(self):
        reglas = [
            "1. El usuario que impacta un barco puede disparar de nuevo sin perder su turno.",
            "2. Si el disparo cae en el agua, se cambia al siguiente jugador.",
            "3. Los barcos pueden ser colocados manualmente o automáticamente.",
            "4. En el modo automático, las posiciones de los barcos son aleatorias y no se confirma su colocación.",
            "5. Se debe confirmar la distribución de los barcos, ya sea manual o automática.",
            "6. Gana el jugador que destruye primero toda la flota enemiga."
        ]

        posicionY = 200
        for regla in reglas:
            self.canvas.create_text(683, posicionY, text=regla, fill="#f5f6ff", font=("Arial", 16, "bold"))
            posicionY += 40
