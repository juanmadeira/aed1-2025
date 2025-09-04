# Escreva um programa que peça a senha para o usuário. Ele só pode seguir se digitar a senha correta.
# Ele pode tentar até 10 vezes
# A senha é AED1_2025

senhaCorreta = "AED1_2025"
senha = ""
acesso = False
tentativas = 0

while(senha != senhaCorreta and tentativas < 10):
    senha = input("Insira a senha: ")
    if(senha == senhaCorreta):
        acesso = True
    else:
        acesso = False
    tentativas += 1

if (acesso):
    print("Sistema acessado!")
else:
    print("Acabaram as tentativas. Acesso negado.")
