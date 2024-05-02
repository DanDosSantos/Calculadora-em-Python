# Exemplo de calculadora com While
# startswith verifica se a str digitada é a que foi passado no parametro, se for, ela é TRUE.
try:
    while True:
        numero_1 = float(input('Digite um número: '))
        numero_2 = float(input('Digite um número: '))
        operador = input('Digite o operador (+ - / *): ')
        
        num1_e_num2 = numero_1 and numero_2
        
        soma = numero_1 + numero_2
        subtracao = numero_1 - numero_2
        divisao = numero_1 // numero_2
        multiplicacao = numero_1 * numero_2
        operadores = '+-/*'

        if num1_e_num2:
            if operador == '+':
                print(soma)
        if num1_e_num2:
            if operador == '-':
                print(subtracao)
        if num1_e_num2:
            if operador == '/':
                print(divisao)
        if num1_e_num2:
            if operador == '*':
                print(multiplicacao)
        if operador not in operadores:
            print('Operador invalido')

        sair = input('Quer sair? [para sair digite: quero] ').lower().startswith('quero')

        if sair == True:
            break
        
except ValueError:
    print('ERRO. formato de número inválido')