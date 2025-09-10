#  _ __ ___  ___ _   _ _ __ ___   ___   _ __  _   _
# | '__/ _ \/ __| | | | '_ ` _ \ / _ \ | '_ \| | | |
# | | |  __/\__ \ |_| | | | | | | (_) || |_) | |_| |
# |_|  \___||___/\__,_|_| |_| |_|\___(_) .__/ \__, |
#                                      |_|    |___/

texto = "  Python é incrível!  "

# funções básicas
len(texto)          # retorna o tamanho da string
str(123)            # converte número em string
ord("A")            # retorna o código ASCII do caractere
chr(65)             # retorna o caractere do código ASCII
# 0-9 (48-57)
# A-Z (65-90)
# a-z (97-122)

# transformações
texto.upper()       # converte para maiúsculas -> '  PYTHON É INCRÍVEL!  '
texto.lower()       # converte para minúsculas -> '  python é incrível!  '
texto.title()       # primeira letra de cada palavra maiúscula -> '  Python É Incrível!  '
texto.capitalize()  # primeira letra da string maiúscula -> '  python é incrível!  '
texto.strip()       # remove espaços no início e no fim -> 'Python é incrível!'
texto.lstrip()      # remove espaços à esquerda
texto.rstrip()      # remove espaços à direita
texto.replace("Python", "Java")  # substitui substrings -> '  Java é incrível!  '

# pesquisa e verificação
"Python" in texto       # verifica se substring existe -> True/False
texto.find("Python")    # retorna o índice da primeira ocorrência ou -1
texto.rfind("Python")   # última ocorrência
texto.index("Python")   # igual a find(), mas dá erro se não encontrar
texto.count("o")        # conta quantas vezes o caractere ou substring aparece
texto.startswith("Py")  # verifica se começa com substring -> True/False
texto.endswith("!")     # verifica se termina com substring -> True/False

# split e join
texto.split()                       # divide em lista de palavras -> ['Python', 'é', 'incrível!']
texto.split(",")                    # divide usando outro separador
"-".join(["Python", "é", "top"])    # junta elementos de lista com separador -> 'Python-é-top'

# tipos de caracteres
texto.isalpha()      # True se só tiver letras
texto.isdigit()      # True se só tiver números
texto.isalnum()      # True se letras ou números
texto.isspace()      # True se só tiver espaços
texto.islower()      # True se todas minúsculas
texto.isupper()      # True SE TODAS MAIÚSCULAS
texto.istitle()      # True Se Todas Palavras Estão Capitalizadas

# substrings e slicing
texto[0]          # primeiro caractere
texto[-1]         # último caractere
texto[0:6]        # fatiamento -> '  Pytho'
texto[::2]        # pula caracteres -> ' Pto ínce!'
