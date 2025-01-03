from componentes.comun.configuracionVentana import ConfiguracionVentana
from componentes.reglas.contenido import ContenidoReglas
from componentes.reglas.botonRegresar import BotonRegresar
from componentes.comun.fondo import Fondo

class VistaReglas():
    def __init__(self, root):
        self.root = root
        self.config = ConfiguracionVentana(self.root)
        self.fondo = Fondo(self.root, "recursos/background.jpg")
        self.botonRegresar = BotonRegresar(self.root, self.regresarVistaInicio)
        self.configurarVista()

    def configurarVista(self):
        self.config.configurar()
        self.fondo.agregarFondo()
        self.canvas = self.fondo.obtenerCanvas()
        self.canvas.create_text(683, 100, text="Reglas del Juego", fill="#f5f6ff", font=("Arial", 40, "bold"))
        self.texto = ContenidoReglas(self.root, self.fondo.canvas)
        self.texto.mostrarReglas()
        self.botonRegresar.agregarBoton()

    def regresarVistaInicio(self):
        """
        Cierra la ventana actual y regresa a la vista de inicio.
        """
        self.root.destroy()
