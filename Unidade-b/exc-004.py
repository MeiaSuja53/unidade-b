class Jogo:
    def __init__(self, nome, categoria, taxa_entrada, id):
        self.nome = nome
        self.categoria = categoria
        self.taxa_entrada = taxa_entrada
        self.id = id

    def __str__(self):
        return f"Nome: {self.nome}, Categoria: {self.categoria}, Taxa de Entrada: {self.taxa_entrada}, ID: {self.id}"

class Plataforma:
    def __init__(self):
        self.jogos = []

    def adicionar_jogo(self, jogo):
        self.jogos.append(jogo)

    def remover_jogo(self, id):
        for jogo in self.jogos:
            if jogo.id == id:
                self.jogos.remove(jogo)

    def listar_jogos(self):
        for jogo in self.jogos:
            print(jogo)

    # Desafio
    def __str__(self):
        return f"Esta plataforma tem {len(self.jogos)} jogos."

    def buscar_por_categoria(self, categoria):
        resultado = []
        for jogo in self.jogos:
            if jogo.categoria == categoria:
                resultado.append(jogo)
        return resultado

def main():
    plataforma = Plataforma()

    while True:
        print("\nOpções:")
        print("1. Adicionar Jogo")
        print("2. Remover Jogo")
        print("3. Listar Jogos")
        print("4. Buscar por Categoria")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do jogo: ")
            categoria = input("Digite a categoria do jogo: ")
            taxa_entrada = float(input("Digite a taxa de entrada do jogo: "))
            id = int(input("Digite o ID do jogo: "))
            jogo = Jogo(nome, categoria, taxa_entrada, id)
            plataforma.adicionar_jogo(jogo)
            print("Jogo adicionado com sucesso!")

        elif opcao == "2":
            id = int(input("Digite o ID do jogo a ser removido: "))
            plataforma.remover_jogo(id)
            print("Jogo removido com sucesso!")

        elif opcao == "3":
            plataforma.listar_jogos()

        elif opcao == "4":
            categoria = input("Digite a categoria a ser buscada: ")
            jogos_encontrados = plataforma.buscar_por_categoria(categoria)
            if jogos_encontrados:
                print(f"Jogos da categoria {categoria}:")
                for jogo in jogos_encontrados:
                    print(jogo)
            else:
                print(f"Nenhum jogo da categoria {categoria} encontrado.")

        elif opcao == "5":
            break

        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()