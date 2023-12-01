class Carro:
    def __init__(self, marca, modelo, ano, preco):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.preco = preco
        self.vendido = False

    def exibir_informacoes(self):
        status_venda = "Vendido" if self.vendido else "Disponível"
        print(f"Marca: {self.marca}\nModelo: {self.modelo}\nAno: {self.ano}\nPreço: R${self.preco:.2f}\nStatus: {status_venda}\n")

    def vender(self):
        if not self.vendido:
            self.vendido = True
            print("Carro vendido com sucesso!")
        else:
            print("Este carro já foi vendido.")

    def ajustar_preco(self, novo_preco):
        if not self.vendido:
            self.preco = novo_preco
            print(f"Preço do carro ajustado para R${self.preco:.2f}")
        else:
            print("Não é possível ajustar o preço de um carro vendido.")

# Exemplo de uso da classe Carro
carro1 = Carro("Toyota", "Corolla", 2022, 75000.00)
carro2 = Carro("Ford", "Mustang", 2021, 120000.00)

# Exibindo informações dos carros
print("Informações do Carro 1:")
carro1.exibir_informacoes()

print("Informações do Carro 2:")
carro2.exibir_informacoes()

# Vendendo o Carro 1
carro1.vender()

# Tentando vender o Carro 1 novamente (não deve ser possível)
carro1.vender()

# Ajustando o preço do Carro 2
carro2.ajustar_preco(110000.00)

# Exibindo informações atualizadas do Carro 2
print("Informações atualizadas do Carro 2:")
carro2.exibir_informacoes()