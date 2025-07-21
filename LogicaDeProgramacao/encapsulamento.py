class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome  # Atributo privado
        self.__idade = idade  # Atributo privado

    def get_nome(self):
        return self.__nome  # Método público para acessar o atributo privado

    def set_nome(self, nome):
        self.__nome = nome  # Método público para modificar o atributo privado

    def get_idade(self):
        return self.__idade  # Método público para acessar o atributo privado

    def set_idade(self, idade):
        if idade > 0:  # Validação simples
            self.__idade = idade
        else:
            print("Idade inválida!")

# Exemplo de uso
pessoa = Pessoa("Arthur", 25)

# Acessando os atributos privados através dos métodos públicos
print("Nome:", pessoa.get_nome())
print("Idade:", pessoa.get_idade())

# Modificando os atributos privados através dos métodos públicos
pessoa.set_nome("Barbosa")
pessoa.set_idade(30)

print("Novo Nome:", pessoa.get_nome())
print("Nova Idade:", pessoa.get_idade())