import re

class PhoneStateMachine:
    def __init__(self):
        self.state = "IDLE"
        self.coins = []
        self.balance = 0
        self.call_cost = 0
        self.call_type = None
        self.phone_number = None

    def start(self):
        self.state = "IDLE"
        self.coins = []
        self.balance = 0
        self.call_cost = 0
        self.call_type = None
        self.phone_number = None
        return "Introduza moedas."

    def coin_insert(self, values):
        valid_coins = ["5c", "10c", "20c", "50c", "1e", "2e"]
        for value in values:
            if value not in valid_coins:
                return f"{value} - moeda inválida; saldo = {self.format_balance()}"
            self.coins.append(value)
            self.balance += self.value_to_cents(value)
        return f"saldo = {self.format_balance()}"

    def dial(self, number):
        if not re.match(r"^00\d{9}$|^0?\d{9}$", number):
            return "Número inválido. Queira discar novo número!"
        if number.startswith("601") or number.startswith("641"):
            return "Esse número não é permitido neste telefone. Queira discar novo número!"
        if number.startswith("00"):
            if self.balance < 150:
                return f"Saldo insuficiente para realizar chamada internacional (custo: 1.5€). Saldo atual: {self.format_balance()}"
            self.call_cost = 150
            self.call_type = "international"
        elif number.startswith("2"):
            if self.balance < 25:
                return f"Saldo insuficiente para realizar chamada nacional (custo: 25c). Saldo atual: {self.format_balance()}"
            self.call_cost = 25
            self.call_type = "national"
        elif number.startswith("800"):
            self.call_cost = 0
            self.call_type = "green"
        elif number.startswith("808"):
            self.call_cost = 10
            self.call_type = "blue"
        self.phone_number = number
        return f"Chamada em curso para {number}. Custo: {self.format_cost(self.call_cost)}"

    def end_call(self):
        if self.call_cost > 0:
            self.balance -= self.call_cost
            return f"Chamada terminada. Saldo atual: {self.format_balance()}"
        return "Chamada terminada. Saldo não foi afetado."

    def abort(self):
        if not self.coins:
            return "Não tem moedas para devolver."
        return f"troco = {self.format_balance()}. Volte sempre!"

    def format_balance(self):
        euros = self.balance // 100
        cents = self.balance % 100
        return f"{euros}e{cents:02d}c"

    def format_cost(self, cost):
        euros = cost // 100
        cents = cost % 100
        return f"{euros}e{cents:02d}c"

    def value_to_cents(self, value):
        if value.endswith("c"):
            return int(value[:-1])
        elif value.endswith("e"):
            return int(value[:-1]) * 100
        else:
            return 0

saldo = 0  # saldo inicial da máquina

# define a função que trata cada comando recebido
def handle_command(command):
    global saldo
    if command == "LEVANTAR":
        print("maq: Introduza moedas.")
    elif command.startswith("MOEDA "):
        valores = re.findall(r'\d+|\d+\.\d+', command)  # extrai os valores da lista de moedas
        for valor in valores:
            valor_float = float(valor)
            if valor_float not in [0.05, 0.10, 0.20, 0.50, 1.0, 2.0]:
                print(f"maq: {valor}c - moeda inválida; saldo = {saldo:.2f}")
                return
            else:
                saldo += valor_float
        print(f"maq: saldo = {saldo:.2f}")
    elif command.startswith("T="):
        numero = command[2:]
        if numero.startswith("601") or numero.startswith("641"):
            print("maq: Esse número não é permitido neste telefone. Queira discar novo número!")
        elif numero.startswith("00"):
            if saldo >= 1.5:
                saldo -= 1.5
                print(f"maq: chamada internacional para {numero}; saldo = {saldo:.2f}")
            else:
                print("maq: Saldo insuficiente para chamada internacional.")
        elif numero.startswith("2"):
            if saldo >= 0.25:
                saldo -= 0.25
                print(f"maq: chamada nacional para {numero}; saldo = {saldo:.2f}")
            else:
                print("maq: Saldo insuficiente para chamada nacional.")
        elif numero.startswith("800"):
            print(f"maq: chamada verde para {numero}; saldo = {saldo:.2f}")
        elif numero.startswith("808"):
            if saldo >= 0.10:
                saldo -= 0.10
                print(f"maq: chamada azul para {numero}; saldo = {saldo:.2f}")
            else:
                print("maq: Saldo insuficiente para chamada azul.")
        else:
            print("maq: Número inválido.")
    elif command == "ABORTAR":
        print(f"maq: Troco = {saldo:.2f}. Volte sempre!")
        saldo = 0
    elif command == "POUSAR":
        print(f"maq: Troco = {saldo:.2f}. Volte sempre!")
        saldo = 0
    else:
        print("maq: Comando inválido.")

# loop principal do programa
while True:
    comando = input("Comando: ")
    handle_command(comando)