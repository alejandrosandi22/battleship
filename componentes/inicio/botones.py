import customtkinter as ctk

class BotonesVistaInicio():
    def __init__(self, root, mostrarVistaBatalla, mostarVistaReglas):
        self.root = root
        self.mostrarVistaBatalla = mostrarVistaBatalla
        self.mostarVistaReglas = mostarVistaReglas

    def mostrarBotones(self):
        botonMostrarBatalla = ctk.CTkButton(self.root, text="Iniciar Juego", width=350, height=65, font=("Arial", 24), command=self.mostrarVistaBatalla)
        botonMostrarBatalla.place(x=683, y=520, anchor="center")

        botonMostrarReglas = ctk.CTkButton(self.root, text="Reglas", width=350, height=65, font=("Arial", 24), command=self.mostarVistaReglas)
        botonMostrarReglas.place(x=683, y=600, anchor="center")
