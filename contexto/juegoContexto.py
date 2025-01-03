class JuegoContexto():
    def __init__(self, root, canvas):
        """
        Inicializa una nueva instancia de JuegoContexto.

        Args:
            root: El widget root de Tkinter, utilizado como el punto de referencia para crear otros widgets.
            canvas: El widget canvas de Tkinter donde se dibujan los elementos gráficos.
        """
        self.root = root
        self.canvas = canvas

    def obtenerCanvas(self):
        """
        Devuelve el widget canvas asociado con esta instancia de JuegoContexto.

        Returns:
            El widget canvas.
        """
        return self.canvas
    
    def obtenerRoot(self):
        """
        Devuelve el widget root asociado con esta instancia de JuegoContexto.

        Returns:
            El widget root.
        """
        return self.root
