import tkinter as tk

from vistas.reglas import VistaReglas
from vistas.batalla import VistaBatalla

from componentes.comun.configuracionVentana import ConfiguracionVentana
from componentes.comun.fondo import Fondo
from componentes.comun.imagen import Imagen

from componentes.inicio.entradas import EntradasVistaInicio
from componentes.inicio.botones import BotonesVistaInicio


class VistaInicio():
    def __init__(self, root):
        self.root = root
        self.canvas = None
        self.config = ConfiguracionVentana(self.root)
        self.fondo = Fondo(self.root, "recursos/background.jpg")
        self.entradas = None
        self.botones = None
        self.configurarVistaInicio()

    def configurarVistaInicio(self):
        self.config.configurar()
        self.fondo.agregarFondo()

        self.canvas = self.fondo.obtenerCanvas()

        self.titulo = Imagen(self.root, "recursos/title.webp", width=480, height=123)
        imagenTitulo = self.titulo.obtenerPhoto()
        self.canvas.create_image(433, 50, image=imagenTitulo, anchor="nw")

        self.entradas = EntradasVistaInicio(self.root, self.canvas)
        self.entradas.mostrarEntradas()
        self.botones = BotonesVistaInicio(self.root, self.mostrarVistaBatalla, self.mostarVistaReglas)
        self.botones.mostrarBotones()

    def mostrarVistaBatalla(self):
        rootBatalla = tk.Toplevel()

        nombreJugador1 = self.entradas.entradaNombreJugador1.get()
        nombreJugador2 = self.entradas.entradaNombreJugador2.get()

        if nombreJugador1 == "":
            nombreJugador1 = "Jugador 1"

        if nombreJugador2 == "":
            nombreJugador2 = "Jugador 2"

        VistaBatalla(rootBatalla, nombreJugador1, nombreJugador2)
        rootBatalla.mainloop()

    def mostarVistaReglas(self):
        rootReglas = tk.Toplevel()
        VistaReglas(rootReglas)
        rootReglas.mainloop()
