import customtkinter as ctk

class BotonRegresar():
    def __init__(self, root, comandoRegresar):
        self.root = root
        self.comandoRegresar = comandoRegresar

    def agregarBoton(self):
        boton_regresar = ctk.CTkButton(self.root, text="Volver Inicio", width=350, height=65, font=("Arial", 24), command=self.comandoRegresar)
        boton_regresar.place(x=683, y=560, anchor="center")
