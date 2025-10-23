dicionario = {
    "cor": "ciano",
    "fruta": "framboesa"
}

print(f"dicionario: {dicionario}")

dicionario["nome"] = "Juan"
print(f"dicionario: {dicionario}")
print(f"dicionario[cor]: {dicionario["cor"]}")

del dicionario["nome"]
print(f"dicionario: {dicionario}")
