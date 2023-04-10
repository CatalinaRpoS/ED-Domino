from ficha import Ficha
from partida import Partida
from jugador import Jugador
from bot import Bot
from time import sleep

if __name__ == "__main__":

    # Creación de la partida
    partida = Partida(list(), list())

    # Creación de la cantidad total de fichas necesarias en la partida
    contador = 1
    for i in range(7):
        for j in range(i, 7):
            partida.fichas.append(Ficha(str(i), str(j), contador))
            contador += 1

    # Creación de jugadores
    print("¿Cuál es tu nombre?")
    jugador = Jugador(input(), list(), partida)
    bot1 = Bot("Miller", list(), partida)
    bot2 = Bot("Carolina", list(), partida)
    bot3 = Bot("Tomás", list(), partida)

    # Se añaden los jugadores a la partida
    partida.jugadores.append(jugador)
    partida.jugadores.append(bot1)
    partida.jugadores.append(bot2)
    partida.jugadores.append(bot3)

    # Se asignan las fichas a los jugadores
    print(partida.asignar_fichas())

    print(f"\nEstas son tus fichas, {jugador.nombre}")
    for ficha in jugador.fichas:
        print(ficha)
    sleep(2)

    print(f"\nEstas son las fichas de {bot1.nombre}")
    for ficha in bot1.fichas:
        print(ficha)
    sleep(2)

    print(f"\nEstas son las fichas de {bot2.nombre}")
    for ficha in bot2.fichas:
        print(ficha)
    sleep(2)

    print(f"\nEstas son las fichas de {bot3.nombre}")
    for ficha in bot3.fichas:
        print(ficha)
    sleep(2)

    # Se asignan los turnos de los jugadores, teniendo en cuenta que empieza el que tenga
    # el doble seis, el resto se eligen aleatoriamente
    print()
    print(partida.asignar_turnos())
    print("El orden de los turnos es:")
    for i in range(len(partida.turnos)):
        print(f"{i + 1}. {partida.turnos[i].nombre}")
        sleep(1.5)

    jugador_inicial = partida.turnos.popleft()
    doble_seis = jugador_inicial.fichas.pop()
    partida.turnos.append(jugador_inicial)
    partida.colocadas.append(doble_seis)
    
    while partida.verificar_ganador() == None:
        jugador_en_turno = partida.cambio_de_turno()
        jugador_en_turno.poner_ficha = 