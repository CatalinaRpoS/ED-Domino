from collections import deque
import random


class Partida:

    def __init__(self, jugadores: list, fichas: list):
        self.jugadores = jugadores
        self.fichas = fichas
        self.colocadas = deque()
        self.turnos = deque()

    def asignar_turnos(self):
        jugadores = self.jugadores
        for jugador in self.jugadores:
            minimo = 0
            maximo = 6

            while minimo <= maximo:
                medio = (minimo + maximo) // 2

                if jugador.fichas[medio].id == 28:
                    self.turnos.append(jugador)
                    jugadores.remove(jugador)
                    self.turnos.append(random.choice(jugadores))
                    jugadores.remove(self.turnos[-1])
                    self.turnos.append(random.choice(jugadores))
                    jugadores.remove(self.turnos[-1])
                    self.turnos.append(jugadores[0])
                    return "¡Los turnos han sido asignados!"

                elif jugador.fichas[medio].id < 28:
                    minimo = medio + 1
                else:
                    maximo = medio - 1
        return "Los turnos no pudieron asignarse"

    def asignar_fichas(self):
        fichas = self.fichas
        for jugador in self.jugadores:
            jugador.fichas = random.sample(fichas, 7)
            jugador.fichas.sort(key=lambda x: x.id)
            for ficha in jugador.fichas:
                fichas.remove(ficha)

        return "¡Las fichas se repartieron!"

    def cambio_de_turno(self):
        jugador_en_turno = self.turnos.popleft()
        self.turnos.append(jugador_en_turno)
        return jugador_en_turno

    def verificar_ganador(self):
        for jugador in self.jugadores:
            if len(jugador.fichas) == 0:
                return jugador
        return None

    def imprimir_colocadas(self):

        print("Fichas en juego:")

        for ficha in self.colocadas:
            print(ficha, end="  ")

        print("")
        print("#--------------------------------------------------")
        print("")

    def __str__(self):
        return f"Soy una partida con {len(self.jugadores)} jugadores y {len(self.fichas)} fichas"
