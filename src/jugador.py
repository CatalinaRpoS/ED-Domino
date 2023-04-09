from ficha import Ficha
from partida import Partida


class Jugador:

    def __init__(self, nombre: str, fichas: list, partida: Partida):
        self.nombre = nombre
        self.fichas = fichas
        self.partida = partida

    def poner_ficha(self, ficha: Ficha):
        pass

    def __str__(self):
        return f"¡Hola! Soy {self.nombre} y tengo {len(self.fichas)} fichas"
