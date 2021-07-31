from gld_script_portfolio.jogos.interface_cartas import *
from gld_script_portfolio.jogos.metodos_cartas import *
from random import randint
from time import sleep as s

cabecalho('PIFE ELETRÔNICO', tipoc=1)
while True:
    entrada = menu('OPÇÕES', ('INICIAR JOGO', 'DESLIGAR JOGO'))
    if entrada not in (1, 2):
        continue
    else:
        break
if entrada == 1:
    while True:
        familia = leiaint('Seleciona o número de jogadores (1 a 6)')
        if familia in (1, 2, 3, 4, 5, 6):
            break
        else:
            continue

    # Dando as cartas aos jogadores e formatando suas telas
    jogo = cria_jogo()
    monte = jogo[len(jogo)-1]
    descarte = list()
    num_jogadores = familia
    cores = ['VM', 'VD', 'AM', 'AZ', 'MA', 'CY']
    class Jogador():
        def __init__(self, mao='', cor=''):
            self.m = mao
            self.c = cor

        def __str__(self, mao=False, cor=False):
            if mao:
                return self.m
            if cor:
                return self.c
            else:
                return f'Cartas do jogador: {self.m} | Cor do jogador: {self.c}'

        def escolhe_mao(self):
            self.m = arruma_trinca(jogo[0])

        def escolhe_cor(self, nova_cor):
            self.c = nova_cor

        def usa_mao(self):
            return self.m

        def usa_cor(self):
            return self.c


    jogadores = dict()
    for numero in range(0, num_jogadores):
        cor_sorteada = randint(0, 5-numero)
        jogadores[f"jogador{numero}"] = Jogador(arruma_trinca(jogo[numero]), cores[cor_sorteada])
        cores.remove(cores[cor_sorteada])

    # Exibindo as cartas aos jogadores

    for numero in range(0, num_jogadores):
        cabecalho(f'Mão do jogador {numero+1}:', tipoc=2, cor=(jogadores[f"jogador{numero}"].usa_cor()))
        mostra_mao(arruma_trinca(jogadores[f"jogador{numero}"].usa_mao()))
        s(1)

    # Excecução do jogo

    while True:
        for numero in range(0, num_jogadores):
            cabecalho(f'Vez do jogador {numero+1}:', tipoc=2, cor=(jogadores[f"jogador{numero}"].usa_cor()))
            cabecalho(f'Sua mão atual:'.center(tamcol), tipoc=3)
            mostra_mao(jogadores[f"jogador{numero}"].usa_mao())
            linha(tipol=3)
            compra_carta(jogadores[f"jogador{numero}"].usa_mao(), monte, descarte)
        while True:
            continuar = leiaint('Continuar? [Sim: 0 | Não: 1]')
            if continuar not in (0, 1):
                continuar = leiaint('Continuar? [Sim: 0 | Não: 1]')
            else:
                break
        if continuar == 0:
            continue
        else:
            desl()
            break

if entrada == 2:
    desl()

# Métodos que ainda precisam ser criados:
    # arruma_série: arruma cartas se estão em série
        # em desenvolvimento, com bug, mas apenas como método independente
        # na forma final, ele precisará se conciliar com arruma trinca, talvez integrando ambos
    # reembaralhamento
        # se a última carta do monte for exibida, reconstrói o monte com as cartas da pilha de descarte
    # vitoria
        # confere se as cartas de certa mão "batem"
