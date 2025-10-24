def define_posicoes(linha, coluna, orientacao, tamanho):
    if orientacao == 'horizontal':
        return [[linha, coluna + i] for i in range(tamanho)]
    elif orientacao == 'vertical':
        return [[linha + i, coluna] for i in range(tamanho)]
    
def preenche_frota(frota,nome_navio,linha_navio,coluna_navio,orientacao,tamanho):
    posic=define_posicoes
    for nome_navio,posic in frota.items():
        frota[nome_navio]=posic