from partida import Partida


class Jugador:

    def __init__(self, nombre: str, fichas: list, partida: Partida):
        self.nombre = nombre
        self.fichas = fichas
        self.partida = partida

    def poner_ficha(self):

        print("Tus fichas son: ")
        contador = 1

        for ficha in self.fichas:
            print(f"{contador}. {ficha}", sep="  ")
            contador += 1

        print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
        print("")

        ultima_ficha = None
        primera_ficha = None
        try:
            ultima_ficha = self.partida.colocadas.pop()
            self.partida.colocadas.append(ultima_ficha)
            primera_ficha = self.partida.colocadas.popleft()
            self.partida.colocadas.appendleft(primera_ficha)
        except:
            pass

        cola = None
        cabeza = None
        fichasDobles = None
        try:
            cola = ultima_ficha.cara[1]
            cabeza = primera_ficha.cara[0]
            fichasDobles = [x for x in self.fichas if x.id == 1 or x.id == 8 or x.id == 14 or
                            x.id == 19 or x.id == 23 or x.id == 26 or x.id == 28]
        except:
            pass

        jugadaDoble = list(filter(lambda ficha: ficha.cara[0] == cola or ficha.cara[0] == cabeza, fichasDobles))

        if len(jugadaDoble) == 2:
            while True:
                opcion = input("Tienes la oportunidad de hacer una jugada doble, ¿Quieres realizarla? (S / N): ")
                if opcion == "S" or opcion == "s":
                    for ficha in jugadaDoble:
                        if ficha.cara[0] == cola:
                            self.partida.colocadas.append(ficha)
                        else:
                            self.partida.colocadas.appendleft(ficha)
                        self.fichas.remove(ficha)
                    print("Acabas de realizar tu jugada")
                    return
                elif opcion == "N" or opcion == "n":
                    print("¡Entendido! Puedes mirar otras opciones")
                    break
                else:
                    print("¡La opción que ingresaste no es válida! Por favor intenta otra vez")

        while True:
            opcion = input("¿Deseas pasar el turno? (S / N): ")
            if opcion == "S" or opcion == "s":
                self.partida.contador += 1
                return
            elif opcion == "N" or opcion == "n":
                self.partida.contador = 0

                try:
                    posicion = int(input("Ingresa la ficha que quieres colocar: "))
                except:
                    print("Recuerda que debes ingresar un número entero, por favor intenta otra vez")
                    continue

                if len(self.fichas) < posicion < 1:
                    print("La ficha que seleccionaste no existe, por favor intenta otra vez")
                    continue

                ficha = self.fichas[posicion - 1]
                ficha_1 = ficha.cara[0]
                ficha_2 = ficha.cara[1]

                if ficha_1 == cabeza or ficha_1 == cola:
                    break
                elif ficha_2 == cabeza or ficha_2 == cola:
                    break
                else:
                    print("La jugada que deseas hacer no es válida, por favor intenta otra vez")
            else:
                print("¡La opción que ingresaste no es válida! Por favor intenta otra vez")

        while True:
            posicion = input("¿Deseas colocar la ficha al inicio o al final? (I / F): ")
            if posicion == "I" or opcion == "i":
                if ficha_1 == cabeza or ficha_2 == cabeza:
                    if ficha_2 != cabeza:
                        ficha.voltear_ficha()
                    self.partida.colocadas.appendleft(ficha)
                    self.fichas.remove(ficha)
                    print("Acabas de realizar tu jugada")
                    return
                else:
                    print("No puedes poner la ficha en este lugar")
                    continue

            elif posicion == "F" or opcion == "f":
                if ficha_1 == cola or ficha_2 == cola:
                    if ficha_1 != cola:
                        ficha.voltear_ficha()
                    self.partida.colocadas.append(ficha)
                    self.fichas.remove(ficha)
                    print("Acabas de realizar tu jugada")
                    return
                else:
                    print("No puedes poner la ficha en este lugar")
                    continue

            else:
                print("La opción que ingresaste no es válida, por favor intenta otra vez")

    def __str__(self):
        return f"¡Hola! Soy {self.nombre} y tengo {len(self.fichas)} fichas"
