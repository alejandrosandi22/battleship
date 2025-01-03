import tkinter as tk
import customtkinter as ctk
from componentes.comun.fondo import Fondo

class ModalJuegoTerminado:
    def __init__(self, root, jugadorGanador, comandoFinalizar):
        self.root = root
        self.canvas = None
        self.jugadorGanador = jugadorGanador
        self.comandoFinalizar = comandoFinalizar
        self.configuracionVentana()

    def configuracionVentana(self):
        """
        Configura la ventana modal: título, tamaño, fondo y componentes.
        """
        self.root.title("BattleShip")
        self.root.geometry("426x280+470+244")
        self.root.configure(bg="#292D2B")

        self.fondo = Fondo(self.root, "recursos/background-finish.jpg", width=426, height=280)
        self.canvas = self.fondo.obtenerCanvas()
    
        self.mostrarTitulo()

    def mostrarTitulo(self):
        """
        Muestra el título y el nombre del jugador ganador en la ventana modal.
        """
        self.canvas.create_text(213, 30, text="¡Ganador!", fill="#E8DF5C", font=("Arial", 20, "bold"), anchor="center")
        self.canvas.create_text(213, 70, text=f"{self.jugadorGanador}", font=("Arial", 14, "bold"), fill="#F5F6FF", anchor="center")

        botonFinalizar = ctk.CTkButton(self.root, text="Finalizar", font=("Arial", 14, "bold"), command=self.comandoFinalizar)
        botonFinalizar.place(x=213, y=190, anchor="center")
