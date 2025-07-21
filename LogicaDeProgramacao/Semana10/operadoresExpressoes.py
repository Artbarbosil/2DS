# Operadores e Expressões em Python

# Operadores Aritméticos
a = 10
b = 3
print("Soma:", a + b)          # Soma
print("Subtração:", a - b)     # Subtração
print("Multiplicação:", a * b) # Multiplicação
print("Divisão:", a / b)       # Divisão
print("Divisão inteira:", a // b) # Divisão inteira
print("Módulo:", a % b)        # Resto da divisão
print("Exponenciação:", a ** b) # Potência

# Operadores de Comparação
print("Igual:", a == b)        # Igual
print("Diferente:", a != b)    # Diferente
print("Maior que:", a > b)     # Maior que
print("Menor que:", a < b)     # Menor que
print("Maior ou igual:", a >= b) # Maior ou igual
print("Menor ou igual:", a <= b) # Menor ou igual

# Operadores Lógicos
x = True
y = False
print("AND:", x and y)         # E lógico
print("OR:", x or y)           # OU lógico
print("NOT:", not x)           # NÃO lógico

# Operadores de Atribuição
c = 5
c += 2  # c = c + 2
print("Atribuição após soma:", c)
c *= 3  # c = c * 3
print("Atribuição após multiplicação:", c)

# Operadores de Identidade
d = [1, 2, 3]
e = d
print("É o mesmo objeto:", d is e) # Verifica se é o mesmo objeto
print("Não é o mesmo objeto:", d is not e) # Verifica se não é o mesmo objeto

# Operadores de Associação
f = [1, 2, 3, 4, 5]
print("Existe na lista:", 3 in f)  # Verifica se o elemento está na lista
print("Não existe na lista:", 6 not in f) # Verifica se o elemento não está na lista

# Operadores Bitwise
g = 6  # 110 em binário
h = 3  # 011 em binário
print("Bitwise AND:", g & h)  # AND bit a bit
print("Bitwise OR:", g | h)   # OR bit a bit
print("Bitwise XOR:", g ^ h)  # XOR bit a bit
print("Shift à esquerda:", g << 1) # Deslocamento à esquerda
print("Shift à direita:", g >> 1)  # Deslocamento à direita