print('i like kenma')
print('o resultado da soma de 1 + 1 é:', 1 + 1)
print(10*(5 + 7)/4)
print(2+(3*3))
print(4**2/3)
print((9**2*6+2)-1)
print(abs(54-57))
print(min(34, 29, 31))

nota = 8
disciplina = 'Lógica de Programação e Algoritmos'

print(nota)
print(disciplina)

print('Disciplina:', disciplina, '. Nota:', nota)

a = 1  # a recebe 1
b = 5  # b recebe 5

resposta = a == b
print(resposta)

resposta = a != b
print(resposta)

frase = 'i like kenma'
print(frase)

print(frase[8])

anime = 'ao haru ride'
category = 'romance'

print(anime)
print(category)

Jesus = 'Vida'
print(Jesus)

s1 = 'Análise e Desenvolvimento'
s1 = s1 + ' de Sistemas'
print(s1)

s1 = 'ant'
s2 = 'bat'
s3 = 'cod'
print(s1 + ' ' + s2 + ' ' + s3)

s1 = 'ant'
print(10*(s1 + ' '))

s1 = 'ant'
s2 = 'bat'
s3 = 'cod'
print(s1, (s2 + ' ')*2+(s3+' ')*3)

s1 = 'ant'
s2 = 'bat'
print((s1 + ' ' + s2 + ' ')*7)

s2 = 'bat'
s3 = 'cod'
print((2*s2 + s3 + ' ')*5)

s2 = 'E' + '-' * 10 + 'U'
print(s1)

nota = 9.5
s2 = 'Você tirou %f na disciplina de Algoritmos' % nota
print(s2)

nota = 9.5
s2 = 'Você tirou %.1f na disciplina de Algoritmos' % nota
print(s2)

nota = 9.5
disciplina = 'Algoritmos'
s3 = 'Você tirou %.1f na disciplina de %s' % (nota, disciplina)
print(s3)

nota = 9.5
disciplina = 'Algoritmos'
s4 = 'Você tirou {} na disciplina de {}' .format(nota, disciplina)

s5 = 'Lógica de Programacão e Algoritmos'
print(s5[28:34])

s6 = 'Lógica de Programacão de Algoritmos'
tamanho = len(s6)
print(tamanho)

idade = input('Qual sua idade?')
print(idade)

nome = input('Qual o seu nome?')
print('Olá {}, seja bem vindo!' .format(nome))

nota = float(input('Qual nota você recebeu na disciplina?'))
print('Você tirou nota {}.'.format(nota))

x = int(input('Digite um número inteiro'))
y = int(input('Digite outro número inteiro'))
res = 'O resultado da soma de {} com {} é {}.'.format(x, y, x + y)
print(res)

d = int(input('Quantos dias?'))
h = int(input('Quantas horas?'))
m = int(input('Quantos minutos?'))
s = int(input('Quantos segundos?'))

total = s + (m * 60) + (h * 60 * 60) + (d * 24 * 60 * 60)
res = 'O resultado total é {}.'.format(total)
print(res)

preco = float(input('Digite o valor do produto: '))
p = float(input('Digite o percentual do desconto (0-100%): '))
desconto = preco * (p/100)
final = preco - desconto

print('O preço do produto é {}. Desconto de {}%'.format(preco, p))
print('O valor do desconto é: {}. O valor final do produto é: {}.'.format(desconto, final))

c = float(input('Digite uma temperatura em Celsius: '))
f = (9 * c / 5) + 32
print('Celsius: {}. Fahrenheite: {}.'.format(c, f))

x = int(input('Digite um valor inteiro: '))
y = int(input('Digite outro valor inteiro: '))
if (x > y):
    print('O primeiro valor é maior que o segundo!')

x = int(input('Digite um valor inteiro: '))
if (x % 2 == 0):
    print('O número é par!')
else:
    print('O número é ímpar!')
if (x % 7 == 0):
    print('Múltiplo de 7')
else:
    print('Não é múltiplo de 7')

x = True
y = False
print(not x)
print(not y)

x = True
y = False
print(x and y)

x = True
y = False
print(x or y)

x = 10
y = 1
res = not x > y
print(res)

x = 10
y = 1
z = 5.5
res = x > y and z == y
print(res)

m1 = float(input('Digite a nota da 1° matéria: '))
m2 = float(input('Digite a nota da 2° matéria: '))
m3 = float(input('Digite a nota da 3° matéria: '))
if m1 >= 7 and m2 >= 7 and m3 >= 7:
    print('O aluno passou de ano.')
else:
    print('O aluno não passou de ano.')

nasc = int(input('Qual seu ano de nascimento?'))
ano = int(input('Em que ano estamos?'))
idade = ano - nasc
print('Você tem {} anos de idade.' .format(idade))
if (idade >= 18):
    print('Você já é de maior. Já pode tirar a carteira de motorista!')
else:
    print('Você ainda não atingiu a idade mínima -18- para tirar a cateira de motorista.')

print('Escolha o que deseja comprar: ')
print('1 - Maça')
print('2 - Laranja')
print('3 - Banana')
produto = int(input('Qual sua escolha? '))
qtd = int(input('Quantas unidades? '))
if (produto == 1):
    pagar = qtd * 2.3
    print('Você comprou {} maças. Total á pagar: {}'.format(qtd, pagar))
else:
    if (produto == 2):
        pagar = qtd * 3.6
        print('Você comprou {} laranjas. Total à pagar: {}'.format(qtd, pagar))
    else:
        if (produto == 3):
            pagar = qtd * 1.85
            print('Você comprou {} bananas. Total à pagar: {}'.format(qtd, pagar))
        else:
            print('Produto não existente')

            a = int(input('Digite o 1° lado do triângulo: '))
b = int(input('Digite o 2° lado do triângulo: '))
c = int(input('Digite o 3° lado do triângulo: '))
if a > 0 and b > 0 and c > 0:
    if a + b > c and a + c > b and b + c > a:
        if a != b and a != c and b != c:
            print('Triângulo escaleno!')
        else:
            if a == b and b == c:
                print('Triângulo equilátero')
            else:
                print('Triângulo isósceles')
    else:
        print('Ao menos um dos valores indicados não servem para forma um triângulo.')
else:
    print('Ao menos um dos valores indicados não servem para forma um triângulo.')

print('Escolha o que deseja comprar: ')
print('1 - Maça')
print('2 - Laranja')
print('3 - Banana')
produto = int(input('Qual sua escolha? '))
qtd = int(input('Quantas unidades? '))
if (produto == 1):
    pagar = qtd * 2.3
    print('Você comprou {} maças. Total á pagar: {}'.format(qtd, pagar))
elif (produto == 2):
    pagar = qtd * 3.6
    print('Você comprou {} laranjas. Total à pagar: {}'.format(qtd, pagar))
elif (produto == 3):
    pagar = qtd * 1.85
    print('Você comprou {} bananas. Total à pagar: {}'.format(qtd, pagar))
else:
    print('Produto não existente')

    print('CALCULADORA:')
print('+ Adição')
print('- Subtração')
print('* Multiplicação')
print('/ Divisão')
print('Pressione outra tecla para sair ')
op = input('Qual operação deseja fazer? ')
x = int(input('Digite o primeiro valor: '))
y = int(input('Digite o segundo valor: '))
if (op == '+'):
    res = x + y
    print('Resultado: {} + {} = {}'.format(x, y, res))
elif (op == '-'):
    res = x - y
    print('Resultado: {} - {} = {}'.format(x, y, res))
elif (op == '*'):
    res = x * y
    print('Resultado: {} * {} = {}'.format(x, y, res))
elif (op == '/'):
    res = x / y
    print('Resultado: {} / {} = {}'.format(x, y, res))

print('PAGAMENTO:')
print('1 - à vista')
print('2 - Parcelamento em 3x')
print('3 - Parcelamento em 5x')
print('4 - Parcelamento em 10x')
print('Pressione outra tecla para sair')
op = int(input('Qual forma de pagamento deseja fazer?'))
valor = float(input('Qual o preço do produto? '))
if (op == 1):
  valor_final = valor * 0.95
  print('Produto comprado À vista. Total a pagar: {}'.format(valor_final))
elif (op == 2):
  valor_final = valor
  parcela = valor_final / 3
  print('Produto parcelado em 3x. Total a pagar: {}. Valor da parcela: {}'.format(valor_final, parcela))
elif (op == 3):
  valor_final = valor * 1.02
  parcela = valor_final / 5
  print('Produto parcelado em 5x. Total a pagar: {}. Valor da parcela: {}'.format(valor_final,parcela))
elif (op == 4):
  valor_final = valor * 1.08
  parcela = valor_final / 10
  print('Produto parcelado em 10x. Total a pagar: {}. Valor da parcela: {}'.format(valor_final, parcela))
else:
  print('Operação inválida!')    
    
