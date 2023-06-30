import os
list = []
while True:
    print('Select one option')
    option = input('[a]dd [d]delete [l]ist: ')

    if option == 'a':
        os.system('cls')
        produto = input('Product: ')
        list.append(produto)
    elif option == 'd':
        index_str = input(
            'Choose a product(index) to be deleted : '
        )

        try:
            indice = int(index_str)
            del list[indice]
        except ValueError:
            print('Insert a integer.')
        except IndexError:
            print('Index does not exist in the list.')
    elif option == 'l':
        os.system('cls')

        if len(list) == 0:
            print('Theres no product in the shopping list.')
        
        for i, value in enumerate(list, start= 1):
            print(i, value)
