
class Pessoa:
    def __init__(self, idade, sexo, tensao, colesterol, batimento, tem_doenca):
        self.idade = idade
        self.sexo = sexo
        self.tensao = tensao
        self.colesterol = colesterol
        self.batimento = batimento
        self.tem_doenca = tem_doenca

class Distribuicao:
    def __init__(self):
        self.total_pessoas = 0
        self.total_homem = 0
        self.total_mulher = 0
        self.total_doenca = 0
        self.total_homem_doenca = 0
        self.total_mulher_doenca = 0
        self.doenca_por_faixa_etaria = {}
        self.doenca_por_colesterol = {}

    def add_pessoa(self, pessoa):
        self.total_pessoas += 1

        if pessoa.sexo == 'M':
            self.total_homem += 1
        else:
            self.total_mulher += 1

        if pessoa.tem_doenca:
            self.total_doenca += 1

            if pessoa.sexo == 'M':
                self.total_homem_doenca += 1
            else:
                self.total_mulher_doenca += 1

            # Atualiza distribuição por faixa etária
            faixa_etaria = self.get_faixa_etaria(pessoa.idade)
            if faixa_etaria not in self.doenca_por_faixa_etaria:
                self.doenca_por_faixa_etaria[faixa_etaria] = [0, 0]
            if pessoa.sexo == 'M':
                self.doenca_por_faixa_etaria[faixa_etaria][0] += 1
            else:
                self.doenca_por_faixa_etaria[faixa_etaria][1] += 1

            # Atualiza distribuição por colesterol
            nivel_colesterol = self.get_nivel_colesterol(pessoa.colesterol)
            if nivel_colesterol not in self.doenca_por_colesterol:
                self.doenca_por_colesterol[nivel_colesterol] = [0, 0]
            if pessoa.sexo == 'M':
                self.doenca_por_colesterol[nivel_colesterol][0] += 1
            else:
                self.doenca_por_colesterol[nivel_colesterol][1] += 1

    def get_faixa_etaria(self, idade):
        faixa = (idade - 30) // 5
        return f'{30 + faixa * 5}-{34 + faixa * 5}'

    def get_nivel_colesterol(self, colesterol):
        nivel = colesterol // 10
        return f'{nivel * 10}-{(nivel + 1) * 10 - 1}'

    def imprime_distribuicao(self, distribuicao, titulo):
        print(titulo)
        print('Faixa\tTotal\tHomens\tMulheres')
        for faixa, contagem in distribuicao.items():
            total = contagem[0] + contagem[1]
            print(f'{faixa}\t{total}\t{contagem[0]}\t{contagem[1]}')
        print()
    def distribuicao_por_sexo(self):
        return {'Homens': [self.total_homem, self.total_homem_doenca],
                'Mulheres': [self.total_mulher, self.total_mulher_doenca]}

    def distribuicao_por_faixa_etaria(self):
        return self.imprime_distribuicao(self.doenca_por_faixa_etaria, 'Distribuição da Doença por Faixa Etária')

    def distribuicao_por_colesterol(self):
        return self.imprime_distribuicao(self.doenca_por_colesterol, 'Distribuição da Doença por Níveis de Colesterol')

def le_arquivo_csv(myheart):
    distribuicao = Distribuicao()

    with open(myheart) as f:
        linhas = f.readlines()

    for linha in linhas[1:]:
        campos = linha.strip().split(',')
        idade = int(campos[0])
        sexo = campos[1]
        tensao = int(campos[2])
        colesterol = int(campos[3])
        batimento = int(campos[4])
        tem_doenca = int(campos[5])

        pessoa = Pessoa(idade, sexo, tensao, colesterol, batimento, tem_doenca)
        distribuicao.add_pessoa(pessoa)

    return distribuicao

if __name__ == '__main__':
    arquivo_csv = 'myheart.csv'
    distribuicao = le_arquivo_csv(arquivo_csv)

    # Imprime as distribuições
    print(f'Total de Pessoas: {distribuicao.total_pessoas}')
    print(f'Total de Pessoas do Sexo Masculino: {distribuicao.total_homem}')
    print(f'Total de Pessoas do Sexo Feminino: {distribuicao.total_mulher}')
    print(f'Total de Pessoas com Doença: {distribuicao.total_doenca}')
    print(f'Total de Homens com Doença: {distribuicao.total_homem_doenca}')
    print(f'Total de Mulheres com Doença: {distribuicao.total_mulher_doenca}')
    print()

    distribuicao.imprime_distribuicao(distribuicao.distribuicao_por_sexo(),
                                      'Distribuição da Doença por Sexo')

    distribuicao.distribuicao_por_faixa_etaria()

    distribuicao.distribuicao_por_colesterol()


