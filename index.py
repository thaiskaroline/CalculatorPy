# Este programa faz uma calculadora simples que pode adicionar, subtrair, multiplicar ou dividir dependendo da entrada do usuário

# Esta função adiciona dois números 
def adicionar(x, y):
    return x + y

# Esta função subtrai dois números
def subtrair(x, y):
    return x - y

# Esta função multiplica dois números
def multiplicar(x, y):
    return x * y

# Esta função divide dois números
def dividir(x, y):
    return x / y

print("Selecione a operação.")
print("1.Adicionar")
print("2.Subtrair")
print("3.Multiplicar")
print("4.Dividir")

while True:
    # Pegue a entrada do usuário
    escolha = input("Digite a escolha (1/2/3/4): ")

    # Verifique se a escolha é uma das quatro opções
    if escolha in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Entrada inválida. Por favor digite um número.")
            continue
        if escolha == '1':
            print(num1, "+", num2, "=", adicionar(num1, num2))
        elif escolha == '2':
            print(num1, "-", num2, "=", subtrair(num1, num2))
        elif escolha == '3':
            print(num1, "*", num2, "=", multiplicar(num1, num2))
        elif escolha == '4':
            print(num1, "/", num2, "=", dividir(num1, num2))
        # Verifique se o usuário quer outra calculadora
        # Quebre o loop se a resposta for não
        proxima_calculadora = input("Vamos fazer o próximo cálculo? (s/n): ")
        if proxima_calculadora == "n":
            break
    else:
        print("Entrada inválida")

        # Pão de queijo