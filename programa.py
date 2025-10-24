from funcoes import posicao_valida
from funcoes import preenche_frota

frota = {
    "porta-avioes": [],
    "navio-tanque": [],
    "contratorpedeiro": [],
    "submarino": []
}
navios_info = {
    "porta-avioes": {"quantidade": 1, "tamanho": 4},
    "navio-tanque": {"quantidade": 2, "tamanho": 3},
    "contratorpedeiro": {"quantidade": 3, "tamanho": 2},
    "submarino": {"quantidade": 4, "tamanho": 1}
}

for nome_navio, info in navios_info.items():
    for i in range(info["quantidade"]):
        valido = False
        while not valido:
            print(f"Insira as informacoes referentes ao navio {nome_navio} que possui tamanho {info['tamanho']}")
            linha = int(input("Linha: "))
            coluna = int(input("Coluna: "))

            if nome_navio != "submarino":
                orient_input = int(input("[1] Vertical [2] Horizontal >"))
                orientacao = "vertical" if orient_input == 1 else "horizontal"
            else:
                orientacao = "horizontal"

            if posicao_valida(frota, linha, coluna, orientacao, info["tamanho"]):
                preenche_frota(frota, nome_navio, linha, coluna, orientacao, info["tamanho"])
                valido = True
            else:
                print("Esta posicao nao esta valida!")

print(frota)
