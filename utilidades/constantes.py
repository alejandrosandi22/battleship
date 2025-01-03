from enum import Enum

TURNO_JUGADOR_1 = "jugador1"
TURNO_JUGADOR_2 = "jugador2"

TAMANO_TABLERO = 10
TAMANO_CELDA = 25


class EstadosDelBarco(Enum):
    ACTIVO = "activo"
    IMPACTADO = "impactado"
    DESTRUIDO = "destruido"

BARCOS = [
    { "id": 1, "casillas": [[1], [1]], "x": 0, "y": 0 },
    { "id": 2, "casillas": [[1], [1], [1]], "x": 0, "y": 0 },
    { "id": 3, "casillas": [[1], [1], [1], [1], [1]], "x": 0, "y": 0 },
    { "id": 4, "casillas": [[1, 0], [1, 1], [1, 0]], "x": 0, "y": 0 },
    { "id": 5, "casillas": [[0, 1], [1, 1], [1, 1], [1, 0]], "x": 0, "y": 0 }
]
