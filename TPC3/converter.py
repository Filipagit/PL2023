import json

# Lista para armazenar os registros a serem convertidos em JSON
registros_json = []

with open("processos.txt", encoding="utf8") as f:
    # Lê as primeiras 20 linhas do arquivo
    for i in range(20):
        linha = f.readline().strip()

        # Extrai os campos da linha
        campos = linha.split("::")
        num_processo = campos[0]
        data = campos[1]
        nome_completo = campos[2]
        relacoes = campos[3]

        # Cria um dicionário com as informações do registro
        registro = {
            "num_processo": num_processo,
            "data": data,
            "nome_completo": nome_completo,
            "relacoes": relacoes
        }

        # Adiciona o dicionário à lista de registros a serem convertidos em JSON
        registros_json.append(registro)

# Converte a lista de registros para JSON
registros_json = json.dumps(registros_json, ensure_ascii=False, indent=4)

# Salva o JSON em um novo arquivo
with open("processos.json", "w", encoding="utf8") as f:
    f.write(registros_json)

print("Arquivo processos.json criado com sucesso!")
