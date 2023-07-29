entry = input ('Insert your CPF: ')
cpf_user = entry.replace('.', '').replace('-', '')

nine_digits = cpf_user[:9]
cont_regressivo1 = 10

result_dig1 = 0
for digit in nine_digits:
    result_dig1  += int(digit) * cont_regressivo1
    cont_regressivo1 -= 1
digit_1 = (result_dig1 * 10) % 11
digit_1 = digit_1 if digit_1 <= 9 else 0

ten_digits = nine_digits + str(digit_1)
cont_regressivo2 = 11

result_dig_2 = 0 
for digit in ten_digits:
    result_dig_2 += int(digit) * cont_regressivo2
    cont_regressivo2 -= 1
digit_2 = (result_dig_2 * 10) % 11
digit_2 = digit_2 if digit_2 <= 9 else 0

cpf_calculated = f'{nine_digits}{digit_1}{digit_2}'

if cpf_user == cpf_calculated:
    print(f'The CPF: {cpf_user} is valid')
else:
    print('The inserted CPF is unvalid')