from componentes.comun.fondo import Fondo
from modelos.juego import Juego
from contexto.juegoContexto import JuegoContexto

class VistaBatalla:
    def __init__(self, root, nombreJugador1, nombreJugador2):
        self.root = root
        self.nombreJugador1 = nombreJugador1
        self.nombreJugador2 = nombreJugador2

        self.configurarVista()

    def configurarVista(self):
        """
        Configura la vista de batalla, incluyendo el fondo y otros elementos.
        """
        self.fondo = Fondo(self.root, "recursos/background-battle.jpg", width=1366, height=768)
        self.canvas = self.fondo.obtenerCanvas()

        contexto  = JuegoContexto(self.root, self.canvas)
        self.juego = Juego(contexto, self.nombreJugador1, self.nombreJugador2)
