class Restaurante:
    def __init__(self):
        self.itens_menu = {"hamburger": 5.50, "batata frita": 2.00, "refrigerante": 1.50, "pizza": 10.00, "salada": 7.00}
        self.pedidos = {}

    def adicionar_pedido(self, numero_pedido):
        self.pedidos[numero_pedido] = {}

    def adicionar_item(self, numero_pedido, item, quantidade):
        if item in self.itens_menu:
            if numero_pedido in self.pedidos:
                if item in self.pedidos[numero_pedido]:
                    self.pedidos[numero_pedido][item] += quantidade
                else:
                    self.pedidos[numero_pedido][item] = quantidade

    def calcular_total_pedido(self, numero_pedido):
        total = 0
        if numero_pedido in self.pedidos:
            for item, quantidade in self.pedidos[numero_pedido].items():
                total += self.itens_menu[item] * quantidade
        return total

    # Desafio
    def remover_item(self, numero_pedido, item):
        if numero_pedido in self.pedidos and item in self.pedidos[numero_pedido]:
            del self.pedidos[numero_pedido][item]

    def alterar_quantidade(self, numero_pedido, item, quantidade):
        if numero_pedido in self.pedidos and item in self.pedidos[numero_pedido]:
            self.pedidos[numero_pedido][item] = quantidade

    def visualizar_pedidos(self):
        for numero_pedido, itens in self.pedidos.items():
            print(f"Pedido {numero_pedido}:")
            for item, quantidade in itens.items():
                print(f"{item}: {quantidade}")
            print(f"Total: {self.calcular_total_pedido(numero_pedido)}")


def main():
    restaurante = Restaurante()

    while True:
        print("\nOpções:")
        print("1. Adicionar Pedido")
        print("2. Adicionar Item")
        print("3. Calcular Total do Pedido")
        print("4. Remover Item")
        print("5. Alterar Quantidade")
        print("6. Visualizar Pedidos")
        print("7. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            numero_pedido = input("Digite o número do pedido: ")
            restaurante.adicionar_pedido(numero_pedido)

        elif opcao == "2":
            numero_pedido = input("Digite o número do pedido: ")
            item = input("Digite o nome do item: ")
            quantidade = int(input("Digite a quantidade: "))
            restaurante.adicionar_item(numero_pedido, item, quantidade)

        elif opcao == "3":
            numero_pedido = input("Digite o número do pedido: ")
            total = restaurante.calcular_total_pedido(numero_pedido)
            print(f"Total do Pedido {numero_pedido}: {total:.2f}")

        elif opcao == "4":
            numero_pedido = input("informe o número do pedido: ")
            item = input("informe o nome do item a ser removido: ")
            restaurante.remover_item(numero_pedido, item)

        elif opcao == "5":
            numero_pedido = input("informe o número do pedido: ")
            item = input("informe o nome do item a ser alterado: ")
            quantidade = int(input("informe a nova quantidade: "))
            restaurante.alterar_quantidade(numero_pedido, item, quantidade)

        elif opcao == "6":
            restaurante.visualizar_pedidos()

        elif opcao == "7":
            break

        else:
            print("Opção inválida! Tente outra vez (:")


if __name__ == "__main__":
    main()