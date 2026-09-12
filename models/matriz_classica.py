from .array_classico import ArrayClassico

class MatrizClassica:
    """
    Array 2D clássico: um array de arrays de tamanho fixo.
    Cada linha é um ArrayClassico.

    Só expõe acesso por índice duplo e as dimensões.
    Nada de append, remove, in, etc.
    """

    def __init__(self, linhas, colunas, valor_inicial=None):
        if linhas <= 0 or colunas <= 0:
            raise ValueError("A matriz precisa ter pelo menos 1 linha e 1 coluna.")

        self._linhas = linhas
        self._colunas = colunas

        # Array clássico que guarda as linhas
        self._linhas_dados = ArrayClassico(linhas)

        # Cada posição do array de linhas é um ArrayClassico (uma linha)
        for i in range(linhas):
            self._linhas_dados.definir(i, ArrayClassico(colunas, valor_inicial))

    @property
    def linhas(self):
        return self._linhas

    @property
    def colunas(self):
        return self._colunas

    def obter(self, i, j):
        self._validar_posicao(i, j)
        linha = self._linhas_dados.obter(i)
        return linha.obter(j)

    def definir(self, i, j, valor):
        self._validar_posicao(i, j)
        linha = self._linhas_dados.obter(i)
        linha.definir(j, valor)

    def preencher(self, valor):
        for i in range(self._linhas):
            linha = self._linhas_dados.obter(i)
            linha.preencher(valor)

    def _validar_posicao(self, i, j):
        if not isinstance(i, int) or not isinstance(j, int):
            raise TypeError("Os índices precisam ser inteiros.")
        if i < 0 or i >= self._linhas or j < 0 or j >= self._colunas:
            raise IndexError(
                f"Posição ({i}, {j}) fora dos limites "
                f"(0..{self._linhas - 1}, 0..{self._colunas - 1})."
            )

    def __str__(self):
        linhas_str = []
        for i in range(self._linhas):
            linhas_str.append(str(self._linhas_dados.obter(i)))
        return "\n".join(linhas_str)
