from modelos.barcos import Barcos
from utilidades.constantes import TAMANO_TABLERO, TAMANO_CELDA, BARCOS, TURNO_JUGADOR_1, TURNO_JUGADOR_2, EstadosDelBarco

class Tablero():
    def __init__(self, contexto, filas=TAMANO_TABLERO, columnas=TAMANO_TABLERO):
        """
        Inicializa una nueva instancia del tablero de juego.

        Args:
            contexto: El contexto del juego que proporciona el root y canvas.
            filas: Número de filas en el tablero (por defecto es TAMANO_TABLERO).
            columnas: Número de columnas en el tablero (por defecto es TAMANO_TABLERO).
        """
        self.root = contexto.obtenerRoot()
        self.canvas = contexto.obtenerCanvas()

        self.filas = filas
        self.columnas = columnas
        self.tablero = []
        self.matrizTablero = []
        self.barcosColocados = []
        self.barcosDestruidos = [
            {"id": 1, "posiciones": []},
            {"id": 2, "posiciones": []},
            {"id": 3, "posiciones": []},
            {"id": 4, "posiciones": []},
            {"id": 5, "posiciones": []},
        ]
        self.totalBarcosDestruidos = 0
        self.coordenadasSeleccionadas = None

    def crearTablero(self):
        """
        Crea una matriz del tamaño del tablero (10x10) donde cada celda contiene una tupla de coordenadas.
        """
        for fila in range(self.filas):
            nuevaFila = []
            for columna in range(self.columnas):
                nuevaFila.append((fila, columna))
            self.matrizTablero.append(nuevaFila)

    def mostrarTablero(self, xInicial, yInicial):
        """
        Muestra el tablero en la pantalla del juego y permite interactuar con él.

        Args:
            xInicial: La posición x inicial para colocar el tablero en el canvas.
            yInicial: La posición y inicial para colocar el tablero en el canvas.
        """
        self.crearTablero()
        for fila in range(self.filas):
            nuevaFila = []
            for columna in range(self.columnas):
                x = xInicial + columna * TAMANO_CELDA
                y = yInicial + fila * TAMANO_CELDA
                
                casilla = self.canvas.create_rectangle(
                    x, y, x + TAMANO_CELDA, y + TAMANO_CELDA, 
                    fill="#292D2B", outline="#f5f6ff", width=1
                )
                
                # Bind de evento de clic para colocar barcos manualmente
                self.canvas.tag_bind(casilla, "<Button-1>", lambda event, x=x, y=y: self.colocarBarcoManualmente(x, y))
                nuevaFila.append({ "casilla": casilla, "posicion": (x, y) })

            self.tablero.append(nuevaFila)
        
        self.agregarEtiquetas(xNumeros=(xInicial - 30), yNumeros=(yInicial + 10), xLetras=(xInicial + 12), yLetras=(yInicial-30))
        
    def resaltarPosición(self, tableroRival, posicionAnterior, coordenadasDeDisparo):
        """
        Resalta la posición seleccionada en el tablero rival y restaura la posición anterior.

        Args:
            tableroRival: El tablero rival donde se resalta la posición.
            posicionAnterior: La coordenada anterior para restaurar el color.
            coordenadasDeDisparo: La coordenada actual que se va a resaltar.
        """
        nuevaX, nuevaY = coordenadasDeDisparo
        casillaSeleccionada = tableroRival[nuevaX][nuevaY]["posicion"]

        anteriorX, anteriorY = posicionAnterior
        casillaAnterior = tableroRival[anteriorX][anteriorY]["posicion"]

        # Restaurar el color de la casilla anterior
        for fila in tableroRival:
            for columna in fila:
                if columna["posicion"] == casillaAnterior:
                    colorAnterior = self.canvas.itemcget(columna["casilla"], "fill")
                    if colorAnterior == "#8C9691":
                        self.canvas.itemconfig(columna["casilla"], fill="#292D2B")
                    elif colorAnterior == "#EF8F8F":
                        self.canvas.itemconfig(columna["casilla"], fill="#E85C5C")
                    elif colorAnterior == "#DBD79F":
                        self.canvas.itemconfig(columna["casilla"], fill="#CDC77A")
                        break

        # Resaltar la nueva posición
        for fila in tableroRival:
            for columna in fila:
                if columna["posicion"] == casillaSeleccionada:
                    colorAnterior = self.canvas.itemcget(columna["casilla"], "fill")
                    if colorAnterior == "#292D2B":
                        self.canvas.itemconfig(columna["casilla"], fill="#8C9691")
                    elif colorAnterior == "#E85C5C":
                        self.canvas.itemconfig(columna["casilla"], fill="#EF8F8F")
                    elif colorAnterior == "#CDC77A":
                        self.canvas.itemconfig(columna["casilla"], fill="#DBD79F")
                        break

    def ocultarBarcos(self):
        """
        Oculta los barcos en la pantalla del juego.
        """
        self.barcosJugador.ocultarBarcos()

    def agregarEtiquetas(self, xNumeros, yNumeros, xLetras, yLetras):
        """
        Muestra las coordenadas (números y letras) en el borde del tablero.

        Args:
            xNumeros: La posición x donde se mostrarán los números.
            yNumeros: La posición y donde se mostrarán los números.
            xLetras: La posición x donde se mostrarán las letras.
            yLetras: La posición y donde se mostrarán las letras.
        """
        for i in range(10):
            self.canvas.create_text(
                xNumeros, yNumeros + i * TAMANO_CELDA, text=str(i + 1),
                fill="#F5F6FF", font=("Arial", 12, "bold"), anchor="w"
            )

        for i, letra in enumerate("ABCDEFGHIJ"):
            self.canvas.create_text(
                xLetras + i * TAMANO_CELDA, yLetras, text=letra,
                fill="#F5F6FF", font=("Arial", 12, "bold"), anchor="n"
            )

    def rotarBarco(self):
        """
        Rota el barco en el tablero.
        """
        self.barcosJugador.rotarBarco(self.tablero)

    def colocarBarcoManualmente(self, x, y):
        """
        Maneja la selección de una casilla para colocar un barco manualmente.

        Args:
            x: La coordenada x donde se coloca el barco.
            y: La coordenada y donde se coloca el barco.
        """
        self.coordenadasSeleccionadas = (x, y)
        self.barcosColocados = self.barcosJugador.colocarManualmente(self.coordenadasSeleccionadas, self.tablero)

    def mostrarBarcos(self, xInicial, yInicial):
        """
        Muestra los barcos en el tablero.

        Args:
            xInicial: La posición x inicial para mostrar los barcos.
            yInicial: La posición y inicial para mostrar los barcos.
        """
        self.barcosJugador = Barcos(self.root, self.canvas, xInicial, yInicial, BARCOS)
        self.barcosJugador.mostrarBarcos()

    def colocarBarcosAleatoriamente(self):
        """
        Coloca los barcos en el tablero de manera aleatoria.
        """
        self.barcosColocados = self.barcosJugador.colocarAleatoriamente(self.tablero)

    def disparar(self, barcosColocados, coordenadasDeDisparo, tablero, turno, armamento):
        """
        Maneja el disparo en el tablero rival y actualiza el estado del juego.

        Args:
            barcosColocados: Los barcos colocados en el tablero rival.
            coordenadasDeDisparo: La coordenada donde se realiza el disparo.
            tablero: El tablero rival donde se realiza el disparo.
            turno: El turno actual del juego.
            armamento: La cantidad de armamento restante.

        Returns:
            tuple: El armamento restante, el turno actualizado, y el total de barcos destruidos.
        """
        DISPARO_ACERTADO = "#CDC77A"
        DISPARO_DESVIADO = "#E85C5C"

        resultado = DISPARO_DESVIADO

        x, y = coordenadasDeDisparo
        casillaSeleccionada = tablero[x][y]["posicion"]

        # Verificar si la posición ya fue utilizada
        for barcoDestruido in self.barcosDestruidos:
            if casillaSeleccionada in barcoDestruido["posiciones"]:
                return armamento, turno, self.totalBarcosDestruidos

        # Verificar si la posición impacta a algún barco
        for i, barco in enumerate(barcosColocados):
            if casillaSeleccionada in barco["posiciones"]:
                resultado = DISPARO_ACERTADO

                self.barcosDestruidos[i]["posiciones"].append(casillaSeleccionada)

                if len(self.barcosDestruidos[i]["posiciones"]) == len(barco["posiciones"]):
                    barco["estado"] = EstadosDelBarco.DESTRUIDO.value
                    self.totalBarcosDestruidos += 1
                else:
                    barco["estado"] = EstadosDelBarco.IMPACTADO.value
                    break

        # Actualizar el color de la casilla en el canvas
        for fila in tablero:
            for columna in fila:
                if columna["posicion"] == casillaSeleccionada:
                    self.canvas.itemconfig(columna["casilla"], fill=resultado)
                    break

        # Cambiar el turno si el disparo fue desviado
        if resultado == DISPARO_DESVIADO:
            if turno == TURNO_JUGADOR_1:
                turno = TURNO_JUGADOR_2
            else:
                turno = TURNO_JUGADOR_1

        armamento -= 1

        return armamento, turno, self.totalBarcosDestruidos
