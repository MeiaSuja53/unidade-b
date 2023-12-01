class Animal:
    def __init__(self, nome, especie, idade, dieta, habitat):
        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.dieta = dieta
        self.habitat = habitat

    def descricao(self):
        return f"{self.nome} é um {self.especie} de {self.idade} anos que é {self.dieta} e vive no habitat {self.habitat}."

class Zoologico:
    def __init__(self):
        self.animais = []

    def adicionar_animal(self, animal):
        self.animais.append(animal)

    def remover_animal(self, nome):
        for animal in self.animais:
            if animal.nome == nome:
                self.animais.remove(animal)

    def listar_animais(self):
        for animal in self.animais:
            print(animal.descricao())

    # Desafio
    def buscar_por_especie(self, especie):
        resultado = []
        for animal in self.animais:
            if animal.especie == especie:
                resultado.append(animal)
        return resultado

    def listar_por_habitat(self, habitat):
        for animal in self.animais:
            if animal.habitat == habitat:
                print(animal.descricao())
def main():
    zoologico = Zoologico()

    while True:
        print("\nOpções:")
        print("1. Adicionar Animal")
        print("2. Remover Animal")
        print("3. Listar Animais")
        print("4. Buscar por Espécie")
        print("5. Listar por Habitat")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do animal: ")
            especie = input("Digite a espécie do animal: ")
            idade = input("Digite a idade do animal: ")
            dieta = input("Digite a dieta do animal: ")
            habitat = input("Digite o habitat do animal: ")
            animal = Animal(nome, especie, idade, dieta, habitat)
            zoologico.adicionar_animal(animal)
            print("Animal adicionado com sucesso!")

        elif opcao == "2":
            nome = input("Digite o nome do animal a ser removido: ")
            zoologico.remover_animal(nome)
            print("Animal removido com sucesso!")

        elif opcao == "3":
            zoologico.listar_animais()

        elif opcao == "4":
            especie = input("Digite a espécie a ser buscada: ")
            animais_encontrados = zoologico.buscar_por_especie(especie)
            if animais_encontrados:
                print(f"Animais da espécie {especie}:")
                for animal in animais_encontrados:
                    print(animal.descricao())
            else:
                print(f"Nenhum animal da espécie {especie} encontrado.")

        elif opcao == "5":
            habitat = input("Digite o habitat a ser listado: ")
            zoologico.listar_por_habitat(habitat)

        elif opcao == "6":
            break

        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()