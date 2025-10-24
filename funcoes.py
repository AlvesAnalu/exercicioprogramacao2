def define_posicoes(linha, coluna, orientacao, tamanho):
    if orientacao == 'horizontal':
        return [[linha, coluna + i] for i in range(tamanho)]
    elif orientacao == 'vertical':
        return [[linha + i, coluna] for i in range(tamanho)]
    
def preenche_frota(frota,nome_navio, linha, coluna, orientacao, tamanho):
    posic=define_posicoes(linha, coluna, orientacao, tamanho)
    if nome_navio not in frota:
        frota[nome_navio]=posic
    else:
        frota[nome_navio].append(posic)

    return frota