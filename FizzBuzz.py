def funcao(num):
    if num == 0:
        print(num)
        return
    if num % 3 == 0 and num % 5 == 0:
        print('\n------- FizzBuzz -------\n')
        print(f'{num} / 5 = {num / 5}')
        print(f'{num} / 3 = {num / 3}')
    elif num % 5 == 0:
        print('\n-------- Buzz --------\n')
        print(f'{num} / 5 = {num / 5}')
    elif num % 3 == 0:
        print('\n-------- Fizz --------\n')
        print(f'{num} / 3 = {num / 3}')
    else:
        print(num)

print('---------------------FizzBuzz---------------------')
print('Se der Fizz seu número é divisível por 3.\nSe der Buzz seu número é divisível por 5.'
      '\nSe der FizzBuzz seu número é divisível por 3 e 5.\nSe o número não for divisível por 3 e 5 ele é retornado. ')
print('--------------------------------------------------\n')
x = ''
while x.upper() != 'N':
    n = input('Digite um número: ')
    if n.isdigit():
        funcao(int(n))
        x = input('\n'
                  'Deseja continuar [S/N]: ')
        print('')
    else:
        print('\033[31m Isso não é um número! \033[m')
print('FizzBuzz finalizado. Até a próxima!')
