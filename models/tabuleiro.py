import random
from .matriz_classica import MatrizClassica


class Tabuleiro:
    def __init__(self, tamanho, qtd_bombas, qtd_energias):
        self.tamanho = tamanho
        self.inicio = (0, 0)
        self.fim = (tamanho - 1, tamanho - 1)

        valido = False
        while not valido:
            self.matriz = MatrizClassica(tamanho, tamanho, 0)
            self.matriz.definir(self.inicio[0], self.inicio[1], 3)
            self.matriz.definir(self.fim[0], self.fim[1], 4)

            self._posicionar_elementos(1, qtd_bombas)
            self._posicionar_elementos(2, qtd_energias)

            valido = self.tem_caminho_valido()

        # Matriz estática para controle de visibilidade (0 = oculta, 1 = revelada)
        # Ainda é uma lista por enquanto; será refatorada no sub-passo 3.2
        self.revelada = [[0 for _ in range(tamanho)] for _ in range(tamanho)]
        self.revelar_celula(0, 0)  # Revela a posição inicial

    def _posicionar_elementos(self, tipo_elemento, quantidade):
        colocados = 0
        while colocados < quantidade:
            x = random.randint(0, self.tamanho - 1)
            y = random.randint(0, self.tamanho - 1)
            if self.matriz.obter(x, y) == 0:
                self.matriz.definir(x, y, tipo_elemento)
                colocados += 1

    def contar_bombas_vizinhas(self, x, y):
        bombas = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.tamanho and 0 <= ny < self.tamanho:
                    if self.matriz.obter(nx, ny) == 1:  # 1 = Bomba
                        bombas += 1
        return bombas

    def revelar_celula(self, x, y):
        # Validação de limites
        if x < 0 or x >= self.tamanho or y < 0 or y >= self.tamanho:
            return
        if self.revelada[x][y] == 1:
            return

        self.revelada[x][y] = 1

        # RECURSÃO (Flood Fill): se o tijolo for vazio e não tiver bombas ao redor, revela vizinhos
        if self.matriz.obter(x, y) == 0 and self.contar_bombas_vizinhas(x, y) == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx != 0 or dy != 0:
                        self.revelar_celula(x + dx, y + dy)

    def tem_caminho_valido(self):
        visitado = [[0 for _ in range(self.tamanho)] for _ in range(self.tamanho)]

        def flood_fill(x, y):
            if x < 0 or x >= self.tamanho or y < 0 or y >= self.tamanho:
                return False
            if self.matriz.obter(x, y) == 1 or visitado[x][y] == 1:
                return False
            if self.matriz.obter(x, y) == 4:
                return True
            visitado[x][y] = 1
            return (
                flood_fill(x - 1, y)
                or flood_fill(x + 1, y)
                or flood_fill(x, y - 1)
                or flood_fill(x, y + 1)
            )

        return flood_fill(self.inicio[0], self.inicio[1])
