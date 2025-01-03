from PIL import Image, ImageTk
import tkinter as tk

class Imagen:
    def __init__(self, root, ruta, width=1366, height=768):
        """
        Inicializa el componente de imagen.
        
        Args:
            root: La ventana raíz de tkinter.
            ruta: Ruta a la imagen.
            width: Ancho del canvas y de la imagen.
            height: Alto del canvas y de la imagen.
        """
        self.root = root
        self.ruta = ruta
        self.width = width
        self.height = height

        self.cargarImagen()
        self.mostrarImagen()

    def cargarImagen(self):
        """
        Carga la imagen desde la ruta, la redimensiona y la convierte en un objeto PhotoImage.
        """
        try:
            self.imagen = Image.open(self.ruta)
            self.imagen = self.imagen.resize((self.width, self.height), Image.LANCZOS)
            self.photo = ImageTk.PhotoImage(self.imagen)
        except Exception as e:
            print(f"Error al cargar la imagen: {e}")

    def mostrarImagen(self):
        """
        Crea un Canvas y coloca la imagen en el Canvas.
        """
        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height, bg="#292D2B", highlightthickness=0)
        self.canvas.pack()

        self.canvas.create_image(0, 0, image=self.photo, anchor="nw")

        self.canvas.image = self.photo

    def obtenerCanvas(self):
        """
        Retorna el objeto Canvas donde se ha colocado la imagen.
        """
        return self.canvas

    def obtenerPhoto(self):
        """
        Retorna el objeto PhotoImage de la imagen cargada.
        """
        return self.photo
