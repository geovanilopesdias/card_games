def cria_baralho_frances(q=2):
    """
    Constrói listas-baralhos com todas a cartas, exceto coringas.
    Se valor de q estiver definido para um valor maior que 1, q baralhos
    são gerados. Do contrário, levanta uma exceção de valor.
    :param q: quantidade de caixa de baralhos a gerar; default = 2.
    :return: lista de q baralhos.
    """

    if q < 1:
        raise ValueError('O número de baralhos deve ser igual ou maior a um!')
    caixa = [[valor, naipe] for naipe in ['♥', '♦', '♣', '♠'] for valor in range(1, 14)]
    return caixa * q


def cria_baralho_espanhol(q=1):
    """
    Constrói lista de baralho de truco.
    :param q: quantidade de caixa de baralhos a gerar; default = 1.
    :return: lista com cartas de baralho de truco.
    """
    if q < 1:
        raise ValueError('O número de baralhos deve ser igual ou maior a um!')
    caixa = [[valor, naipe] for naipe in range(3, 7) for valor in range(1, 11)]
    return caixa * q


def exibe_carta(carta):
    if carta[0] == 1:
        carta_editada = 'A'+carta[1]
    elif carta[0] == 11:
        carta_editada = 'J'+carta[1]
    elif carta[0] == 12:
        carta_editada = 'Q'+carta[1]
    elif carta[0] == 13:
        carta_editada = 'K'+carta[1]
    else:
        carta_editada = str(carta[0])+carta[1]

    return carta_editada


def arruma_mao(mao):
    """
    Organiza os elementos da lista "mao", identificando trincas, preferencialmente, e sequências após.
    Nota 1: Para fins de simplificação do método, assume-se que Ás possui apenas o valor unitário.
    Nota 2: A identificação de trincas é preferencial, pois a probabilidade de formá-la é maior que a da sequência.
    Seja n o valor de cartas na mão. As possibilidades de trinca é de 24n, mas de sequências é de 4(n-2).
    :param mao: lista das cartas a serem analisadas.
    :return: Parâmetro mao, com os mesmos elementos da lista "mao".
    """
    if type(mao) != list:
        raise TypeError('Parâmetro "mao" precisa ser uma lista!')
    if len(mao) < 3:
        raise IndexError('Método não funcionará para mãos com menos de 3 cartas!')
    trio = list()
    # Trinca
    mao.sort(key=lambda x: (x[0], x[1]))
    a = 0
    while a < len(mao)-2:  # iteração de índices até antepenúltimo da mão
        naipes_diferentes = (mao[a][1] != mao[a + 1][1] != mao[a + 2][1])
        valores_iguais = (mao[a][0] == mao[a + 1][0] == mao[a + 2][0])
        if naipes_diferentes and valores_iguais:
            trio.extend([mao[a], mao[a + 1], mao[a + 2]])
            mao.remove(mao[a])
            mao.remove(mao[a + 1])
            mao.remove(mao[a + 2])
        a += 1

    # Sequência
    mao.sort(key=lambda x: (x[1], x[0]))  # Organiza primeiro por naipe, após em ordem crescente
    a = 0
    while a < len(mao) - 2:
        naipes_iguais = (mao[a][1] == mao[a+1][1] == mao[a+2][1])
        valores_subsequentes = (mao[a][0] == mao[a+1][0]-1 == mao[a+2][0]-2)
        if naipes_iguais and valores_subsequentes:
            trio.extend([mao[a], mao[a+1], mao[a+2]])
            mao.remove(mao[a])
            mao.remove(mao[a + 1])
            mao.remove(mao[a + 2])
        a += 1

    fim = True if len(trio) == 9 else False

    # Reforma
    mao.sort(key=lambda x: (x[0], x[1]))
    if trio:
        mao.extend(trio)

    return mao, fim


def cria_jogo(q=2, num_cartas=9, jogadores=2, tipo=0):
    """
    Constrói condição inicial de um jogo de cartas de turnos para certo número de jogadores, com certo número de cartas
    a partir de uma lista de cartas a receber como parâmetro.
    Retorna a lista "jogo", com uma lista para cada jogador no início e a lista do monte
    restante como último elemento.
        Para receber o monte corretamente, usar o output do método como:
            jogo = cria_jogo()

            monte = jogo[len(jogo)-1]
        Para receber a mão de cada jogador corretamente, usar o output do método como:
            jogador_1 = jogo[0]

            jogador_2 = jogo[1]
            etc.

        Ou uma iteração com dicionários.
    :param q: Quantidade de baralhos disponível para construção da mão. Usado ao chamar um dos métodos que geram
                baralhos.
    :param num_cartas: Define o número de cartas para a mão. Default para cacheta/pif-paf (9).
    :param jogadores: Número de jogadores para o jogo.
    :param tipo: Tipo de baralho a gerar: 0 para francês, 1 para espanhol (truco).
    :return: lista "jogo" com as mãos dos jogadores seguida da lista "monte" restante no final.
    """
    from random import randint
    if q < 1:
        raise ValueError('O número de baralhos deve ser igual ou maior a um!')
    if jogadores < 2:
        raise ValueError('O número de jogadores deve ser igual ou maior a dois!')
    if num_cartas < 2:
        raise ValueError('O número de cartas deve ser igual ou maior a dois!')
    if tipo > 1:
        raise ValueError('Código de baralho não cadastrado.')

    if tipo == 0:
        monte = cria_baralho_frances(q)
    elif tipo == 1:
        monte = cria_baralho_espanhol(q)  # Inserir 1 para truco.

    mao = list()  # lista de construção das mãos dos jogadores
    jogo = []  # lista que recebe as mãos e o "monte" sem as cartas dos jogadores
    try:
        for jogador in range(0, jogadores):
            for c in range(0, num_cartas):
                carta = randint(0, len(monte)-1)  # Há 52 cartas, sem coringas, em todos os q baralhos
                if (monte[carta] not in mao) or (monte[carta] in mao and mao.count(monte[carta]) < q):
                    mao.append(monte[carta])
                    monte.remove(monte[carta])
            jogo.append(mao[:])
            mao.clear()
        jogo.append(monte[:])
    except IndexError as erro:
        print(repr(erro))
    else:
        return jogo


def compra_carta(mao, monte, descarte):  # Reformar com métodos aninhados e o que for
    """
    De um jogo com vários jogadores e turnos, recebe a lista "mao", com as cartas de um jogador e
    as listas monte e descarte.
    Exibe uma carta aleatória do monte para ser descartada ou substituída por uma das
    cartas na mão.
    Retorna a lista "jogo" contendo as listas atualizadas.
    :param mao: lista de cartas do jogador.
    :param monte: lista do monte.
    :param descarte: lista da pilha de descarte.
    :return: lista contendo como elementos a nova mão, o novo monte e a lista de descarte
    """
    from random import randint
    from gld_script_portfolio.jogos.card_games.interface_cardgames import leiaint, sim_nao, \
        formate, mostra_mao, cabecalho
    from time import sleep as s

    if not descarte:
        indice_carta = randint(0, len(monte) - 1)  # Sorteia um índice respectivo a uma carta do monte.
        carta_monte = exibe_carta(monte[indice_carta])
        formate(f'Compraste a carta {carta_monte} do monte.', destaque='N', cor_letra='BR')
        ficardomonte = sim_nao('Desejas ficar com a carta? [S/N]: ')
        if ficardomonte == 's':
            while True:
                troca = leiaint('Substituí-la por qual das cartas? Responda com a posição: ')
                if 0 <= troca < len(mao):
                    break
                else:
                    continue
            mao.insert(troca, monte[indice_carta])
            monte.remove(monte[indice_carta])
            descarte.append(mao[troca+1])
            mao.pop(troca+1)
            # Finalização:
            jogo_atual = (mao, monte, descarte)
            cabecalho('Sua mão atual é: ', tipoc=3)
            mostra_mao(arruma_mao(mao)[0])
            return jogo_atual
        else:
            formate(f'Carta {monte[indice_carta][0]}{monte[indice_carta][1]} descartada!',
                    destaque='N', cor_letra='VM')
            s(1)
            descarte.append(monte[indice_carta])
            monte.remove(monte[indice_carta])
            # Finalização:
            jogo_atual = (mao, monte, descarte)
            cabecalho('Sua mão atual é: ', tipoc=3)
            mostra_mao(arruma_mao(mao)[0])
            return jogo_atual

    else:
        carta_topo_descarte = exibe_carta(descarte[len(descarte) - 1])
        formate(f'A carta no topo do descarte é {carta_topo_descarte}.',
                destaque='N', cor_letra='BR')
        while True:
            escolhalocal = leiaint('Queres pegá-la ou comprar do monte? [Pegar: 0 | Comprar: 1] ')
            if escolhalocal in (0, 1):
                break
            else:
                continue
        if escolhalocal == 0:
            while True:
                troca = leiaint('Substituí-la por qual das cartas? (Responda com sua posição): ')
                if 0 <= troca < len(mao):
                    break
                else:
                    continue
            mao.insert(troca, descarte[len(descarte)-1])
            descarte.remove(descarte[len(descarte)-1])
            descarte.append(mao[troca + 1])
            mao.pop(troca + 1)
            jogo_atual = (mao, monte, descarte)
            s(1)
            carta_topo_descarte = exibe_carta(descarte[len(descarte) - 1])
            formate(f'Descartaste um {carta_topo_descarte}!',
                    destaque='N', cor_letra='VM')
            cabecalho('Sua mão atual é: ', tipoc=3)
            mostra_mao(arruma_mao(mao)[0])
            return jogo_atual
        else:
            indice_carta = randint(0, len(monte) - 1)
            carta_monte = exibe_carta(monte[indice_carta])
            formate(f'Escolheste comprar uma carta do monte.', destaque='N', cor_letra='BR')
            s(1)
            formate(f'Compraste a carta {carta_monte}.',
                    destaque='N', cor_letra='BR')
            ficardomonte = sim_nao('Desejas ficar com a carta? [S/N] ')
            if ficardomonte == 's':
                while True:
                    troca = leiaint('Substituí-la por qual das cartas? (Responda com sua posição): ')
                    if 0 <= troca < len(mao):
                        break
                    else:
                        continue
                mao.insert(troca, monte[indice_carta])
                monte.remove(monte[indice_carta])
                descarte.append(mao[troca + 1])
                mao.pop(troca + 1)
                jogo_atual = (mao, monte, descarte)
                cabecalho('Sua mão atual é: ', tipoc=3)
                mostra_mao(arruma_mao(mao)[0])
                return jogo_atual
            else:
                formate(f'Carta {carta_monte} descartada!',
                        destaque='N', cor_letra='VM')
                descarte.append(monte[indice_carta])
                monte.remove(monte[indice_carta])
                jogo_atual = (mao, monte, descarte)
                cabecalho('Sua mão atual é: ', tipoc=3)
                mostra_mao(arruma_mao(mao)[0])
                return jogo_atual
