def define_posicoes(linha, coluna, orientacao, tamanho):
    if orientacao == 'horizontal':
        return [[linha, coluna + i] for i in range(tamanho)]
    elif orientacao == 'vertical':
        return [[linha + i, coluna] for i in range(tamanho)]