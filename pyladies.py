print('Hello, Ladies!')

# nome1, nome2, nome3 = 'Isa', 'Mara', 'Marina'
# print (nome1, nome2, nome3)

# a = 2
# type (a)

# a = 2
# b =3
# c = 2.0
# d = '2.0'

# print (a + b)

# print (b ** a)

# print ('Batata frita'.upper())
# print ('OIIIII'.lower())
# print ('Pyladies ' + 'São Paulo')
# print ('pão de queijo'.capitalize())
# print ('bolacha ou biscoito'.title())

# expectativa = 'stranger things'

# print(expectativa.upper())
# print(expectativa.title())
# print(expectativa[:: -1])


# cat = 'Gatinho'

# print (cat[:6] + 'a') #trocar 'o' por 'a'

# print (len(cat)) #Tamanho da string: conta quantos caracteres tem uma string

# chaves = 'Eu prefiro morrer do que perder a vida.'

# print (len(chaves)) #Qual o tamanho da string?
# print (chaves.startswith('p')) #Verifique se começa com 'p'?
# print (chaves.endswith('.')) #Verifique se termina com '.'
# print (chaves.find(',')) #Verifique a posição do caractere ','
# print (chaves[:38] + '!') #Troque o caractere '.' por '!'

# listaMercado = ['1 kg de banana', '12 ovos', '1kg de farinha']
# listaMercado.append('fermento em pó')
# print(listaMercado) #Dada a lista mercado = ['1 kg de banana', '12 ovos', '1kg de farinha'], acrescente a string 'fermento em pó'.

# a = 3.0112
# print('Resultado = {}'.format(int(a)))
# Resultado = 3

# nome = input('Qual o seu nome? ')
# name = input()  # leia uma única linha e armazene-a na variável &quot;nome&quot;
# print('Hi ' + name + '!')

# Crie um código para uma outra pessoa adivinhar um número de 1 a 10.
# n = 8

# numUsuario = int(input('Digite umm número de 1 a 10: '))

# if numUsuario > 10 or numUsuario < 0:
#     print('Ops! Escolha um número de 1 a 10')
# elif numUsuario > n:
#     print('Errou! Seu número é maior que o número original: ' + str(n))
# elif numUsuario < n:
#     print('Errou! Seu número é menor que o número original: ' + str(n))
# else:
#      print('Acertou! Seu número é igual ao número original: ' + str(n))


#Faça um código, usando contadores e acumuladores, que calcule quanto gastei durante o evento.
# contador = 1
# somaLanches = 0

# while contador <= 7:
#     lanche = float(input('Gastei R$: '))
#     somaLanches += lanche
#     contador += 1

# print(somaLanches)

# soma = 0
# while True: #enquanto for verdadeiro
#     valor = float(input('Digite o valor gasto: '))
#     if valor == 0:
#         break
#     soma = soma + valor
# print('Soma: {}'.format(soma))

# alunas = ['Ana', 'Beatriz', 'Caroline', 'Denise', 'Élida',
# 'Fernanda', 'Glaucia']
# for aluna in alunas:
#     if aluna.startswith('C'):
#         print(aluna)

# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# soma_par = 0
# for numero in lista:
#     if (numero % 2) == 0:
#      soma_par = soma_par + numero
# print('A soma dos pares de toda lista é {}'.format(soma_par))

#verifique apenas linguagens que comecem com aletra P e imprima na tela.
linguagens = ['Java', 'JavaScript', 'PHP', 'C', 'Python'] 
for programacao in linguagens:
    if programacao.startswith('P'):
        #  print(programacao)
         programacao = 'x'
         print(programacao)
print(linguagens)

        