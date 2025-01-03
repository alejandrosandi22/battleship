import tkinter as tk
import random

from utilidades.constantes import TAMANO_CELDA, EstadosDelBarco
from utilidades.verificadorDePosiciones import VerificadorDePosiciones

class Barcos():
    def __init__(self, root, canvas, xInicial, yInicial, barcos):
        """
        Inicializa una nueva instancia de la clase Barcos.

        Args:
            root: El widget root de Tkinter, que es el punto de referencia para crear widgets.
            canvas: El widget canvas de Tkinter donde se dibujarán los barcos.
            xInicial: La coordenada x inicial para mostrar los barcos en el canvas.
            yInicial: La coordenada y inicial para mostrar los barcos en el canvas.
            barcos: Una lista de diccionarios que contiene la información sobre los barcos.
        """
        self.barcos = barcos
        self.root = root
        self.xInicial = xInicial
        self.yInicial = yInicial
        self.canvas = canvas
        self.barcoSeleccionadoId = None
        self.barcosColocados = []
        self.verificadorDePosiciones = VerificadorDePosiciones()

    def mostrarBarcos(self):
        """
        Muestra los barcos en el tablero creando botones en las posiciones correspondientes.
        """
        for barco in self.barcos:
            y1 = self.yInicial
            botonesBarco = []
            posiciones = []

            for fila in barco["casillas"]:
                x1 = self.xInicial
                botonesFila = []

                for celda in fila:
                    if celda == 1:
                        background = "#E8DF5C"
                        boton = tk.Button(self.root, width=2, height=1, bg=background, borderwidth=1, relief="solid", highlightbackground="#f5f6ff", command=lambda id=barco["id"]: self.seleccionarBarco(id))
                        boton.place(x=x1, y=y1, width=TAMANO_CELDA, height=TAMANO_CELDA)

                        botonesFila.append(boton)
                        posiciones.append((x1, y1))
                    else:
                        botonesFila.append(None)

                    x1 += TAMANO_CELDA
                botonesBarco.append(botonesFila)
                y1 += TAMANO_CELDA

            self.barcosColocados.append({
                "id": barco["id"],
                "casillas": botonesBarco,
                "posiciones": posiciones,
                "estado": EstadosDelBarco.ACTIVO.value
            })

            if len(fila) == 2:
                self.xInicial += (TAMANO_CELDA * 3)
            else:    
                self.xInicial += (TAMANO_CELDA * 2) * len(fila)

    def ocultarBarcos(self):
        """
        Oculta todos los barcos generados del tablero.
        """
        for barco in self.barcosColocados:
            for fila in barco["casillas"]:
                for boton in fila:
                    if boton is not None:
                        boton.place_forget()

    def seleccionarBarco(self, id):
        """
        Selecciona o deselecciona un barco según su id.

        Args:
            id: El id del barco que se va a seleccionar o deseleccionar.
        """
        if id == self.barcoSeleccionadoId:
            self.barcoSeleccionadoId = None
        else:
            self.barcoSeleccionadoId = id

        for barco in self.barcosColocados:
            if barco["id"] == self.barcoSeleccionadoId:
                for fila in barco["casillas"]:
                    for boton in fila:
                        if isinstance(boton, tk.Button):
                            boton.config(bg="#FBFAE4")
            else:
                for fila in barco["casillas"]:
                    for boton in fila:
                        if isinstance(boton, tk.Button):
                            boton.config(bg="#E8DF5C")

    def rotarBarco(self, tablero):
        """
        Rota el barco seleccionado en el tablero.

        Args:
            tablero: La estructura del tablero para verificar la validez de la nueva posición.

        Returns:
            list: La lista actualizada de barcos colocados.
        """
        barcosColocadosTemporales = self.barcosColocados
        posicionNoValida = False

        for barco in barcosColocadosTemporales:
            if barco["id"] == self.barcoSeleccionadoId:
                casillasOriginales = barco["casillas"]

                # Crear una lista de filas combinadas para la rotación
                longitudMaxima = max(len(fila) for fila in casillasOriginales)
                filasCombinadas = [[] for _ in range(longitudMaxima)]

                for fila in casillasOriginales:
                    for i in range(longitudMaxima):
                        if i < len(fila):
                            filasCombinadas[i].append(fila[i])
                        else:
                            filasCombinadas[i].append(None)

                casillasTransformadas = filasCombinadas
                barco["casillas"] = casillasTransformadas
                if not posicionNoValida:
                    posicionNoValida = self.actualizarVisualizacionBarco(barco, tablero)
                break

            if not posicionNoValida:
                self.barcosColocados = barcosColocadosTemporales

        return self.barcosColocados

    def actualizarVisualizacionBarco(self, barco, tablero):
        """
        Actualiza la visualización del barco en el canvas después de rotarlo.

        Args:
            barco: El barco que se está actualizando.
            tablero: La estructura del tablero para verificar la validez de la nueva posición.

        Returns:
            bool: Indica si la nueva posición es válida o no.
        """
        primeraPosicion = barco["posiciones"][0] if barco["posiciones"] else (self.xInicial, self.yInicial)
        posicionNoValida = False

        yInicio = primeraPosicion[1]
        for fila in barco["casillas"]:
            xInicio = primeraPosicion[0]
            for casilla in fila:
                if posicionNoValida:
                    break
                if casilla is not None:
                    if not self.verificadorDePosiciones.verificar((xInicio, yInicio), self.barcosColocados, tablero, self.barcoSeleccionadoId):
                        posicionNoValida = True
                        break
                xInicio += TAMANO_CELDA
            yInicio += TAMANO_CELDA

        if not posicionNoValida:
            for fila in barco["casillas"]:
                for boton in fila:
                    if boton is not None:
                        boton.place_forget()

            yInicio = primeraPosicion[1]
            for fila in barco["casillas"]:
                xInicio = primeraPosicion[0]
                for casilla in fila:
                    if casilla is not None:
                        casilla.place(x=xInicio, y=yInicio, width=TAMANO_CELDA, height=TAMANO_CELDA)
                    xInicio += TAMANO_CELDA
                yInicio += TAMANO_CELDA
        
        return posicionNoValida

    def colocarManualmente(self, coordenadaSeleccionada, tablero):
        """
        Coloca los barcos en las posiciones seleccionadas dentro del tablero de forma manual.

        Args:
            coordenadaSeleccionada: La coordenada donde se va a colocar el barco.
            tablero: La estructura del tablero para verificar la validez de la nueva posición.

        Returns:
            list: La lista actualizada de barcos colocados.
        """
        barcosColocadosTemporales = self.barcosColocados
        nuevasPosiciones = []

        posicionNoValida = False

        for barco in barcosColocadosTemporales:
            if barco["id"] == self.barcoSeleccionadoId:
                xInicio, yInicio = coordenadaSeleccionada
                nuevasPosiciones = []
                for i, fila in enumerate(barco["casillas"]):
                    if posicionNoValida:
                        break

                    for j, casilla in enumerate(fila):
                        if casilla != None:
                            x = xInicio + j * TAMANO_CELDA
                            y = yInicio + i * TAMANO_CELDA
                            nuevasPosiciones.append((x, y))

                            if not self.verificadorDePosiciones.verificar((x, y), self.barcosColocados, tablero, self.barcoSeleccionadoId):
                                nuevasPosiciones = []
                                posicionNoValida = True
                                break

                if not posicionNoValida:
                    barco["posiciones"] = nuevasPosiciones
                break
        
        if not posicionNoValida:
            for barco in barcosColocadosTemporales:
                if barco["id"] == self.barcoSeleccionadoId:
                    for fila in barco["casillas"]:
                        for casillas in fila:
                            if casillas != None:
                                casillas.place_forget()

                    nuevaPosicion = 0
                    for fila in barco["casillas"]:
                        for casilla in fila:
                            if casilla != None:
                                if nuevaPosicion < len(nuevasPosiciones):
                                    x, y = nuevasPosiciones[nuevaPosicion]
                                    casilla.config(bg="#E8DF5C")
                                    casilla.place(x=x, y=y, width=TAMANO_CELDA, height=TAMANO_CELDA)
                                nuevaPosicion += 1

            self.barcoSeleccionadoId = None
            self.barcosColocados = barcosColocadosTemporales

        return self.barcosColocados

    def colocarAleatoriamente(self, tablero):
        """
        Coloca los barcos en posiciones aleatorias dentro del tablero.

        Args:
            tablero: La estructura del tablero para verificar la validez de la nueva posición.

        Returns:
            list: La lista actualizada de barcos colocados.
        """
        barcosColocadosTemporales = self.barcosColocados

        for barco in barcosColocadosTemporales:
            contador = 0
            posicionNoValida = False

            while contador < 100:
                posicionNoValida = False
                nuevasPosiciones = []

                filaEscogida = random.choice(tablero)
                casillaEscogida = random.choice(filaEscogida)

                xInicio, yInicio = casillaEscogida["posicion"]

                for i, fila in enumerate(barco["casillas"]):
                    if posicionNoValida:
                        break

                    for j, boton in enumerate(fila):
                        if boton != None:
                            x = xInicio + j * TAMANO_CELDA
                            y = yInicio + i * TAMANO_CELDA
                            nuevasPosiciones.append((x, y))

                            if not self.verificadorDePosiciones.verificar((x, y), self.barcosColocados, tablero, 0):
                                nuevasPosiciones = []
                                posicionNoValida = True
                                contador += 1
                                break
                
                if not posicionNoValida:
                    barco["posiciones"] = nuevasPosiciones
                    break

            if not posicionNoValida:
                for fila in barco["casillas"]:
                    for boton in fila:
                        if boton != None:
                            boton.place_forget()

                nuevaPosicion = 0
                for fila in barco["casillas"]:
                    for boton in fila:
                        if boton != None:
                            if nuevaPosicion < len(nuevasPosiciones):
                                x, y = nuevasPosiciones[nuevaPosicion]
                                boton.config(bg="#E8DF5C")
                                boton.place(x=x, y=y, width=TAMANO_CELDA, height=TAMANO_CELDA)
                            nuevaPosicion += 1

                self.barcosColocados = barcosColocadosTemporales

        return self.barcosColocados
