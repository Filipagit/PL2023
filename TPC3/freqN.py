import re

# Expressões regulares para extrair informações do arquivo
ano_regex = re.compile(r'^(\d{4})')
nome_regex = re.compile(r'(\b[A-Z][a-z]*\b)')

# Dicionário para armazenar as frequências por século
frequencias_por_seculo = {}

# Abrir o arquivo e ler as linhas
with open('processos.txt', 'r', encoding='utf-8') as f:
    for linha in f:
        # Extrair o ano da linha
        ano_match = ano_regex.search(linha)
        if ano_match:
            ano = int(ano_match.group(1))
            seculo = (ano - 1) // 100 + 1

            # Extrair o nome e o apelido da linha
            nome_match = nome_regex.findall(linha)
            nome = nome_match[0]
            apelido = nome_match[-1]

            # Adicionar ao dicionário de frequências do século
            if seculo not in frequencias_por_seculo:
                frequencias_por_seculo[seculo] = {'nomes': {}, 'apelidos': {}}
            frequencias_por_seculo[seculo]['nomes'][nome] = frequencias_por_seculo[seculo]['nomes'].get(nome, 0) + 1
            frequencias_por_seculo[seculo]['apelidos'][apelido] = frequencias_por_seculo[seculo]['apelidos'].get(apelido, 0) + 1

# Imprimir as 5 maiores frequências por século para nomes e apelidos
for seculo, frequencias in frequencias_por_seculo.items():
    nomes_ordenados = sorted(frequencias['nomes'].items(), key=lambda x: x[1], reverse=True)[:5]
    apelidos_ordenados = sorted(frequencias['apelidos'].items(), key=lambda x: x[1], reverse=True)[:5]

    print(f'Século {seculo}:')
    print('Nomes:')
    for nome, freq in nomes_ordenados:
        print(f'  {nome}: {freq}')
    print('Apelidos:')
    for apelido, freq in apelidos_ordenados:
        print(f'  {apelido}: {freq}')
    print()
