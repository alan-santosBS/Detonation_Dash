from models.array_classico import ArrayClassico

# Cria um array de 5 posições, tudo 0
arr = ArrayClassico(5, 0)

print("Tamanho:", arr.tamanho)
print("Array:", arr)

# Define valores
arr.definir(0, 10)
arr.definir(2, 30)
arr.definir(4, 50)
print("Depois de definir:", arr)

# Lê valores
print("arr.obter(0) =", arr.obter(0))
print("arr.obter(2) =", arr.obter(2))

# Testa erro de índice
try:
    arr.obter(99)
except IndexError as e:
    print("Erro esperado:", e)

# Testa preencher
arr.preencher(7)
print("Depois de preencher com 7:", arr)
