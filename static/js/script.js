let estadoCarro = { x: 0, y: 0 };
let ehPulo = false;

window.addEventListener('keydown', (e) => {
    if (e.code === 'Space') {
        ehPulo = true;
        destacarCarroPulo(true);
    }
    
    if (['ArrowUp', 'ArrowDown', 'ArrowLeft', 'ArrowRight'].includes(e.code)) {
        e.preventDefault();
        calcularEEnviarMovimento(e.code);
    }
});

window.addEventListener('keyup', (e) => {
    if (e.code === 'Space') {
        ehPulo = false;
        destacarCarroPulo(false);
    }
});

function destacarCarroPulo(ativo) {
    const celulaCarro = document.querySelector('.celula.carro');
    if (celulaCarro) {
        if (ativo) {
            celulaCarro.classList.add('pulando');
            celulaCarro.innerText = '🚀';
        } else {
            celulaCarro.classList.remove('pulando');
            celulaCarro.innerText = '🏎️';
        }
    }
}

function calcularEEnviarMovimento(tecla) {
    let novoX = estadoCarro.x;
    let novoY = estadoCarro.y;

    if (tecla === 'ArrowUp') novoX -= 1;
    if (tecla === 'ArrowDown') novoX += 1;
    if (tecla === 'ArrowLeft') novoY -= 1;
    if (tecla === 'ArrowRight') novoY += 1;

    fetch('/mover', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ x: novoX, y: novoY, pulo: ehPulo })
    })
    .then(response => response.json())
    .then(dados => {
        if (dados.vitoria || dados.derrota) {
            window.location.href = '/estatisticas';
        } else {
            carregarEstadoJogo();
        }
    })
    .catch(err => console.error("Erro na movimentação:", err));
}

function carregarEstadoJogo() {
    fetch('/obter_estado')
        .then(res => res.json())
        .then(dados => {
            if (dados.erro) return;

            document.getElementById('tempo').innerText = dados.tempo_decorrido;
            document.getElementById('escudo').innerText = dados.carro.campo_forca;
            document.getElementById('avarias').innerText = dados.carro.avarias_atuais;
            document.getElementById('limite-avarias').innerText = dados.carro.limite_avarias;
            document.getElementById('tijolos').innerText = dados.carro.tijolos_percorridos;

            estadoCarro.x = dados.carro.x;
            estadoCarro.y = dados.carro.y;

            const grid = document.getElementById('grid-tabuleiro');
            if (!grid) return;

            grid.style.gridTemplateColumns = `repeat(${dados.tamanho}, 40px)`;
            grid.innerHTML = '';

            for (let i = 0; i < dados.tamanho; i++) {
                for (let j = 0; j < dados.tamanho; j++) {
                    const celula = document.createElement('div');
                    celula.classList.add('celula');

                    const estaRevelada = dados.revelada && dados.revelada[i] && dados.revelada[i][j] === 1;

                    if (i === dados.carro.x && j === dados.carro.y) {
                        celula.classList.add('carro');
                        celula.innerText = ehPulo ? '🚀' : '🏎️';
                    } else if (!estaRevelada) {
                        celula.classList.add('oculta');
                    } else {
                        celula.classList.add('revelada');
                        
                        if (dados.matriz[i][j] === 3) {
                            celula.classList.add('inicio');
                            celula.innerText = '🚩';
                        } else if (dados.matriz[i][j] === 4) {
                            celula.classList.add('fim');
                            celula.innerText = '🏁';
                        } else {
                            const numBombas = dados.vizinhanca[i][j];
                            if (numBombas > 0) {
                                celula.innerText = numBombas;
                            }
                        }
                    }

                    grid.appendChild(celula);
                }
            }
        })
        .catch(err => console.error("Erro ao carregar o mapa:", err));
}

carregarEstadoJogo();
setInterval(carregarEstadoJogo, 1000);