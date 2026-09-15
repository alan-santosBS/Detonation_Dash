class Carro:

    """
    Representa o veículo controlado pelo jogador.

    Guarda o estado da partida (posição, avarias, campo de força) e as
    estatísticas que aparecem na tela final (tijolos percorridos e
    bombas explodidas).
    """

    def __init__(self, pos_x=0, pos_y=0, limite_avarias=3):
        # Estado do veículo no mapa
        self.x = pos_x
        self.y = pos_y

        # Sistema de avarias: quantas aguenta e quantas já tomou
        self.limite_avarias = limite_avarias
        self.avarias_atuais = 0

        # Campo de força absorve dano de bombas antes de contar avaria
        self.campo_forca = 0

        # Estatísticas exibidas na tela final
        self.tijolos_percorridos = 0
        self.bombas_explodidas = 0

    def mover_para(self, novo_x, novo_y):
        self.x = novo_x
        self.y = novo_y
        self.tijolos_percorridos += 1

    def receber_dano(self):
        # Conta a bomba independente de ter escudo ou não
        self.bombas_explodidas += 1

        # Se tiver campo de força, consome uma carga e evita a avaria
        if self.campo_forca > 0:
            self.campo_forca -= 1
        else:
            self.avarias_atuais += 1

    def recarregar_energia(self):
        self.campo_forca += 1

    def destruido(self):
        # Perde quando as avarias atuais alcançam o limite
        return self.avarias_atuais >= self.limite_avarias
