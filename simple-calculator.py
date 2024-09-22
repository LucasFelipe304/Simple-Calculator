def opcoes():
    print("""
    1 - Soma
    2 - Subtração
    3 - Multiplicação
    4 - Divisão
    5 - Sair do programa
""")
opcoes()

while True:
    escolher_opcao = str(input('Escolha sua opção: ')).strip()

    if escolher_opcao == '1':
        n1 = float(input('Digite um número (N1): '))
        n2 = float(input('Digite um número (N2): '))
        def soma(x, y):
            return x + y
        resultado_soma = soma(n1, n2)
        print(resultado_soma)

    elif escolher_opcao == '2':
        n1 = float(input('Digite um número (N1): '))
        n2 = float(input('Digite um número (N2): '))
        def sub(x, y):
            return x - y
        resultado_sub = sub(n1, n2)
        print(resultado_sub)

    elif escolher_opcao == '3':
        n1 = float(input('Digite um número (N1): '))
        n2 = float(input('Digite um número (N2): '))
        def multiplicacao(x, y):
            return x * y
        resultado_multiplicacao = multiplicacao(n1, n2)
        print(resultado_multiplicacao)
    
    elif escolher_opcao == '4':
        n1 = float(input('Digite um número (N1): '))
        n2 = float(input('Digite um número (N2): '))
        def divisao(x, y):
            if y == 0:
                return "Erro: Divisão por zero não é permitida."
            return x / y
        resultado_divisao = divisao(n1, n2)
        print(resultado_divisao)

    elif escolher_opcao == '5':
        print("Saindo do programa.")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção entre 1 e 5.")