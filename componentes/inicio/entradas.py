import customtkinter as ctk

class EntradasVistaInicio():
    def __init__(self, root, canvas):
        self.root = root
        self.canvas = canvas
        self.entradaNombreJugador1 = None
        self.entradaNombreJugador2 = None

    def mostrarEntradas(self):
        self.canvas.create_text(545, 260, text="Jugador 1:", fill="#f5f6ff", anchor="e", font=("Arial", 16))
        self.entradaNombreJugador1 = ctk.CTkEntry(self.root, placeholder_text="Ingrese el nombre del jugador 1", width=480, height=54, font=("Arial", 24), border_width=0)
        self.entradaNombreJugador1.place(x=443, y=280)

        self.canvas.create_text(545, 370, text="Jugador 2:", fill="#f5f6ff", anchor="e", font=("Arial", 16))
        self.entradaNombreJugador2 = ctk.CTkEntry(self.root, placeholder_text="Ingrese el nombre del jugador 2", width=480, height=54, font=("Arial", 24), border_width=0)
        self.entradaNombreJugador2.place(x=443, y=390)
