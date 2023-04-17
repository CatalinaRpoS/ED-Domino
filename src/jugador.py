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
        
        ficha_1 = None
        ficha_2 = None
        ultima_ficha_1 = None
        ultima_ficha_2 = None
        primera_ficha_1 = None
        primera_ficha_2 = None
        fichasDobles = None

        try:
            
            cola = ultima_ficha.cara[1]
            cabeza = primera_ficha.cara[0]

            fichasDobles = [x for x in self.fichas 
                            if x.id == 1 or x.id == 8 or x.id == 14 or
                            x.id == 19 or x.id == 23 or x.id == 26 or x.id == 28]
            
        except:
            pass

        jugadaDoble = list(filter(lambda ficha: ficha.cara[0] == cola or ficha.cara[0] == cabeza, fichasDobles))

        if len(jugadaDoble) == 2:

            if input("Tienes la oportunidad de hacer una jugada doble, ¿Quieres realizarla? (S / N):") == "S":
                
                for ficha in jugadaDoble:

                    if ficha.cara[0] == cola:
                        self.partida.colocadas.append(ficha)
                    
                    else:
                        self.partida.colocadas.appendleft(ficha)
                    
                    self.fichas.remove(ficha)

        while True:

            if input("¿Deseas pasar el turno? (S / N): ") == "S":
                return

            posicion = int(input("Ingresa la ficha que quieres colocar: ")) 
            
            if posicion > len(self.fichas) and posicion < 1:
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

        while True:

            posicion = input("¿Deseas colocar la ficha al inicio o al final? (I / F): ")
            if posicion == "I":
                if ficha.cara[1] != self.partida.colocadas[0].cara[0]:
                    ficha.voltear_ficha()
                self.partida.colocadas.appendleft(ficha)
                self.fichas.remove(ficha)

            elif posicion == "F":
                if ficha.cara[0] != self.partida.colocadas[-1].cara[1]:
                    ficha.voltear_ficha()
                self.partida.colocadas.append(ficha)
                self.fichas.remove(ficha)

            else:
                print("La opción que ingresaste no es válida, por favor intenta otra vez")


    def __str__(self):
        return f"¡Hola! Soy {self.nombre} y tengo {len(self.fichas)} fichas"
