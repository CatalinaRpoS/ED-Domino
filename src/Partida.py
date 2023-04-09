from collections import deque


class Partida():

    def __init__(self, jugadores: list, fichas: list):

        self.jugadores = jugadores
        self.fichas = fichas
        self.colocadas = deque()
        self.turnos = deque()


    def asignar_turnos(self):
        pass


    def asignar_fichas(self):
        pass