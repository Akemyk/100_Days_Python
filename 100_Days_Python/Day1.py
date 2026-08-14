#---Imprimindo o console---
print("Ola, mundo") #As aspas são para indicar que é uma string, ou seja, um texto. O que torna uma string é o fato de estar entre aspas.
#A saída é o que o computador mostra para o usuário. Já o processamento é o que ele faz com os dados que recebe.

#---Manipulação de Strings---
"""
Podemos economizar tempo e espaço ao invés de escrever uma string linha por linha, usamos \n.
"""
print("Ola, mundo\nOla, mundo")

"""
Podemos concatenar strings, ou seja, juntar duas ou mais strings em uma só.
"""
print("Ola"+ " " +"Julia") #Quando concatemos, as strings se juntam sem espaço, então precisamos colocar um espaço entre aspas para que haja um espaço entre as palavras.
#Erro de identação é um erro que ocorre quando o código não está alinhado corretamente, ou seja, quando há espaços ou tabulações a mais ou a menos do que o necessário. Isso pode causar erros de sintaxe e dificultar a leitura do código.

#---Comando de entrada---
"""
Comando de entrada é o que permite que o comuputador receba os dados do usuário, onde ele é capaz
de digitar no console.
"""
input("Qual o seu nome? ")

print("Ola "+ input("Qual o seu nome? ")+"!")
"""
Evite aninhar funções, ou seja, colocar uma função dentro de outra. Isso pode dificultar a leitura do código e causar erros.    
"""
#---Variáveis---
"""
Variável é um espaço na memória do computador que armazena um valor, que pode ser alterado durante a execução do programa. 
O valor armazenado em uma variável pode ser de diferentes tipos, como números, strings, listas, etc.
"""
nome = input("Qual o seu nome? ") 
print("Olá " + nome)
print("O nome " + nome + " tem " + str(len(nome)) + " caracteres") #Função len() é uma função que retorna o tamanho de uma string, ou seja, o número de caracteres que ela possui.
#Use seu cérebro para pensar e não armazenar. Utilize a documentação ou pesquise.

nome = input("Qual o seu nome? ")
largura = len(nome)
print("O nome " + nome + " tem " + str(largura) + " caracteres") 


copo1 = "leite"
copo2 = "suco"
copo3 = copo2 #suco
copo2 = copo1 #leite
copo1 = copo3 #suco
print(copo1)
print(copo2)

copo1, copo2 = copo2, copo1

#O sinal de = é de atribuição. É pegar o que está na direita e jogar dentro da gaveta(variável).

#---Exercicio final---
print("Gerador de nome de banda")
cidade = input("Qual o nome da cidade em que você cresceu? ")
animal = input("Qual o nome do seu pet? ")
print("O nome da sua banda é "+cidade+" "+animal)

#--Revisão--
print("Estou aprendendo Python no meu próprio ritmo")

print("*")
print("**")
print("***")
print("****")

print("Meu nome é Julia","Tenho 20 anos","E estou no meu 2 semestre da faculdade")

print("No princípio era o Verbo\nO Verbo estava com Deus\nE o Verbo era Deus\nEle estava no peincío com Deus")

print("Como vai você"+ " " +"Julai")

input("Qual a sua comida favorita?")

print("A cor "+input("Qual a sua cor favorita? ")+ " é exelente")

nome = "Julia"
profissao = "Jovem aprendiz"
cidade = "São Paulo"
print(nome + " " + profissao+ " " +cidade)

nome = input("Qual o seu nome?")
print("A fra tem "+str(len(nome))+" quantidade")

nome = input("Qual o seu nome? ")
tamanho = len(nome)
print(tamanho)
if (tamanho < 5):
    print(True)
else:
    print(False) 

A = int(input("Digite um número"))
B = int(input("Digite outro"))
X = A+B
print("X = ",X)

nome = input("Qual o seu nome? ")
print("Olá "+nome)
