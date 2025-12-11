# Crie um programa em Python para acompanhar a pontuação de jogadores em um jogo de
# tabuleiro simples. Primeiro crie um dicionário chamado pontuacao para armazenar as pontuações
# dos jogadores. Use os nomes dos jogadores como chaves e as pontuações iniciais como valores
# associados. Permita que o usuário atualize a pontuação dos jogadores durante o jogo. Solicite ao
# usuário o nome do jogador e a quantidade de pontos a serem adicionados à pontuação atual
# desse jogador. Ao final do jogo (ou a qualquer momento desejado), imprima um relatório
# mostrando o nome de cada jogador e sua pontuação final. Para testar, inicialize o dicionário de
# pontuação com alguns jogadores e pontuações iniciais. Permita que o usuário atualize a
# pontuação dos jogadores durante o jogo. No fim, imprima na tela o relatório de pontuação ao final
# do jogo.

pontuacao = {
    "João": 10,
    "Maria": 15,
    "José": 8
}

print("Pontuações iniciais:")
for jogador, pontos in pontuacao.items():
    print(f"{jogador}: {pontos}")

while True:
    print("\nAtualizar pontuação do jogador (ou digite 'sair' para encerrar):")
    nome = input("Nome do jogador: ").strip()
    
    if nome.lower() == "sair":
        break
    
    if nome not in pontuacao:
        print("Jogador não encontrado. Tente novamente.")
        continue
    
    try:
        pontos_adicionar = int(input("Quantidade de pontos a adicionar: "))
    except ValueError:
        print("Por favor, digite um número inteiro válido.")
        continue

    pontuacao[nome] += pontos_adicionar
    print(f"Pontuação atualizada: {nome} = {pontuacao[nome]}")

print("\nRelatório final de pontuação:")
for jogador, pontos in pontuacao.items():
    print(f"{jogador}: {pontos}")