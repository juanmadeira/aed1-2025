# faça um sistema de votação. o programa deve:
# pedir votos (número do candidato) em loop até digitar "fim"
# mostrar o candidato vencedor (ou empate) ao final

def voting(votes):
    candidates = list(set(votes))
    result = {}
    for i in range(len(candidates)):
        result.update({candidates[i]: votes.count(candidates[i])})

    winnerVotes = max(result.values())
    winner = [key for key, value in result.items() if value == winnerVotes]

    if len(winner) > 1:
        winners = ""
        for i in range(len(winner)):
            winners += winner[i] + ", "
        return f"\nHouve um empate! Os vencedores foram os candidatos de números {winners[:-2]} com {winnerVotes} votos."

    return f"\nO candidato vencedor foi o de número {winner[0]} com {winnerVotes} votos."


votes = []
while True:
    votes.append(input("Insira o número do candidato desejado (digite \"fim\" para encerrar): "))
    if votes[-1] == "fim":
        votes.pop(-1)
        break

print(voting(votes))
