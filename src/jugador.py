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

        print("#--------------------------------------------------")
        print("")

        try:
            ultima_ficha = self.partida.colocadas.pop()
            self.partida.colocadas.append(ultima_ficha)

            primera_ficha = self.partida.colocadas.popleft()
            self.partida.colocadas.appendleft(primera_ficha)

        except:
            pass

        while True:

            if input("¿Deseas pasar el turno? (S / N): ") == "S":
                return

            posicion = int(input("Ingresa la ficha que quieres colocar: ")) - 1
            if posicion > 6:
                print("La ficha que seleccionaste no existe, por favor intenta otra vez")
                continue

            ficha = self.fichas[posicion]

            ficha_1 = None
            ficha_2 = None
            ultima_ficha_1 = None
            ultima_ficha_2 = None
            primera_ficha_1 = None
            primera_ficha_2 = None

            try:
                ficha_1 = ficha.cara[0]
                ficha_2 = ficha.cara[1]
                ultima_ficha_1 = ultima_ficha.cara[0]
                ultima_ficha_2 = ultima_ficha.cara[1]
                primera_ficha_1 = primera_ficha.cara[0]
                primera_ficha_2 = primera_ficha.cara[0]
            except:
                pass

            if ficha_1 == ultima_ficha_1 or ficha_1 == ultima_ficha_2:
                break
            elif ficha_2 == ultima_ficha_1 or ficha_2 == ultima_ficha_2:
                break
            elif ficha_1 == primera_ficha_1 or ficha_1 == primera_ficha_2:
                break
            elif ficha_2 == primera_ficha_1 or ficha_2 == primera_ficha_2:
                break
            else:
                print("La jugada que deseas hacer no es válida, por favor intenta otra vez")

        while True:

            posicion = input("¿Deseas colocar la ficha al inicio o al final? (I / F): ")
            if posicion == "I":
                if ficha.cara[1] != self.partida.colocadas[0].cara[0]:
                    ficha.voltear_ficha()
                self.partida.colocadas.appendleft(ficha)
                self.fichas.remove(ficha)

                if ficha.cara[0] == ficha.cara[1]:
                    self.jugar_doble()
                else:
                    return
            elif posicion == "F":
                if ficha.cara[0] != self.partida.colocadas[-1].cara[1]:
                    ficha.voltear_ficha()
                self.partida.colocadas.append(ficha)
                self.fichas.remove(ficha)

                if ficha.cara[0] == ficha.cara[1]:
                    self.jugar_doble()
                else:
                    return
            else:
                print("La opción que ingresaste no es válida, por favor intenta otra vez")


    def jugar_doble(self):
        print("Hola")

    def __str__(self):
        return f"¡Hola! Soy {self.nombre} y tengo {len(self.fichas)} fichas"
