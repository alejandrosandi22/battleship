from utilidades.constantes import TAMANO_CELDA

class VerificadorDePosiciones():

    def __dentroDelTablero(self, nuevasPosicion, tablero):
        """
        Verifica si una posición está dentro del tablero.

        Args:
            nuevasPosicion: La posición a verificar (x, y).
            tablero: El tablero representado como una lista de filas, cada una con una lista de casillas que tienen una clave "posicion".

        Returns:
            bool: True si la posición está dentro del tablero, False en caso contrario.
        """
        for fila in tablero:
            for casilla in fila:
                if casilla["posicion"] == nuevasPosicion:
                    return True
        return False
    
    def __superponenDeBarcos(self, nuevasPosicion, barcosColocados, barcoActualId):
        """
        Verifica si una posición se superpone con barcos ya colocados.

        Args:
            nuevasPosicion: La posición a verificar (x, y).
            barcosColocados: Lista de barcos ya colocados, cada uno con una lista de posiciones.

        Returns:
            bool: True si la posición se superpone con algún barco, False en caso contrario.
        """

        for barco in barcosColocados:
            if barco["id"] == barcoActualId:
                continue 
            for posicion in barco["posiciones"]:
                if posicion == nuevasPosicion:
                    return True
        return False
    
    def __esAdyacente(self, nuevasPosicion, barcosColocados, barcoActualId):
        """
        Verifica si una posición es adyacente a algún barco ya colocado.

        Args:
            nuevasPosicion: La posición a verificar (x, y).
            barcosColocados: Lista de barcos ya colocados, cada uno con una lista de posiciones.

        Returns:
            bool: True si la posición es adyacente a algún barco, False en caso contrario.
        """
        direcciones = [
            (-TAMANO_CELDA, 0),              # Izquierda
            (TAMANO_CELDA, 0),               # Derecha
            (0, -TAMANO_CELDA),              # Arriba
            (0, TAMANO_CELDA),               # Abajo
            (-TAMANO_CELDA, -TAMANO_CELDA),  # Esquina superior izquierda
            (TAMANO_CELDA, -TAMANO_CELDA),   # Esquina superior derecha
            (-TAMANO_CELDA, TAMANO_CELDA),   # Esquina inferior izquierda
            (TAMANO_CELDA, TAMANO_CELDA)     # Esquina inferior derecha
        ]

        for barco in barcosColocados:
            if barco["id"] == barcoActualId:
                continue  
            for posicion in barco["posiciones"]:
                for direccion in direcciones:
                    direccionX, direccionY = direccion
                    adyacente = (posicion[0] + direccionX, posicion[1] + direccionY)
                    if adyacente == nuevasPosicion:
                        return True
        return False
    
    def verificar(self, nuevasPosicion, barcosColocados, tablero, barcoActualId):
        """
        Verifica si una nueva posición para un barco es válida.

        Args:
            nuevasPosicion: La nueva posición del barco (x, y).
            barcosColocados: Lista de barcos ya colocados, cada uno con una lista de posiciones.
            tablero: El tablero representado como una lista de filas, cada una con una lista de casillas que tienen una clave "posicion".

        Returns:
            bool: True si la posición es válida (dentro del tablero, no se superpone y no es adyacente), False en caso contrario.
        """
        # Verifica que la posición esté dentro del tablero
        if not self.__dentroDelTablero(nuevasPosicion, tablero):
            return False
        
        # Verifica que la posición no se superponga con ningún barco existente
        if self.__superponenDeBarcos(nuevasPosicion, barcosColocados, barcoActualId):
            return False
        
        # Verifica que la posición no esté adyacente a otros barcos
        if self.__esAdyacente(nuevasPosicion, barcosColocados, barcoActualId):
            return False

        return True
