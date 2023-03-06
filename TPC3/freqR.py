import re

# Dicionário para armazenar a frequência de cada tipo de relação
relacoes = {}

with open("processos.txt", encoding="utf8") as f:
    for linha in f:
        # Extrai as relações da linha atual
        relacoes_str = re.search(r'([A-Za-z]+\.[ A-Za-z]+\.)', linha)
        if relacoes_str:
            relacoes_lst = [r.strip() for r in relacoes_str.group(1).split(",")]

            # Atualiza o dicionário de frequências com as novas relações encontradas
            for r in relacoes_lst:
                if r in relacoes:
                    relacoes[r] += 1
                else:
                    relacoes[r] = 1

# Imprime as frequências de cada tipo de relação
print("Frequência de tipos de relação:")
for rel, freq in relacoes.items():
    print(f"{rel}: {freq}")
