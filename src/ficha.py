class Ficha:

    def __init__(self, valor_1: str, valor_2: str, id_ficha: int):
        self.cara = [valor_1, valor_2]
        self.id = id_ficha

    def voltear_ficha(self):
        self.cara[0], self.cara[1] = self.cara[1], self.cara[0]

    def __str__(self):
        return f"|{self.cara[0]} | {self.cara[1]}| , ID = {self.id}"
