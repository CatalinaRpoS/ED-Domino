from ficha import Ficha
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
            
            print(f"{contador}. {ficha}", sep = "  ")
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

            if input("Deseas pasar (Y / N): ") == "Y":
                return

            ficha = self.fichas[int(input("Ingresa la ficha que quieres colocar: ")) - 1]

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

            print(ficha_1 )
            print(ficha_2 )
            print(ultima_ficha_1 )
            print(ultima_ficha_2 )
            print(primera_ficha_1 )
            print(primera_ficha_2 )

            if ficha_1 == ultima_ficha_1 or ficha_1 == ultima_ficha_2:
                break
            
            elif ficha_2 == ultima_ficha_1 or ficha_2 == ultima_ficha_2:
                break

            elif ficha_1 == primera_ficha_1 or ficha_1 == primera_ficha_2:
                break
            
            elif ficha_2 == primera_ficha_1 or ficha_2 == primera_ficha_2:
                break
                    

        while True:

            posicion = input("Ingresar la ficha al inicio o al final (I / F): ")
            
            if posicion == "I":
                
                self.partida.colocadas.appendleft(ficha)
                return
            
            if posicion == "F":

                self.partida.colocadas.append(ficha)
                return
            
            else:
                print("Un cursito de lectura critica no vendria mal")
        

    def __str__(self):
        return f"¡Hola! Soy {self.nombre} y tengo {len(self.fichas)} fichas"
