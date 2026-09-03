from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from models import Carro, Tabuleiro
import time

app = Flask(__name__)
app.secret_key = 'chave_secreta_campo_minado'

# Dicionário em memória para armazenar o estado ativo da partida
partida = {
    'carro': None,
    'tabuleiro': None,
    'tempo_inicio': 0,
    'tempo_fim': 0
}

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/selecionar_tamanho')
def selecionar_tamanho():
    return render_template('selecionar_tamanho.html')

@app.route('/iniciar_jogo', methods=['POST'])
def iniciar_jogo():
    dados = request.get_json()
    tamanho = int(dados.get('tamanho', 10))
    qtd_bombas = int(dados.get('bombas', 5))
    qtd_energias = int(dados.get('energias', 3))

    # Instancia as classes e registra o tempo inicial
    partida['tabuleiro'] = Tabuleiro(tamanho, qtd_bombas, qtd_energias)
    partida['carro'] = Carro(pos_x=0, pos_y=0, limite_avarias=3)
    partida['tempo_inicio'] = time.time()
    
    return jsonify({'status': 'ok', 'redirect': url_for('jogo')})

@app.route('/jogo')
def jogo():
    if not partida['tabuleiro']:
        return redirect(url_for('selecionar_tamanho'))
    return render_template('jogo.html')

@app.route('/obter_estado', methods=['GET'])
def obter_estado():
    # Envia o estado atual do tabuleiro e do carrinho para a tela
    carro = partida['carro']
    tabuleiro = partida['tabuleiro']
    tempo_decorrido = int(time.time() - partida['tempo_inicio'])

    return jsonify({
        'tamanho': tabuleiro.tamanho,
        'matriz': tabuleiro.matriz,
        'carro': {
            'x': carro.x,
            'y': carro.y,
            'avarias_atuais': carro.avarias_atuais,
            'limite_avarias': carro.limite_avarias,
            'campo_forca': carro.campo_forca,
            'tijolos_percorridos': carro.tijolos_percorridos
        },
        'tempo_decorrido': tempo_decorrido
    })

@app.route('/mover', methods=['POST'])
def mover():
    dados = request.get_json()
    destino_x = dados.get('x')
    destino_y = dados.get('y')
    eh_pulo = dados.get('pulo', False)

    carro = partida['carro']
    tabuleiro = partida['tabuleiro']

    # Validação do movimento (muda de posição e processa a célula)
    carro.mover_para(destino_x, destino_y)
    
    conteudo_celula = tabuleiro.matriz[destino_x][destino_y]
    
    if eh_pulo:
        # Pular um tijolo ignora bomba e energia, mas conta como movimento percorrido
        pass
    else:
        if conteudo_celula == 1:  # Bomba
            carro.receber_dano()
            tabuleiro.matriz[destino_x][destino_y] = 0  # Desativa bomba explodida
        elif conteudo_celula == 2:  # Energia
            carro.recarregar_energia()
            tabuleiro.matriz[destino_x][destino_y] = 0  # Consome energia

    # Checa condições de vitória ou derrota
    derrota = carro.destruido()
    vitoria = (carro.x == tabuleiro.fim[0] and carro.y == tabuleiro.fim[1])

    if vitoria or derrota:
        partida['tempo_fim'] = time.time()

    return jsonify({
        'carro': {
            'x': carro.x,
            'y': carro.y,
            'avarias_atuais': carro.avarias_atuais,
            'campo_forca': carro.campo_forca,
            'tijolos_percorridos': carro.tijolos_percorridos
        },
        'vitoria': vitoria,
        'derrota': derrota
    })

@app.route('/estatisticas')
def estatisticas():
    carro = partida['carro']
    tempo_total = int(partida['tempo_fim'] - partida['tempo_inicio']) if partida['tempo_fim'] else 0
    vitoria = (carro.x == partida['tabuleiro'].fim[0] and carro.y == partida['tabuleiro'].fim[1]) if carro else False

    dados_finais = {
        'sucesso': vitoria,
        'tempo_total': tempo_total,
        'bombas_explodidas': carro.bombas_explodidas if carro else 0,
        'tijolos_percorridos': carro.tijolos_percorridos if carro else 0,
        'resistência_restante': (carro.limite_avarias - carro.avarias_atuais) if carro else 0
    }
    return render_template('estatisticas.html', stats=dados_finais)

if __name__ == '__main__':
    app.run(debug=True)