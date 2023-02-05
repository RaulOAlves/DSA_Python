# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!

print('\n******************* Calculadora em Python *******************\n\n Selecione o número da operação desejada:\n\n1- Soma\n2- Subtração\n3- Multiplicação\n4- Divisão\n')

operacao = int(input('Digite sua opção (1/2/3/4): '))
x = int(input('Digite o primeiro número: '))
y = int(input('Digite o segundo número: '))

if operacao == 1:
    z = x + y
    print ('{} + {} = {}'.format(x,y,z))
elif operacao == 2:
    z = x - y
    print ('{} - {} = {}'.format(x,y,z))
elif operacao == 3:
    z = x * y
    print ('{} * {} = {}'.format(x,y,z))
elif operacao == 4:
    z = x / y
    print ('{} / {} = {}'.format(x,y,z))
else:
    print('Operação inválida')
