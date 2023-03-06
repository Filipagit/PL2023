import re

# a) calcular a frequência de processos por ano

frequencias = {}

with open('processos.txt', 'r') as f:
    for linha in f:
        match = re.search(r'^\d+::(\d{4})-', linha)
        if match:
            ano = match.group(1)
            if ano in frequencias:
                frequencias[ano] += 1
            else:
                frequencias[ano] = 1

for ano, frequencia in frequencias.items():
    print(f'Ano {ano}: {frequencia} processos')

   