import random
from .matriz_classica import MatrizClassica


class Tabuleiro:
    def __init__(self, tamanho, qtd_bombas, qtd_energias): # recebe o tamanho do tabuleiro, a quantidade de bombas e a quantidade de energias
        self.tamanho = tamanho
        self.inicio = (0, 0) # define a posição inicial do carro no canto superior esquerdo do tabuleiro
        self.fim = (tamanho - 1, tamanho - 1)

        valido = False
        while not valido: # Garante que o tabuleiro tenha um caminho válido do início ao fim, evitando que o jogador fique preso
            self.matriz = MatrizClassica(tamanho, tamanho, 0) # Cria a matriz do tabuleiro preenchida com 0 (vazio)
            self.matriz.definir(self.inicio[0], self.inicio[1], 3)
            self.matriz.definir(self.fim[0], self.fim[1], 4)

            self._posicionar_elementos(1, qtd_bombas) 
            self._posicionar_elementos(2, qtd_energias)

            valido = self.tem_caminho_valido()

        # Cria a matriz de reveladas, que indica quais células foram reveladas pelo jogador (0 = oculta, 1 = revelada)
        self.revelada = MatrizClassica(tamanho, tamanho, 0)
        self.revelar_celula(0, 0)  # Revela a posição inicial

    def _posicionar_elementos(self, tipo_elemento, quantidade):
        colocados = 0
        while colocados < quantidade:
            x = random.randint(0, self.tamanho - 1) # Posiciona as bombas (1) e energias (2) aleatoriamente no tabuleiro com o random
            y = random.randint(0, self.tamanho - 1)
            if self.matriz.obter(x, y) == 0: # se for 0 coloca o elemento, se não, tenta novamente
                self.matriz.definir(x, y, tipo_elemento)
                colocados += 1

    def contar_bombas_vizinhas(self, x, y): # Conta o número de bombas (1) ao redor da célula (x, y) no tabuleiro
        bombas = 0
        for dx in [-1, 0, 1]: # testa os 8 vizinhos da célula (x, y) para contar quantas bombas existem ao redor dela
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy

                if 0 <= nx < self.tamanho and 0 <= ny < self.tamanho: # Valida se o vizinho está dentro dos limites do tabuleiro
                    if self.matriz.obter(nx, ny) == 1:  # 1 = Bomba
                        bombas += 1
        return bombas

    def revelar_celula(self, x, y): # Revela a célula (x, y) no tabuleiro, marcando-a como revelada na matriz de reveladas
        # Validação de limites
        if x < 0 or x >= self.tamanho or y < 0 or y >= self.tamanho:
            return
        if self.revelada.obter(x, y) == 1:
            return

        self.revelada.definir(x, y, 1)

        # RECURSÃO (Flood Fill): se o tijolo for vazio e não tiver bombas ao redor, revela vizinhos
        if self.matriz.obter(x, y) == 0 and self.contar_bombas_vizinhas(x, y) == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx != 0 or dy != 0:
                        self.revelar_celula(x + dx, y + dy)

    def tem_caminho_valido(self): # Verifica se existe um caminho válido do início ao fim do tabuleiro, evitando que o jogador fique preso
        
        visitado = MatrizClassica(self.tamanho, self.tamanho, 0)

        def flood_fill(x, y):
            if x < 0 or x >= self.tamanho or y < 0 or y >= self.tamanho:
                return False
            if self.matriz.obter(x, y) == 1 or visitado.obter(x, y) == 1:
                return False
            if self.matriz.obter(x, y) == 4:
                return True
            visitado.definir(x, y, 1)
            return (
                flood_fill(x - 1, y)
                or flood_fill(x + 1, y)
                or flood_fill(x, y - 1)
                or flood_fill(x, y + 1)
            )

        return flood_fill(self.inicio[0], self.inicio[1]) # se retornar false ele cria um novo tabuleito e testa os caminhos novamente
