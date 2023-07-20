while True:
        num1 = input ("Enter one number: ")
        num2 = input ("Enter another number: ")
        operator = input ('Enter any of the operators (+ - / * ): ')
        
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
            print('One or both of the numbers entered are invalid. Type it again')
            continue   

        operator_permited = '+-/*'

        if operator not in operator_permited:
            print('Enter only the given operators.')
            continue     
        
        if len(operator) > 1:
            print('Enter only one operator.')
            continue 

        print('Making your account. Check the result below: ')

        if operator == '+':
            print(f'{num1_float} + {num2_float}=',num1_float + num2_float)
        elif operator == '-':
            print(f'{num1_float} - {num2_float}=',num1_float - num2_float)
        elif operator == '/':
            print(f'{num1_float} / {num2_float}=',num1_float / num2_float)
        elif operator == '*':
            print(f'{num1_float} * {num2_float}=',num1_float * num2_float)


        out = input('Do you want to quit? [Y]es: ').lower().startswith('y')

        if out is True:
            break