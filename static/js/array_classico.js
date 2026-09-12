/**
 * Simula um array clássico de tamanho fixo.
 *
 * Internamente usa um Array APENAS como buffer bruto de memória.
 * Toda a lógica de busca, inserção e remoção é implementada na mão
 * (percorrendo o buffer com laços), sem usar métodos prontos do Array
 * como indexOf, includes, push, splice, find, etc.
 *
 * O usuário só pode usar:
 *   - obter(i)        -> lê o valor no índice i
 *   - definir(i, v)   -> grava o valor v no índice i
 *   - tamanho         -> retorna o tamanho ocupado
 */
class ArrayClassico {
    constructor(capacidadeInicial) {
        if (capacidadeInicial <= 0) {
            throw new Error("O tamanho do array deve ser maior que zero.");
        }

        this._capacidade = capacidadeInicial;
        this._tamanho = 0;
        // Buffer bruto: Array usado SÓ como memória, não exposto ao resto do código
        this._buffer = new Array(capacidadeInicial);
    }

    get tamanho() {
        return this._tamanho;
    }

    get capacidade() {
        return this._capacidade;
    }

    obter(indice) {
        this._validarIndice(indice);
        return this._buffer[indice];
    }

    definir(indice, valor) {
        this._validarIndice(indice);
        this._buffer[indice] = valor;
        if (indice >= this._tamanho) {
            this._tamanho = indice + 1;
        }
    }

    /**
     * Busca um valor no array percorrendo índice por índice.
     * Retorna o índice encontrado ou -1 se não existir.
     * Implementação manual, sem indexOf/includes do Array nativo.
     */
    buscar(valor) {
        for (let i = 0; i < this._tamanho; i++) {
            if (this._buffer[i] === valor) {
                return i;
            }
        }
        return -1;
    }

    /**
     * Verifica se um valor está presente. Implementação manual.
     */
    contem(valor) {
        return this.buscar(valor) !== -1;
    }

    /**
     * Adiciona um valor no final do array.
     * Se o array estiver cheio, NÃO realoca — apenas avisa no console.
     * (A realocação ficaria mais complexa; pro caso das bandeiras o
     *  tamanho do tabuleiro já é o limite máximo, então reservamos
     *  a capacidade total desde o início.)
     */
    adicionar(valor) {
        if (this._tamanho >= this._capacidade) {
            console.warn("ArrayClassico cheio, não foi possível adicionar:", valor);
            return false;
        }
        this._buffer[this._tamanho] = valor;
        this._tamanho++;
        return true;
    }

    /**
     * Remove a primeira ocorrência do valor, deslocando os elementos
     * seguintes uma posição pra trás manualmente. Implementação manual.
     */
    remover(valor) {
        const indice = this.buscar(valor);
        if (indice === -1) {
            return false;
        }
        for (let i = indice; i < this._tamanho - 1; i++) {
            this._buffer[i] = this._buffer[i + 1];
        }
        this._buffer[this._tamanho - 1] = undefined;
        this._tamanho--;
        return true;
    }

    preencher(valor) {
        for (let i = 0; i < this._capacidade; i++) {
            this._buffer[i] = valor;
        }
        this._tamanho = this._capacidade;
    }

    _validarIndice(indice) {
        if (!Number.isInteger(indice)) {
            throw new Error("O índice precisa ser um número inteiro.");
        }
        if (indice < 0 || indice >= this._capacidade) {
            throw new Error(
                "Índice " + indice + " fora dos limites (0.." + (this._capacidade - 1) + ")."
            );
        }
    }
}
