while True:
        num1 = input ("Digite um numero: ")
        num2 = input ("Digite outro numero: ")
        operator = input ('Digite o operador simples desejado (+ - / *): ')
        
        num1_float = 0
        num2_float = 0
        num_valid = None
        
        try:
            num1_float = float(num1)
            num2_float = float(num2)
            num_valid = True
        except:
            num_valid = None

        if  num_valid is None:
            print('Um ou ambos os numeros digitados sao invalidos. Digite novamente')
            continue   

        operator_permited = '+-/*'

        if operator not in operator_permited:
            print('Digite apenas os operadores informados.')
            continue     
        
        if len(operator) > 1:
            print('Digite apenas um operador.')
            continue 

        print('Realizando sua conta. Confira abaixo o resultado: ')

        if operator == '+':
            print(f'{num1_float} + {num2_float}=',num1_float + num2_float)
        elif operator == '-':
            print(f'{num1_float} - {num2_float}=',num1_float - num2_float)
        elif operator == '/':
            print(f'{num1_float} / {num2_float}=',num1_float / num2_float)
        elif operator == '*':
            print(f'{num1_float} * {num2_float}=',num1_float * num2_float)


        sair = input('Quer Sair? [S]im: ').lower().startswith('s')

        if sair is True:
            break