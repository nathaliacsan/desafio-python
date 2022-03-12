# Desenvolver um script(ruby, python) que imprima na tela todos os números de
# 1 até 100, com as seguintes regras:

# Se o número for divisível por 3, deve ser impressa a string 'Ruby'
# Se o número for divisível por 5, deve ser impressa a string 'Python'
# Se o número for divisível por 3 e 5, deve ser impressa a string 'Py-Ruby'
# Nos outros casos, o número deve ser impresso como o próprio número

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print('Py-Ruby')
    elif number % 3 == 0:
        print('Ruby')
    elif number % 5 == 0:
        print('Python')
    else:
        print(number)
