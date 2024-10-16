# Definindo a lista de filmes com suas classificações indicativas e salas
filmes = [
    {"nome": "Filme A", "classificacao": 18, "sala": 1},
    {"nome": "Filme B", "classificacao": 16, "sala": 2},
    {"nome": "Filme C", "classificacao": 12, "sala": 3},
    {"nome": "Filme D", "classificacao": 10, "sala": 4}
]

# Solicitando o nome e a idade do usuário
nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))

# Função para exibir a lista de filmes
def exibir_filmes():
    print("\nLista de filmes disponíveis:")
    for i, filme in enumerate(filmes):
        print(f"{i + 1}. {filme['nome']} - Sala {filme['sala']} - Classificação: {filme['classificacao']}+")

# Loop para verificar a escolha do filme e a idade do usuário
while True:
    exibir_filmes()
    escolha = int(input("\nEscolha o número do filme que deseja assistir: ")) - 1

    if escolha < 0 or escolha >= len(filmes):
        print("Opção inválida! Tente novamente.")
        continue

    filme_escolhido = filmes[escolha]
    if idade >= filme_escolhido["classificacao"]:
        print(f"\n{nome}, você pode assistir ao filme '{filme_escolhido['nome']}' na sala {filme_escolhido['sala']}. Aproveite!")
        break
    else:
        print(f"\nDesculpe, {nome}, mas você não tem idade suficiente para assistir ao filme '{filme_escolhido['nome']}'.")
