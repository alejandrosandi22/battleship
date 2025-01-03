import customtkinter as ctk
from modelos.tablero import Tablero

class Jugador():
    def __init__(self, contexto, nombre, comprobarEstadoJugadores):
        """
        Inicializa una nueva instancia del jugador.

        Args:
            contexto: El contexto del juego que proporciona el root y canvas.
            nombre: El nombre del jugador.
            comprobarEstadoJugadores: Función que verifica el estado de ambos jugadores.
        """
        self.root = contexto.obtenerRoot()
        self.canvas = contexto.obtenerCanvas()

        self.tablero = Tablero(contexto)

        self.comprobarEstadoJugadores = comprobarEstadoJugadores

        self.nombre = nombre
        self.listo = False
        self.armamento = 20
        self.barcosDestruidos = 0
        self.coordenadasDeDisparo = (0, 0)

    def mostrarNombreJugador(self, x):
        """
        Muestra el nombre del jugador en el canvas en la posición x especificada.

        Args:
            x: La posición x en el canvas donde se mostrará el nombre.
        """
        self.canvas.create_text(x, 30, text=f"{self.nombre}", fill="#F5F6FF", width=275, font=("Arial", 14, "bold"), anchor="center")

    def mostrarInformacion(self, posicionX):
        """
        Muestra la información del jugador (barcos destruidos y armamento) en el canvas.

        Args:
            posicionX: La posición x en el canvas donde se mostrará la información.
        """
        self.textoBarcosDestruidos = self.canvas.create_text(posicionX, 80, text=f"Barcos destruidos: {self.barcosDestruidos}", fill="#F5F6FF", font=("Arial", 11, "bold"), width=275, anchor="w")
        self.textoArmamaneto = self.canvas.create_text(posicionX, 110, text=f"Armamaneto: {self.armamento}", fill="#F5F6FF", font=("Arial", 11, "bold"), width=275, anchor="w")

    def actualizarTextoArmamento(self):
        """
        Actualiza el texto en el canvas para mostrar el armamento actual del jugador.
        """
        self.canvas.itemconfig(self.textoArmamaneto, text=f"Armamaneto: {self.armamento}")

    def generarBotones(self, xInicial, yInicial=640):
        """
        Genera y posiciona los botones para ordenar barcos, confirmar que el jugador está listo y disparar.

        Args:
            xInicial: La posición x inicial para colocar los botones.
            yInicial: La posición y inicial para colocar los botones (por defecto es 640).
        """
        self.botonOrdenarBarcos = ctk.CTkButton(self.root, text="Aleatoriamente", width=125, bg_color="#292D2B", command=self.tablero.colocarBarcosAleatoriamente)
        self.botonOrdenarBarcos.place(x=xInicial, y=yInicial, anchor="center")

        self.botonListo = ctk.CTkButton(self.root, text="Listo", width=125, bg_color="#292D2B", command=self.manejarJugadorListo)
        self.botonListo.place(x=(xInicial + 150), y=yInicial, anchor="center")

    def manejarJugadorListo(self):
        """
        Maneja la acción cuando el jugador confirma que está listo. 
        Desactiva los botones de ordenar barcos y listo si el jugador ha colocado todos sus barcos.
        """
        if len(self.tablero.barcosColocados) == 5:
            self.listo = True
            self.tablero.ocultarBarcos()
            self.botonListo.configure(state="disable", fg_color="#B5B28F")
            self.botonOrdenarBarcos.configure(state="disable", fg_color="#B5B28F")

            self.comprobarEstadoJugadores()

    def iniciarConfiguracionJuego(self, posicionXInfo):
        """
        Configura el juego al iniciar. Oculta los botones de configuración y muestra la información del jugador.

        Args:
            posicionXInfo: La posición x en el canvas donde se mostrará la información del jugador.
        """
        self.botonListo.place_forget()
        self.botonOrdenarBarcos.place_forget()

        self.mostrarInformacion(posicionXInfo)

    def moverIzquierda(self):
        """
        Mueve la coordenada de disparo una posición a la izquierda, sin permitir coordenadas negativas.
        """
        x, y = self.coordenadasDeDisparo
        if x > 0:
            self.coordenadasDeDisparo = (x - 1, y)

    def moverDerecha(self):
        """
        Mueve la coordenada de disparo una posición a la derecha.
        """
        x, y = self.coordenadasDeDisparo
        if x < 9:
            self.coordenadasDeDisparo = (x + 1, y)

    def moverArriba(self):
        """
        Mueve la coordenada de disparo una posición hacia arriba, sin permitir coordenadas negativas.
        """
        x, y = self.coordenadasDeDisparo
        if y > 0:
            self.coordenadasDeDisparo = (x, y - 1)

    def moverAbajo(self):
        """
        Mueve la coordenada de disparo una posición hacia abajo.
        """
        x, y = self.coordenadasDeDisparo
        if y < 9:
            self.coordenadasDeDisparo = (x, y + 1)

    def generarTablero(self, xInicial, yInicial):
        """
        Genera y muestra el tablero del jugador en el canvas.

        Args:
            xInicial: La posición x inicial del tablero.
            yInicial: La posición y inicial del tablero.
        """
        self.tablero.mostrarTablero(xInicial, yInicial)

    def manejarMovimientoTeclado(self, event, tableroRival):
        """
        Maneja el movimiento del jugador en el tablero según la tecla presionada y resalta la posición en el tablero rival.

        Args:
            event: El evento de teclado que se produce.
            tableroRival: El tablero del rival para resaltar la posición.
        """
        posicionAnterior = self.coordenadasDeDisparo
        
        if event.keysym == 'a':
            self.moverArriba()
        elif event.keysym == 'd':
            self.moverAbajo()
        elif event.keysym == 'w':
            self.moverIzquierda()
        elif event.keysym == 's':
            self.moverDerecha()

        self.tablero.resaltarPosición(tableroRival, posicionAnterior, self.coordenadasDeDisparo)
        self.actualizarCoordenadas()

    def manejarRotarBarco(self, event):
        """
        Maneja la rotación del barco si se presiona la tecla 'r'.

        Args:
            event: El evento de teclado que se produce.
        """
        if event.keysym == 'r':
            self.tablero.rotarBarco()
        
    def mostrarCoordenadasDeDisparo(self, posicionX, posicionY=640):
        """
        Muestra las coordenadas actuales de disparo para el jugador.

        Args:
            posicionX: La posición x en el canvas donde se mostrará el texto de disparo.
            posicionY: La posición y en el canvas donde se mostrará el texto de disparo (por defecto es 640).
        """
        self.botonDisparar = self.canvas.create_text((posicionX + 150), posicionY, text="<Espacio para disparar>", fill="#F5F6FF", font=("Arial", 12, "bold"), anchor="w")
        
        if hasattr(self, 'textoCoordenadasDisparo'):
            self.canvas.itemconfig(self.textoCoordenadasDisparo, text=f"Disparar en: {self.getLetraCoordenada()}")
        else:
            letra = self.getLetraCoordenada()
            self.textoCoordenadasDisparo = self.canvas.create_text(posicionX, posicionY, text=f"Disparar en: {letra}", fill="#F5F6FF", font=("Arial", 12, "bold"), anchor="w")

    def actualizarCoordenadas(self):
        """
        Actualiza el texto en el canvas para reflejar las coordenadas actuales de disparo.
        """
        if hasattr(self, 'textoCoordenadasDisparo'):
            self.canvas.itemconfig(self.textoCoordenadasDisparo, text=f"Disparar en: {self.getLetraCoordenada()}")

    def getLetraCoordenada(self):
        """
        Convierte la coordenada de disparo en la letra correspondiente y el número.

        Returns:
            str: La coordenada en formato de letra (A-J) y número (1-10).
        """
        letra = "ABCDEFGHIJ"[self.coordenadasDeDisparo[1]]
        numero = self.coordenadasDeDisparo[0] + 1
        return f"{letra}{numero}"
    
    def ejecutarDisparo(self, barcosColocados, tablero, turno, nombreRival, barcosDestruidosRivales, armamentoRival):
        """
        Ejecuta el disparo en el tablero rival y actualiza el estado del juego.

        Args:
            barcosColocados: Los barcos colocados en el tablero rival.
            tablero: El tablero rival donde se realiza el disparo.
            turno: El turno actual.
            nombreRival: El nombre del jugador rival.
            barcosDestruidosRivales: Número de barcos destruidos por el rival.
            armamentoRival: Armamento restante del rival.

        Returns:
            tuple: El turno actualizado y el nombre del jugador ganador (si hay uno).
        """
        jugadorGanador = None
        
        self.armamento, turnoActualizado, barcosDestruidos = self.tablero.disparar(barcosColocados, self.coordenadasDeDisparo, tablero, turno, self.armamento)
        self.barcosDestruidos = barcosDestruidos

        self.canvas.itemconfig(self.textoBarcosDestruidos, text=f"Barcos destruidos: {self.barcosDestruidos}")

        self.coordenadasDeDisparo = (0, 0)
        self.actualizarCoordenadas()
        self.actualizarTextoArmamento()

        jugadorGanador = self.determinarJugadorGanador(turno, turnoActualizado, nombreRival, barcosDestruidosRivales, armamentoRival)
            
        return turnoActualizado, jugadorGanador

    def determinarJugadorGanador(self, turno, turnoActualizado, nombreRival, barcosDestruidosRivales, armamentoRival):
        """
        Determina el jugador ganador basado en el estado del juego después del disparo.

        Args:
            turno: El turno actual antes del disparo.
            turnoActualizado: El turno después del disparo.
            nombreRival: El nombre del jugador rival.
            barcosDestruidosRivales: Número de barcos destruidos por el rival.
            armamentoRival: Armamento restante del rival.

        Returns:
            str: El nombre del jugador ganador, o None si no hay ganador aún.
        """
        if self.armamento == 0 and turnoActualizado == turno:
            if self.barcosDestruidos > barcosDestruidosRivales:
                return self.nombre
            elif self.barcosDestruidos < barcosDestruidosRivales:
                return nombreRival
            else:
                return self.nombre if self.armamento > armamentoRival else nombreRival
        elif armamentoRival == 0 and turnoActualizado != turno:
            if self.barcosDestruidos > barcosDestruidosRivales:
                return self.nombre
            elif self.barcosDestruidos < barcosDestruidosRivales:
                return nombreRival
            else:
                return self.nombre if self.armamento > armamentoRival else nombreRival
        
        return None

    def generarBarcos(self, xInicial, yInicial):
        """
        Genera y muestra los barcos del jugador en el canvas.

        Args:
            xInicial: La posición x inicial para mostrar los barcos.
            yInicial: La posición y inicial para mostrar los barcos.
        """
        self.tablero.mostrarBarcos(xInicial, yInicial)

    def solicitarDisparo(self):
        """
        Solicita al juego que ejecute un disparo si el jugador tiene armamento restante.

        Returns:
            bool: True si el disparo puede ser realizado (armamento > 0), de lo contrario False.
        """
        if self.armamento > 0:
            return True
        return False
