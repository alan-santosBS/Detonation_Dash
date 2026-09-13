# 🏁 Detonation Dash

Jogo web desenvolvido como trabalho da disciplina de **Algoritmos e Estruturas de Dados** do curso de **Tecnologia em Sistemas para Internet (TSI)** do IFPE.

O jogador controla um carrinho 🏎️ que precisa atravessar um mapa quadrado de tijolos, do canto superior esquerdo até o canto inferior direito, evitando bombas 💣 e coletando energia ⚡ pelo caminho.

---

## 👥 Integrantes

| Nome | GitHub |
|------|--------|
| Alan Santos | [@alan-santosBS](https://github.com/alan-santosBS) |
| Luhan Felipe | [@luhanfelipe](https://github.com/luhanfelipe) |
| Luísa Vitória | [@luisavmf0](https://github.com/luisavmf0) |

---

## 🎮 Como jogar

1. Na tela inicial, clique em **INICIAR**
2. Escolha o tamanho do mapa (8x8, 12x12 ou 16x16) e a dificuldade
3. Use as **setas do teclado** para mover o carrinho
4. Segure a tecla **ESPAÇO** enquanto anda para **pular** um tijolo que você suspeite ter bomba
5. Chegue até o quadrado final (canto inferior direito) sem estourar o limite de avarias

### Elementos do mapa

- 🏎️ **Carro:** onde você está
- 🚩 **Início:** ponto de partida
- 🏁 **Fim:** ponto de chegada
- 💣 **Bomba:** causa avaria (ou consome campo de força)
- ⚡ **Energia:** aumenta o campo de força do carro
- 🚩 (marcação): bandeira que você pode deixar em casas suspeitas

---

## ✨ Funcionalidades

- Mapa quadrado com tamanho configurável pelo jogador
- Posicionamento aleatório de bombas e cargas de energia
- Sistema de avarias com limite que pode destruir o carro
- Campo de força que absorve danos
- Pulo de tijolo para casas suspeitas
- Painel de informações em tempo real (tempo, avarias, campo de força, tijolos percorridos)
- Tela de estatísticas final (tempo total, bombas explodidas, tijolos percorridos e resultado)
- Marcação de casas suspeitas com bandeiras
- Tela "Sobre" com informações do grupo e do projeto

---

## 🏗️ Arquitetura

- **Backend:** Python 3 + Flask
- **Frontend:** HTML5, CSS3 e JavaScript puro
- **Modelos (POO):**
  - `Carro` — posição, avarias, campo de força e estatísticas
  - `Tabuleiro` — mapa, bombas, energias, revelação e validação de caminho
  - `ArrayClassico` — array unidimensional de tamanho fixo
  - `MatrizClassica` — array bidimensional construído sobre `ArrayClassico`

### 📌 Destaque técnico: Arrays Clássicos

O trabalho exige o uso de **arrays clássicos** — estruturas de tamanho fixo acessadas apenas por índice, com o tamanho conhecido, sem utilizar recursos prontos das linguagens (como `append`, `in`, `Set`, compreensões de lista, etc).

Como Python não possui um array clássico nativo, foram implementadas duas classes próprias:

- **`ArrayClassico`** (`models/array_classico.py`) — simula um array de 1 dimensão. Expõe apenas `obter(i)`, `definir(i, v)` e `tamanho`. Internamente usa uma lista do Python **apenas como buffer bruto**, sem expor nenhuma operação avançada.
- **`MatrizClassica`** (`models/matriz_classica.py`) — array 2D construído sobre `ArrayClassico`. A matriz é um array de linhas, e cada linha é um `ArrayClassico`.

No front-end, o mesmo padrão foi aplicado em JavaScript com uma classe `ArrayClassico` própria (`static/js/array_classico.js`), usada no lugar de `Set` para armazenar as bandeiras marcadas pelo jogador.

---

## 🚀 Como executar

### Pré-requisitos

- Python 3.10 ou superior
- pip

### Passo a passo

## 1. Clonar o repositório
git clone https://github.com/luhanfelipe/Detonation_Dash.git
cd Detonation_Dash

## 2. Criar e ativar o ambiente virtual
python3 -m venv venv

source venv/bin/activate        # Linux/macOS
ou: venv\Scripts\activate       # Windows

## 3. Instalar dependências
pip install flask

## 4. Executar
python3 app.py
Acesse em: http://localhost:5000

---

### 🛠️ Tecnologias

- Python 3
- Flask
- HTML5
- CSS3
- JavaScript

---

## O que fazer

1. Abre o `README.md` no Pulsar
2. **Ctrl+A** → **Delete**
3. Cola o conteúdo acima
4. Salva
