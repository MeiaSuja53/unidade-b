class Cliente:
    def __init__(self, nome, prioridade):
        self.nome = nome
        self.prioridade = prioridade

    def __str__(self):
        return self.nome

class FilaBanco:
    def __init__(self):
        self.fila = []

    def adicionar_cliente(self, nome, prioridade):
        if prioridade:
            cliente = Cliente(nome, True)
            self.fila.insert(0, cliente)
        else:
            cliente = Cliente(nome, False)
            self.fila.append(cliente)
        print(f"{cliente.nome} foi adicionado à fila.")

    def atender_proximo_cliente(self):
        if self.fila:
            proximo_cliente = self.fila.pop(0)
            print(f"{proximo_cliente} está sendo atendido.")
        else:
            print("A fila está vazia.")

    def visualizar_fila(self):
        print("Fila:")
        for cliente in self.fila:
            print(cliente)
        if not self.fila:
            print("A fila está vazia.")

    def executar(self):
        while True:
            print("Bem-vindo ao banco!")
            print("1. Adicionar cliente à fila")
            print("2. Atender próximo cliente")
            print("3. Visualizar fila")
            print("4. Sair")

            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                nome = input("Nome do cliente: ")
                prioridade = input("O cliente tem prioridade por lei? (S/N): ")
                self.adicionar_cliente(nome, prioridade.upper() == "S")

            elif escolha == "2":
                self.atender_proximo_cliente()

            elif escolha == "3":
                self.visualizar_fila()

            elif escolha == "4":
                break

            else:
                print("Opção inválida. Tente novamente.")

        print("O programa foi encerrado.")

if __name__ == "__main__":
    fila_banco = FilaBanco()
    fila_banco.executar()