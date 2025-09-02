# student.py

# Lê o número do cartão como string
cartao = input().strip()

# Transforma cada caractere em inteiro
digitos = [int(c) for c in cartao]

# Lista para os cálculos
soma_impares = 0
soma_pares = 0

# Percorre os dígitos de trás para frente com índice
for i, d in enumerate(reversed(digitos), start=1):
    if i % 2 == 1:  # posição ímpar (contando da direita)
        soma_impares += d
    else:  # posição par
        dobro = d * 2
        if dobro > 9:
            dobro = dobro - 9  # soma dos dígitos (ex: 12 -> 1+2=3 = 12-9)
        soma_pares += dobro

# Soma total
soma_total = soma_impares + soma_pares

# Verificação
if soma_total % 10 == 0:
    print("Cartão válido")
else:
    print("Cartão inválido")
# Leia uma linha com o número do cartão
numero = input()

# TODO: implemente a verificação pelo algoritmo de Luhn
# Siga as dicas do README.

# Ao final, imprima exatamente:
# print("Cartão válido")  ou  print("Cartão inválido")
