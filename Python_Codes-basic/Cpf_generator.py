import random
import sys


cpf_gerado = ''
for i in range(9):
    cpf_gerado += str(random.randint(0, 9))

cont_regressivo1 = 10

resultado_dig1 = 0
for digito in cpf_gerado:
    resultado_dig1  += int(digito) * cont_regressivo1
    cont_regressivo1 -= 1
digito_1 = (resultado_dig1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = cpf_gerado + str(digito_1)
cont_regressivo2 = 11

result_dig_2 = 0 
for digito in dez_digitos:
    result_dig_2 += int(digito) * cont_regressivo2
    cont_regressivo2 -= 1
digito_2 = (result_dig_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_calculo = f'{cpf_gerado}{digito_1}{digito_2}'

if cpf_gerado == cpf_calculo:
    print(f'O CPF: {cpf_gerado} é válido')
else:
    print(f'O CPF {cpf_gerado} inserido é inválido')