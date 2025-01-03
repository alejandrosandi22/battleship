from componentes.comun.imagen import Imagen

class Fondo:
    def __init__(self, root, ruta, width=1366, height=768):
        self.root = root
        self.imagen_fondo = Imagen(self.root, ruta, width, height)
        self.canvas = self.imagen_fondo.obtenerCanvas()
        self.agregarFondo()

    def agregarFondo(self):
        """
        Agrega la imagen de fondo al canvas.
        """
        imagen_fondo = self.imagen_fondo.obtenerPhoto()
        self.canvas.create_image(0, 0, image=imagen_fondo, anchor="nw")

    def obtenerCanvas(self):
        """
        Retorna el objeto Canvas donde se ha colocado la imagen de fondo.
        """
        return self.canvas
