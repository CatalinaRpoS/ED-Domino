from ficha import Ficha
from partida import Partida
from jugador import Jugador
from bot import Bot
from time import sleep
from pyfiglet import figlet_format

if __name__ == "__main__":

    # Bienvenida al juego para los jugadores
    bienvenida = figlet_format("S u p e r\nD o m i n o", font="colossal")
    print(bienvenida)
    sleep(2)
    
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
    sleep(1)

    ''' print(f"\nEstas son las fichas de {bot1.nombre}")
    for ficha in bot1.fichas:
        print(ficha)
    sleep(1)

    print(f"\nEstas son las fichas de {bot2.nombre}")
    for ficha in bot2.fichas:
        print(ficha)
    sleep(1)

    print(f"\nEstas son las fichas de {bot3.nombre}")
    for ficha in bot3.fichas:
        print(ficha)
    sleep(1) '''

    # Se asignan los turnos de los jugadores, teniendo en cuenta que empieza el que tenga
    # el doble seis, el resto se eligen aleatoriamente
    print()
    print(partida.asignar_turnos())
    print("El orden de los turnos es:")
    for i in range(len(partida.turnos)):
        print(f"{i + 1}. {partida.turnos[i].nombre}")
        sleep(1)

    print("")
    print("¡Empecemos a jugar!")
    print("")

    jugador_inicial = partida.turnos.popleft()
    print(f"Turno de {jugador_inicial.nombre}\n")
    print(f"{jugador_inicial.nombre} hizo su jugada\n")

    partida.turnos.append(jugador_inicial)
    partida.colocadas.append(jugador_inicial.fichas.pop())
    sleep(3)

    while True:

        ganador = partida.verificar_ganador()

        if ganador != None:
            print("\nEl juego ha terminado")
            print(f"¡{ganador.nombre} ha ganado!\n")
            break

        partida.imprimir_colocadas()
        jugador_en_turno = partida.cambio_de_turno()

        print(f"Turno de {jugador_en_turno.nombre}\n")
        jugador_en_turno.poner_ficha()
        sleep(3)
