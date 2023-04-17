from partida import Partida


class Bot:

    def __init__(self, nombre: str, fichas: list, partida: Partida):
        self.nombre = nombre
        self.fichas = fichas
        self.partida = partida

    def poner_ficha(self):

        # print("Tus fichas son: ")
        # contador = 1

        # for ficha in self.fichas:
        #     print(f"{contador}. {ficha}", sep="  ")
        #     contador += 1

        # print("#--------------------------------------------------")
        # print("")

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
            for ficha in jugadaDoble:
                if ficha.cara[0] == cola:
                    self.partida.colocadas.append(ficha)
                else:
                    self.partida.colocadas.appendleft(ficha)
                self.fichas.remove(ficha)
            print(f"{self.nombre} ha realizado su jugada")
            return

        for i in range(len(self.fichas) - 1, -1, -1):
            ficha = self.fichas[i]
            ficha_1 = ficha.cara[0]
            ficha_2 = ficha.cara[1]

            if ficha_1 == cabeza:
                ficha.voltear_ficha()
                self.partida.colocadas.appendleft(ficha)
                self.fichas.pop(i)
                print(f"{self.nombre} ha realizado su jugada")
                return
            elif ficha_2 == cabeza:
                self.partida.colocadas.appendleft(ficha)
                self.fichas.pop(i)
                print(f"{self.nombre} ha realizado su jugada")
                return
            elif ficha_1 == cola:
                self.partida.colocadas.append(ficha)
                self.fichas.pop(i)
                print(f"{self.nombre} ha realizado su jugada")
                return
            elif ficha_2 == cola:
                ficha.voltear_ficha()
                self.partida.colocadas.append(ficha)
                self.fichas.pop(i)
                print(f"{self.nombre} ha realizado su jugada")
                return

        print(f"{self.nombre} pasa el turno")
        return

    def __str__(self):
        return f"¡Hola! Soy {self.nombre} y tengo {len(self.fichas)} fichas"
