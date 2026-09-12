from models.matriz_classica import MatrizClassica

# Cria uma matriz 3x4 preenchida com 0
mat = MatrizClassica(3, 4, 0)

print("Linhas:", mat.linhas)
print("Colunas:", mat.colunas)
print("Matriz inicial:")
print(mat)

# Define alguns valores
mat.definir(0, 0, 1)
mat.definir(1, 2, 5)
mat.definir(2, 3, 9)

print("\nDepois de definir:")
print(mat)

# Lê valores
print("\nmat.obter(0, 0) =", mat.obter(0, 0))
print("mat.obter(1, 2) =", mat.obter(1, 2))
print("mat.obter(2, 3) =", mat.obter(2, 3))

# Testa erro de índice
try:
    mat.obter(99, 0)
except IndexError as e:
    print("\nErro esperado:", e)

# Testa preencher
mat.preencher(7)
print("\nDepois de preencher com 7:")
print(mat)
