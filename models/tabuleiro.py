import random

class Tabuleiro:
    def __init__(self, tamanho, qtd_bombas, qtd_energias):
        self.tamanho = tamanho
        self.inicio = (0, 0)
        self.fim = (tamanho - 1, tamanho - 1)
        
        # Garante a criação de um mapa com caminho solucionável
        valido = False
        while not valido:
            # Inicialização de matriz bidimensional estática (sem métodos dinâmicos)
            self.matriz = [[0 for _ in range(tamanho)] for _ in range(tamanho)]
            self.matriz[self.inicio[0]][self.inicio[1]] = 3  # Início
            self.matriz[self.fim[0]][self.fim[1]] = 4         # Chegada
            
            self._posicionar_elementos(1, qtd_bombas)   # Sorteia Bombas
            self._posicionar_elementos(2, qtd_energias) # Sorteia Energias
            
            valido = self.tem_caminho_valido()

    def _posicionar_elementos(self, tipo_elemento, quantidade):
        colocados = 0
        while colocados < quantidade:
            x = random.randint(0, self.tamanho - 1)
            y = random.randint(0, self.tamanho - 1)
            if self.matriz[x][y] == 0:
                self.matriz[x][y] = tipo_elemento
                colocados += 1

    def tem_caminho_valido(self):
        # Matriz estática de controle para posições já visitadas
        visitado = [[0 for _ in range(self.tamanho)] for _ in range(self.tamanho)]
        
        def flood_fill(x, y):
            # Parada 1: Posição fora dos limites do array
            if x < 0 or x >= self.tamanho or y < 0 or y >= self.tamanho:
                return False
            # Parada 2: Encontrou bomba (1) ou célula já testada (1)
            if self.matriz[x][y] == 1 or visitado[x][y] == 1:
                return False
            # Vitória: Alcançou o objetivo final (4)
            if self.matriz[x][y] == 4:
                return True
            
            visitado[x][y] = 1
            
            # Navegação recursiva em 4 direções
            if flood_fill(x - 1, y): return True  # Cima
            if flood_fill(x + 1, y): return True  # Baixo
            if flood_fill(x, y - 1): return True  # Esquerda
            if flood_fill(x, y + 1): return True  # Direita
            
            return False

        return flood_fill(self.inicio[0], self.inicio[1])