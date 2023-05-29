from collections import deque
import random


class Partida:

    def __init__(self, jugadores: list, fichas: list):
        self.jugadores = jugadores
        self.fichas = fichas
        self.colocadas = deque()
        self.turnos = deque()
        self.contador = 0

    def asignar_turnos(self):
        for i in range(len(self.jugadores)):
            minimo = 0
            maximo = 6

            # El jugador que tiene el doble seis comienza con el primer
            # turno, los demás se asignan aleatoriamente
            while minimo <= maximo:
                medio = (minimo + maximo) // 2

                if self.jugadores[i].fichas[medio].id == 28:
                    self.turnos.append(self.jugadores[i])
                    self.turnos.append(self.jugadores[i-1])
                    self.turnos.append(self.jugadores[i-2])
                    self.turnos.append(self.jugadores[i-3])
                    return "¡Los turnos han sido asignados!"

                elif self.jugadores[i].fichas[medio].id < 28:
                    minimo = medio + 1
                else:
                    maximo = medio - 1
        return "Los turnos no pudieron asignarse"

    def asignar_fichas(self):
        indices = [0, 1, 2, 3]

        for i in range(0, len(self.fichas), 4):
            random.shuffle(indices)
            self.jugadores[indices[0]].fichas.append(self.fichas[i])
            self.jugadores[indices[1]].fichas.append(self.fichas[i+1])
            self.jugadores[indices[2]].fichas.append(self.fichas[i+2])
            self.jugadores[indices[3]].fichas.append(self.fichas[i+3])

        return "¡Las fichas se repartieron!"

    def cambio_de_turno(self):
        jugador_en_turno = self.turnos.popleft()
        self.turnos.append(jugador_en_turno)
        return jugador_en_turno

    def verificar_ganador(self):
        if self.contador == 4:
            suma_minima = []
            for jugador in self.jugadores:
                lista_ids = [ficha.id for ficha in jugador.fichas]
                suma_minima.append(sum(lista_ids))
            return self.jugadores[suma_minima.index(min(suma_minima))]

        else:
            for jugador in self.jugadores:
                if len(jugador.fichas) == 0:
                    return jugador
        return None

    def imprimir_colocadas(self):

        print("\nFichas en juego:\n")
        colocadas = ""
        for i in range(len(self.colocadas)):
            if i == 7 or i == 14 or i == 21:
                colocadas = colocadas + " ... "
            colocadas = colocadas + self.colocadas[i].__str__() + " "
            if i == 6 or i == 13 or i == 20:
                colocadas = colocadas + " ... \n\n"
        print(colocadas)

        print("")
        print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
        print("")

    def __str__(self):
        return f"Soy una partida con {len(self.jugadores)} jugadores y {len(self.fichas)} fichas"
