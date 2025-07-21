# Exemplo de aninhamento de estruturas condicionais
idade = int(input("Digite sua idade: "))
habilitacao = input("Você possui habilitação? (sim/não): ").strip().lower()

if idade >= 18:
    if habilitacao == "sim":
        print("Você pode dirigir.")
    else:
        print("Você não pode dirigir, pois não possui habilitação.")
else:
    print("Você não pode dirigir, pois é menor de idade.")