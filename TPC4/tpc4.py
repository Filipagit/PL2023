import os
import re
import csv
import json

def csv_to_json(csv_file):
    # Abre o arquivo CSV
    with open(csv_file, 'r', newline='', encoding='utf-8') as f:
        # Lê o arquivo CSV com o módulo csv
        reader = csv.reader(f)
        # Extrai o cabeçalho do CSV
        header = next(reader)

        # Cria um dicionário para armazenar o resultado
        result = {}

        # Itera pelas linhas do CSV
        for row in reader:
            # Inicializa um objeto vazio para a linha
            data = {}

            # Itera pelos campos da linha
            for i, field in enumerate(row):
                # Verifica se o campo é uma lista
                match = re.match(r'^(.+){(\d+)(,\s*(\d+))?}$', header[i])
                if match:
                    field_name, start, end = match.group(1, 2, 4)
                    if end:
                        end = int(end)
                    else:
                        end = int(start)
                    # Cria uma lista com os valores da lista
                    values = [x for x in row[i:i+end] if x]
                    # Aplica a função de agregação, se houver
                    agg_function = re.search(r'::(\w+)$', header[i])
                    if agg_function:
                        function_name = agg_function.group(1)
                        if function_name == 'sum':
                            value = sum(map(float, values))
                        elif function_name == 'media':
                            value = sum(map(float, values)) / len(values)
                    else:
                        value = values
                    data[field_name] = value
                else:
                    data[header[i]] = field

            # Adiciona a linha ao resultado
            result[row[0]] = data

        # Retorna o resultado como JSON
        return json.dumps(result, indent=4, ensure_ascii=False)

def main():
    # Solicita o nome do arquivo CSV ao usuário
    csv_file_name = input("Por favor, insira o nome do arquivo CSV: ")
    # Concatena o caminho da diretoria com o nome do arquivo CSV
    csv_file = os.path.join('/home/filipa/Desktop/PL2023/TPC4/ficheiros_csv', csv_file_name)

    # Define o nome do arquivo JSON de saída
    json_file = os.path.splitext(csv_file_name)[0] + ".json"

    # Converte o arquivo CSV em JSON
    result = csv_to_json(csv_file)

    # Grava o resultado no arquivo JSON de saída
    with open(json_file, 'w', encoding='utf-8') as f:
        f.write(result)

    # Imprime uma mensagem informando que a conversão foi concluída com sucesso
    print(f'O arquivo "{csv_file}" foi convertido em "{json_file}" com sucesso!')

if __name__ == '__main__':
    main()
