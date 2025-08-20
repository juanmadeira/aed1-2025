# anagrama("amor", "roma") => True
# anagrama("joao", "batata") => False

def anagrama(term1, term2):
    term1 = sorted(list(term1))
    term2 = sorted(list(term2))
    if term1 == term2:
        return True
    else:
        return False


term1 = input("Insira o primeiro termo: ")
term2 = input("Insira o segundo termo: ")
print(anagrama(term1, term2))
