# Exemplo de uso do match case em Python

def verificar_dia(dia):
    match dia:
        case "segunda":
            return "Hoje é segunda-feira, início da semana!"
        case "terça":
            return "Hoje é terça-feira, segundo dia útil."
        case "quarta":
            return "Hoje é quarta-feira, metade da semana!"
        case "quinta":
            return "Hoje é quinta-feira, quase lá!"
        case "sexta":
            return "Hoje é sexta-feira, fim de semana chegando!"
        case "sábado" | "domingo":
            return "É fim de semana, aproveite!"
        case _:
            return "Dia inválido!"

# Testando a função
dia = input("Digite o dia da semana: ").lower()
mensagem = verificar_dia(dia)
print(mensagem)