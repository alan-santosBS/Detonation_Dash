class ArrayClassico:
    """
    Simula um array clássico de tamanho fixo.

    Usa uma lista APENAS como buffer bruto de memória. Toda a lógica
    de acesso, validação e operações é feita manualmente — sem
    atalhos como append, remove ou index.

    Interface pública:
      - obter(i)      -> lê o valor no índice i
      - definir(i, v) -> grava o valor v no índice i
      - tamanho       -> retorna o tamanho do array
    """

    def __init__(self, tamanho, valor_inicial=None):
        # Tamanho fixo: precisa ser positivo
        if tamanho <= 0:
            raise ValueError("O tamanho do array deve ser maior que zero.")

        self._tamanho = tamanho
        # Buffer bruto: lista usada só como memória, não exposta externamente
        self._buffer = [valor_inicial] * tamanho

    @property
    def tamanho(self):
        return self._tamanho

    def obter(self, indice):
        # Valida antes de ler — comportamento de array clássico
        self._validar_indice(indice)
        return self._buffer[indice]

    def definir(self, indice, valor):
        # Valida antes de gravar
        self._validar_indice(indice)
        self._buffer[indice] = valor

    def preencher(self, valor):
        """Preenche todo o array com um mesmo valor."""
        for i in range(self._tamanho):
            self._buffer[i] = valor

    def _validar_indice(self, indice):
        # Garante que o índice é inteiro e está dentro dos limites.
        # É o equivalente à proteção que um array de C/Java oferece.
        if not isinstance(indice, int):
            raise TypeError("O índice precisa ser um número inteiro.")
        if indice < 0 or indice >= self._tamanho:
            raise IndexError(
                f"Índice {indice} fora dos limites (0..{self._tamanho - 1})."
            )

    def __str__(self):
        itens = []
        for i in range(self._tamanho):
            itens.append(str(self._buffer[i]))
        return "[" + ", ".join(itens) + "]"
