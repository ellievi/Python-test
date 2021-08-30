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
