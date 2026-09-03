class Carro:
    def __init__(self, pos_x=0, pos_y=0, limite_avarias=3):
        self.x = pos_x
        self.y = pos_y
        self.limite_avarias = limite_avarias
        self.avarias_atuais = 0
        self.campo_forca = 0
        self.tijolos_percorridos = 0
        self.bombas_explodidas = 0

    def mover_para(self, novo_x, novo_y):
        self.x = novo_x
        self.y = novo_y
        self.tijolos_percorridos += 1

    def receber_dano(self):
        self.bombas_explodidas += 1
        # Se possuir escudo, absorve o dano sem causar avaria
        if self.campo_forca > 0:
            self.campo_forca -= 1
        else:
            self.avarias_atuais += 1

    def recarregar_energia(self):
        self.campo_forca += 1

    def destruido(self):
        return self.avarias_atuais >= self.limite_avarias