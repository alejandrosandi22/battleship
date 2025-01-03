import tkinter as tk
from componentes.batalla.modalJuegoTerminado import ModalJuegoTerminado
from modelos.jugador import Jugador
from utilidades.constantes import TURNO_JUGADOR_1, TURNO_JUGADOR_2

class Juego():
    def __init__(self, contexto, nombreJugador1, nombreJugador2):
        """
        Inicializa una nueva instancia del juego.

        Args:
            contexto: El contexto del juego que proporciona el root y canvas.
            nombreJugador1: El nombre del primer jugador.
            nombreJugador2: El nombre del segundo jugador.
        """
        self.root = contexto.obtenerRoot()
        self.canvas = contexto.obtenerCanvas()

        self.turno = None

        self.jugador1 = Jugador(contexto, nombreJugador1, self.comprobarEstadoJugadores)
        self.jugador2 = Jugador(contexto, nombreJugador2, self.comprobarEstadoJugadores)

        self.empezarJuego = False
        self.juegoTerminado = False
        self.jugadorGanador = None

        self.configurarJuego()

    def configurarJuego(self):
        """
        Configura el juego inicializando el manejo de eventos del teclado, generando los tableros,
        botones y coordenadas de disparo, y mostrando los nombres de los jugadores.
        """
        self.root.bind("<KeyPress>", self.gestionarEntradaTecladoPorTurno)
        self.generarTableros()
        self.generarBotones()
        self.mostrarNombreJugador()

    def mostrarNombreJugador(self):
        """
        Muestra los nombres de los jugadores en el canvas en posiciones específicas.
        """
        self.jugador1.mostrarNombreJugador(341)
        self.jugador2.mostrarNombreJugador(1074)

    def comprobarEstadoJugadores(self):
        """
        Verifica si ambos jugadores están listos para comenzar el juego. 
        Si ambos están listos, inicia el juego llamando a manejarIniciarJuego.
        """
        if self.jugador1.listo and self.jugador2.listo:
            self.empezarJuego = True
            self.manejarIniciarJuego()
            self.jugador1.tablero.resaltarPosición(self.jugador2.tablero.tablero, (0, 0), (0, 0))

    def manejarIniciarJuego(self):
        """
        Configura la interfaz después de que el juego ha comenzado. Oculta los botones de configuración de barcos
        y muestra los botones de disparo. También inicializa la información del turno actual.
        """
        if self.empezarJuego:
            self.jugador1.iniciarConfiguracionJuego(posicionXInfo=190)
            self.jugador2.iniciarConfiguracionJuego(posicionXInfo=925)

            self.generarCoordenadasDisparo()
            
            self.mostrarTurnos()
            self.turno = TURNO_JUGADOR_1

    def generarCoordenadasDisparo(self):
        """
        Genera y muestra las coordenadas de disparo para ambos jugadores en sus respectivas posiciones.
        """
        self.jugador1.mostrarCoordenadasDeDisparo(posicionX=190)
        self.jugador2.mostrarCoordenadasDeDisparo(posicionX=925)

    def generarTableros(self):
        """
        Genera y muestra los tableros de los jugadores en posiciones específicas.
        También genera los barcos en el tablero de cada jugador.
        """
        self.jugador1.generarTablero(xInicial=220, yInicial=190)
        self.jugador2.generarTablero(xInicial=953, yInicial=190)

        self.jugador1.generarBarcos(xInicial=220, yInicial=465)
        self.jugador2.generarBarcos(xInicial=953, yInicial=465)

    def generarBotones(self):
        """
        Genera y muestra los botones para cada jugador en sus respectivas posiciones.
        """
        self.jugador1.generarBotones(xInicial=250)
        self.jugador2.generarBotones(xInicial=985)

    def manejarEmpezarJuego(self):
        """
        Cambia el estado de empezarJuego a True, indicando que el juego debería comenzar.
        """
        self.empezarJuego = True

    def mostrarTurnos(self):
        """
        Muestra el turno actual en el canvas.
        """
        self.canvas.create_text(683, 30, text="Turno", fill="#E8DF5C", font=("Arial", 20, "bold"), anchor="center")
        if hasattr(self, 'textoTurno'):
            self.canvas.itemconfig(self.textoTurno, text=f"{self.jugador1.nombre}")
        else:
            self.textoTurno = self.canvas.create_text(683, 68, text=f"{self.jugador1.nombre}", fill="#F5F6FF", font=("Arial", 14, "bold"), anchor="center")

    def actualizarTextoTurnos(self):
        """
        Actualiza el turno actual entre los dos jugadores y actualiza el texto en el canvas 
        para reflejar el nuevo turno.
        """
        if self.turno == TURNO_JUGADOR_1:
            if hasattr(self, 'textoTurno'):
                self.canvas.itemconfig(self.textoTurno, text=f"{self.jugador1.nombre}")
        else:
            if hasattr(self, 'textoTurno'):
                self.canvas.itemconfig(self.textoTurno, text=f"{self.jugador2.nombre}")

    def disparar(self):
        """
        Ejecuta el disparo del jugador actual si es posible.
        """
        jugadorActual = self.jugador1 if self.turno == TURNO_JUGADOR_1 else self.jugador2

        if jugadorActual.solicitarDisparo():
            if self.turno == TURNO_JUGADOR_1:
                self.turno, self.jugadorGanador = self.jugador1.ejecutarDisparo(
                    self.jugador2.tablero.barcosColocados, 
                    self.jugador2.tablero.tablero, 
                    self.turno, 
                    self.jugador2.nombre, 
                    self.jugador2.barcosDestruidos, 
                    self.jugador2.armamento
                )
            else:
                self.turno, self.jugadorGanador = self.jugador2.ejecutarDisparo(
                    self.jugador1.tablero.barcosColocados, 
                    self.jugador1.tablero.tablero, 
                    self.turno, 
                    self.jugador1.nombre, 
                    self.jugador1.barcosDestruidos, 
                    self.jugador1.armamento
                )

            if self.jugadorGanador:
                self.juegoTerminado = True

        self.actualizarTextoTurnos()

        if self.turno == TURNO_JUGADOR_1:
            self.jugador1.tablero.resaltarPosición(self.jugador2.tablero.tablero, (0, 0), (0, 0))
        elif self.turno == TURNO_JUGADOR_2:
            self.jugador2.tablero.resaltarPosición(self.jugador1.tablero.tablero, (0, 0), (0, 0))

    def gestionarEntradaTecladoPorTurno(self, event):
        """
        Maneja la entrada del teclado en función del turno actual del jugador.

        Args:
            event: El evento de teclado que se produce.
        """
        self.jugador1.manejarRotarBarco(event)
        self.jugador2.manejarRotarBarco(event)

        if not self.empezarJuego:
            return
        
        if self.turno == TURNO_JUGADOR_1:
            if event.keysym == 'space':
                self.disparar()
            else:
                self.jugador1.manejarMovimientoTeclado(event, self.jugador2.tablero.tablero)
        elif self.turno == TURNO_JUGADOR_2:
            if event.keysym == 'space':
                self.disparar()
            else:
                self.jugador2.manejarMovimientoTeclado(event, self.jugador1.tablero.tablero)
        
        self.comprobarJuegoTerminado()

    def comprobarJuegoTerminado(self):
        """
        Verifica si el juego ha terminado. Si es así, muestra un modal indicando al jugador ganador.
        """
        if self.juegoTerminado:
            self.rootModalGanador = tk.Toplevel()
            ModalJuegoTerminado(self.rootModalGanador, self.jugadorGanador, self.comandoFinalizar)
            self.rootModalGanador.mainloop()

    def comandoFinalizar(self):
        """
        Cierra la ventana principal y la ventana del modal de ganador.
        """
        self.root.destroy()
        self.rootModalGanador.destroy()
