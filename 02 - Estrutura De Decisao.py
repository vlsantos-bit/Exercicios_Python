#!/usr/bin/env python
# coding: utf-8

# # 02 - Estrutura De Decisão https://wiki.python.org.br/EstruturaDeDecisao


# # 1-Faça um Programa que peça dois números e imprima o maior deles


da = [] 
for i in range(0,2,1):
    x=input("Insira dois numeros = ")
    da.append(float(x))

print("Maior numero",max(da))


# # 2-Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.


n = input('Insira um valor = ')
n = float(n)
if n>0:
    print('Positivo')
else:
    print('Negativo')


# # 3 - Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.



l = input('Insira uma letra = ')
if l=='M':
    print('Masculino')
elif l=='F':
    print('Feminino')


# # 4 - Faça um Programa que verifique se uma letra digitada é vogal ou consoante. 



l1 = input('Insira uma letra = ')

if l1 == 'A':
    print('Vogal')
elif l1 == 'E':
    print('Vogal')
elif l1 == 'I':
    print('Vogal')
elif l1 == 'O':
    print('Vogal')
elif l1 == 'U':
    print('Vogal')
elif l1 == 'a':
    print('Vogal')
elif l1 == 'e':
    print('Vogal')
elif l1 == 'i':
    print('Vogal')
elif l1 == 'o':
    print('Vogal')
elif l1 == 'u':
    print('Vogal')
else:
    print('Consoante')


# # 5 - Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar: 
# 
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.




n1 = input("Insira dois numeros = ")
n2 = input("Insira dois numeros = ")
n1 = float(n1)
n2 = float(n2)

no = (n1+n2)/2

if 7<=no<=9:
    print('Média =', no ,', Aluno Aprovado')

elif no==10:
    print('Média =', no ,', Aluno Aprovado com Distinção')
else:
    print('Média =', no ,', Aluno Reprovado')


# # 6 e 7 - Faça um Programa que leia três números e mostre o maior deles e depois menor




da = [] 
for i in range(0,3,1):
    x=input("Insira 3 numeros = ")
    da.append(float(x))
print('Maior Valor', max(da))





da = [] 
for i in range(0,3,1):
    x=input("Insira 3 numeros = ")
    da.append(float(x))
print('Menor valor', min(da))


# # 8 - Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.




import pandas as pd
prod1 = float(input('Valor Produto 1 = '))
prod2 = float(input('Valor Produto 2 = '))
prod3 = float(input('Valor Produto 3 = '))

da = {'Produto 1':prod1,'Produto 2':prod2,'Produto 3':prod3}
data = pd.DataFrame(da,index=[0])
dt = data.T
dt=dt.loc[dt[:].idxmin()]
dt = dt.index
pr = dt[0]
print('Compra mais barata =',pr, ' -- Valor = ', min(data.min()))


# # 9 - Faça um Programa que leia três números e mostre-os em ordem decrescente.




da = [] 
for i in range(0,3,1):
    x=input("Insira 3 valores = ")
    da.append(float(x))

da.sort()
print("Ordem crescente",da)


# # 10 - Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.




x=input("Insira perido de estudo, ex: M-Matutino, V-Vespertino, N-Noturno = ")
if x == 'V':
    print('Boa tarde')
elif x=='M':
    print('Matutino')
elif x=='N':
    print('Boa noite')
else:
    print('Valor inválido')


# # 11 - As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.



s = float(input('Valor do salário = '))

#taxas
t1 = s*0.20
t2 = s*0.15
t3 = s*0.10
t4 = s*0.05

if s<=280:
    print('Salário atual:',s,' Percentual: 20%',' Aumento(R$):',t1,' Novo Salário:',s+t1)
elif 280<s<=700:
    print('Salário atual:',s,' Percentual: 15%',' Aumento(R$):',t2,' Novo Salário:',s+t2)
elif 700<s<=1500:
    print('Salário atual:',s,' Percentual: 10%',' Aumento(R$):',t3,' Novo Salário:',s+t3)
elif s>1500:
    print('Salário atual:',s,' Percentual: 5%',' Aumento(R$):',t4,' Novo Salário:',s+t4)


# # 12 - Faça um programa para o cálculo de uma folha de pagamento.
# 
# Sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00  
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00


#-------------------------------------------------------------------------------------------
s = float(input('Valor da hora = '))
h = float(input('N° de horas trabalhadas = '))
sa = s*h
#taxas FGTS-------------------------------------------------------------------------------
t1 = sa*0.05
t2 = sa*0.10
t3 = sa*0.20
#Descontos--------------------------------------------------------------------------------
sin = sa*0.03
FGTS = sa*0.11
IR1 = 0.0
INSS = sa*0.10
#Caso 1-----------------------------------------------------------------------------------
desc1 = (IR1+INSS+sin)
sat1 = sa-desc1
if 0<sa<=900:
    print('Salário Bruto:',s,'*',h,'       : R$',sa)
    print('(-) IR (Isento)                 : R$',IR1)
    print('(-) INSS ( 10%)                 : R$',INSS)
    print('FGTS (11%)                      : R$',FGTS)
    print('Sindicato (3%)                  : R$',sin)
    print('Total de descontos              : R$',desc1)
    print('Salário Liquído                 : R$',sat1)

#Caso 2-----------------------------------------------------------------------------------
desc2 = (t1+INSS+sin)
sat2 = sa-desc2
if 900<sa<=1500:
    print('Salário Bruto:',s,'*',h,'       : R$',sa)
    print('(-) IR (5%)                 : R$',t1)
    print('(-) INSS ( 10%)                 : R$',INSS)
    print('FGTS (11%)                      : R$',FGTS)
    print('Sindicato (3%)                  : R$',sin)
    print('Total de descontos              : R$',desc2)
    print('Salário Liquído                 : R$',sat2)
#Caso 2-----------------------------------------------------------------------------------
desc3 = (t2+INSS+sin)
sat3 = sa-desc3
if 1500<sa<=2500:
    print('Salário Bruto:',s,'*',h,'       : R$',sa)
    print('(-) IR (10%)                 : R$',t2)
    print('(-) INSS ( 10%)                 : R$',INSS)
    print('FGTS (11%)                      : R$',FGTS)
    print('Sindicato (3%)                  : R$',sin)
    print('Total de descontos              : R$',desc3)
    print('Salário Liquído                 : R$',sat3)
#Caso 3-----------------------------------------------------------------------------------
desc4 = (t3+INSS+sin)
sat4 = sa-desc4
if sa>2500:
    print('Salário Bruto:',s,'*',h,'       : R$',sa)
    print('(-) IR (20%)                 : R$',t3)
    print('(-) INSS ( 10%)                 : R$',INSS)
    print('FGTS (11%)                      : R$',FGTS)
    print('Sindicato (3%)                  : R$',sin)
    print('Total de descontos              : R$',desc4)
    print('Salário Liquído                 : R$',sat4)


# # 13 - Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.




n = float(input('Insira um valor de 1-7 = '))
if n==1:
    print('Domingo')
elif n==2:
    print('Segunda')
elif n==3:
    print('Terça')
elif n==4:
    print('Quarta')
elif n==5:
    print('Quinta')
elif n==6:
    print('Sexta')
elif n==7:
    print('Sabádo')
else:
    print('Valor inválido')


# # 14 - Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
# 
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E

O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
#-------------------------------------------------------------------------------------------


import pandas as pd
nota1 = float(input('Insira a nota 1 = '))
nota2 = float(input('Insira a nota 2 = '))
data = {'Nota 1':nota1, 'Nota2':nota2}
data = pd.DataFrame(data,index=[0])
me = (nota1+nota2)/2

if 9<me<=10:
    print('Média:',me,'Conceito: A','- Aprovado')
elif 7.5<me<=9:
    print('Média:',me,'Conceito: B','- Aprovado')
elif 6<me<=7.5:
    print('Média:',me,'Conceito: C','- Aprovado')
elif 4<me<=6:
    print('Média:',me,'Conceito: D','- Reprovado')
elif 0<=me<=4:
    print('Média:',me,'Conceito: E','- Reprovado')
    
print(data)


# # 15 - Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# 
# Dicas:   
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;




l1 = float(input('lado 1 do triangulo = '))
l2 = float(input('lado 2 do triangulo = '))
l3 = float(input('lado 3 do triangulo = '))
cond1 = l1+l2
cond2 = l2+l3
cond3 = l3+l1

#Para ser um triangulo soma de quaisquer dois lados for maior que o terceiro
if cond1>l3:
    print('É um triangulo')
elif cond2>l1:
    print('É um triangulo')
elif cond3>l2:
    print('É um triangulo')
else:
    print('Não é triangulo')

if l1==l2==l3:
    print('Triangulo Equilatero')
elif l1==l2 or l2==l3 or l3==l1:
    print('Triangulo Isósceles')
elif l1!=l2!=l3:
    print('Triângulo Escaleno')


# # 16 - Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. 
O programa deverá pedir os valores de a, b e c e fazer as consistências, 
informando ao usuário nas seguintes situações:

*Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
*Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
*Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
*Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
#-------------------------------------------------------------------------------------------


a = float(input('Insira o valor de a = '))
b = float(input('Insira o valor de b = '))
c = float(input('Insira o valor de c = '))

delt = (((-b)**2)-(4*a*c))
x1 = (delt**0.5)/2*a
x2 = (-(delt**0.5))/2*a
# 1-Condição------------------------------------------------------------------
if a==0:
    print('A equação não é do segundo grau')
    print('Saindo...')
    exit()
# 2-Condição-------------------------------------------------------------------    
if delt<0:
    print('Equação não possui raizes reais (Delta Negativo)')
    print('Saindo...')
    exit()
# 3-Condição-------------------------------------------------------------------
if delt==0:
    print('Equação possui apenas uma raiz =', x1)

# 4-Condição-------------------------------------------------------------------
if delt>0:
    print('Raiz 1 = ', x1)
    print('Raiz 2 = ', x2)


# # 17 - Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.


import numpy as np 
ins = int(input('Insira um ano = '))

ano_bi = []
#Gerador de numeros (para alterar, mudar valore no range)
for i in range(-1,10000,4):
    ano_bi.append([i+1])

ano_b = np.array(ano_bi).flatten()

if ins in ano_b:
    print('Ano Bissexto')
else:
    print('Ano não Bissexto')


# # 18 - Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
# 
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:

326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades 

Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
#-------------------------------------------------------------------------------------------


import math as ma
def transform(n):
    n = int(n)
    if n>1000:
        print('(Erro) - Numero não está de acordo')
        exit()
    #Centena---------------------------------------------------------------
    ci = n/100
    c = ma.floor(ci)
    #Dezena----------------------------------------------------------------
    di = int('{:0<3}'.format(c))
    d = (n-di)/10
    d = ma.floor(d)
    #Unidade---------------------------------------------------------------
    ui = int('{:0<2}'.format(d))
    u = n-di-ui
    #Condições-------------------------------------------------------------
    if ((c==0) and (d==0) and (u==0)):
        print(n,' = ',u,'Unidade')        
    elif ((c==0) and (d==0)):
        if 0<u<=1:
            print(n,' = ',u,'Unidade')
        else:
            print(n,' = ',u,'Unidades')    
    elif ((c==0) and (u==0)):
        if 0<d<=1:
            print(n,' = ',d,'Dezena')
        else:
            print(n,' = ',d,'Dezenas')     
    elif ((u==0) and (d==0)):
        if 0<c<=1:
            print(n,' = ',c,'Centena')
        else:
            print(n,' = ',c,'Centenas')    
    elif c==0:
        if ((0<d<=1) and (0<u<=1)):
            print(n,' = ',d,'Dezena e ',u,'Unidade')
        elif 0<d<=1:
            print(n,' = ',d,'Dezena e ',u,'Unidades')
        elif 0<u<=1:
            print(n,' = ',d,'Dezenas e ',u,'Unidade')
        else:
            print(n,' = ',d,'Dezenas e ',u,'Unidades')                        
    elif d==0:
        if ((0<c<=1) and (0<u<=1)):
            print(n,' = ',c,'Centena e ',u,'Unidade')
        elif 0<c<=1:
            print(n,' = ',c,'Centena e ',u,'Unidades')
        elif 0<u<=1:
            print(n,' = ',c,'Centenas e ',u,'Unidade')
        else:
            print(n,' = ',c,'Centenas e ',u,'Unidades')                        
    elif u==0:
        if ((0<c<=1) and (0<d<=1)):
            print(n,' = ',c,'Centena, ',d,'Dezena')
        elif 0<c<=1:
            print(n,' = ',c,'Centena, ',d,'Dezenas')
        elif 0<d<=1:
            print(n,' = ',c,'Centenas, ',d,'Unidade')
        else:
            print(n,' = ',c,'Centenas e ',d,'Dezenas')
    elif ((0<c<=1) and (0<d<=1) and (0<u<=1)):
        print(n,' = ',c,'Centena, ',d,'Dezena e ',u,'Unidade')
    else:
        print(n,' = ',c,'Centenas, ',d,'Dezenas e ',u,'Unidades')
#Teste------------------------------------------------------------------------------------ 
x = [326,300,100,320,310,305,301,101,311,111,25,20,10,21,11,1,7,16]

for i in range(-1,len(x)-1,1):
    a=transform(x[i+1])


# # 19 - Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
*A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
*A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
*A mensagem "Aprovado com Distinção", se a média for igual a 10.
#-------------------------------------------------------------------------------------------


not1 = float(input('Insira primeira nota = '))
not2 = float(input('Insira primeira nota = '))
not3 = float(input('Insira primeira nota = '))

me = ((not1+not2+not3)/3)

if 7<=me<=9:
    print('Aprovado com a respectiva média = ', me)
if me<7:
    print('Reprovado com a respectiva média = ', me)
if me==10:
    print('Aprovado com Distinção, respectiva média = ', me)


# # 20 - Faça um Programa para um caixa eletrônico.  
# 
# O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
# 
*Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
*Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de
#-------------------------------------------------------------------------------------------


import pandas 
saq = int(input('Insira o valor desejado para o saque = '))
#criando dicionário
dic_n = {0:'zero',1:'uma',2:'duas',
         3:'três',4:'quatro',5:'cinco',6:'seis',7:'sete',8:'oito',9:'nove',10:'dez'}
v = saq
n1 = [100]
n2 = [50]
n3 = [10]
n4 = [5]
n5 = [1]
#Para valores de 100------------------------------------------------------
cen=v
l_cen = []
while(cen>=100):
    cen-=100
    l_cen.append(cen)
n_cen = len(l_cen)
#valores de 50------------------------------------------------------------
ci = cen
l_ci= []
while(ci>=50):
    ci-=50
    l_ci.append(ci)
n_ci = len(l_ci)
#valores de 10------------------------------------------------------------
de = cen
l_de= []
while(de>=10):
    de-=10
    l_de.append(de)
n_de = len(l_de)
#valores de 5--------------------------------------------------------------
u5 = de
l_u5 = []
while(u5>=5):
    u5-=5
    l_u5.append(u5)
n_u5 = len(l_u5)
#valores de 1--------------------------------------------------------------
u1 = u5
l_u1 = []
for u1 in range(u1):
    u1-=1
    l_u1.append(u1)
n_u1 = len(l_u1)
#Aplicando dicionário------------------------------------------------------
inf = {'cem':n_cen,'cinquenta':n_ci,'dez':n_de,'cinco':n_u5,'um':n_u1}
data = pd.DataFrame(inf,index=[0])
data = data.replace(dic_n)
data=data.max()
#Condições de visualização-------------------------------------------------
if data.cinquenta=='uma':
    del(data['dez'])
df = data[data.str.contains("zero") == False]
a = len(df)
#condiçoes para visualizar extremos
if  v>600:
    print('Função indisponível, para realizar o saque de',v,'R$.')
    print('Valor máximo de saque é de 600 R$')
elif  v<10:
    print('Função indisponível, para realizar o saque de',v,'R$.')
    print('Valor minímo de saque é de 10 R$')
if a==1:
    if df[0]=='uma':
        print('Para sacar a quantia de',v,'reais, o programa fornece',df[0],'nota de',df.index[0])
    else:
        print('Para sacar a quantia de',v,'reais, o programa fornece',df[0],'nota de',df.index[0])
if a==2:
    if ((df[0]=='uma')and(df[1]=='uma')):
        print('Para sacar a quantia de',v,'reais, o programa fornece',df[0],'nota de',df.index[0]
         ,'e',df[1],'nota de',df.index[1])
    elif df[0]=='uma':
        print('Para sacar a quantia de',v,'reais, o programa fornece',df[0],'nota de',df.index[0]
         ,'e',df[1],'notas de',df.index[1])
    elif df[1]=='uma':
        print('Para sacar a quantia de',v,'reais, o programa fornece',df[0],'notas de',df.index[0]
         ,'e',df[1],'nota de',df.index[1])
    else:
        print('Para sacar a quantia de',v,'reais, o programa fornece',df[0],'notas de',df.index[0]
         ,'e',df[1],'notas de',df.index[1])
if a==3:
    if ((df[0]=='uma')and(df[1]=='uma')and(df[2]=='uma')):
        print('Para sacar a quantia de',v,'reais, o programa fornece',df[0],'nota de',df.index[0]
         ,',',df[1],'nota de',df.index[1],'e',df[2],'nota de',df.index[2])
    elif df[0]=='uma':
         print('Para sacar a quantia de',v,'reais, o programa fornece',df[0],'nota de',df.index[0]
         ,',',df[1],'notas de',df.index[1],'e',df[2],'notas de',df.index[2])
    elif df[1]=='uma':
         print('Para sacar a quantia de',v,'reais, o programa fornece',df[0],'notas de',df.index[0]
         ,',',df[1],'nota de',df.index[1],'e',df[2],'notas de',df.index[2])
    elif df[2]=='uma':
         print('Para sacar a quantia de',v,'reais, o programa fornece',df[0],'notas de',df.index[0]
         ,',',df[1],'notas de',df.index[1],'e',df[2],'nota de',df.index[2])
    else: 
        print('Para sacar a quantia de',v,'reais, o programa fornece',df[0],'notas de',df.index[0]
        ,',',df[1],'notas de',df.index[1],'e',df[2],'notas de',df.index[2])
if a==4:
    if ((df[0]=='uma')and(df[1]=='uma')and(df[2]=='uma')and(df[3]=='uma')):
        print('Para sacar a quantia de',v,'reais, o programa fornece',df[0],'nota de',df.index[0]
         ,',',df[1],'nota de',df.index[1],',',df[2],'nota de',df.index[2],'e',df[3],'nota de',df.index[3])
    elif df[0]=='uma':
        print('Para sacar a quantia de',v,'reais, o programa fornece',df[0],'nota de',df.index[0]
         ,',',df[1],'notas de',df.index[1],',',df[2],'notas de',df.index[2],'e',df[3],'notas de',df.index[3])
    elif df[1]=='uma':
        print('Para sacar a quantia de',v,'reais, o programa fornece',df[0],'notas de',df.index[0]
         ,',',df[1],'nota de',df.index[1],',',df[2],'notas de',df.index[2],'e',df[3],'notas de',df.index[3])
    elif df[2]=='uma':
        print('Para sacar a quantia de',v,'reais, o programa fornece',df[0],'notas de',df.index[0]
         ,',',df[1],'notas de',df.index[1],',',df[2],'nota de',df.index[2],'e',df[3],'notas de',df.index[3])
    elif df[3]=='uma':
        print('Para sacar a quantia de',v,'reais, o programa fornece',df[0],'notas de',df.index[0]
         ,',',df[1],'notas de',df.index[1],',',df[2],'nota de',df.index[2],'e',df[3],'nota de',df.index[3])
    else: 
        print('Para sacar a quantia de',v,'reais, o programa fornece',df[0],'notas de',df.index[0]
        ,',',df[1],'notas de',df.index[1],'e',df[2],'notas de',df.index[2])


# # 21 - Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).
# 




n = int(input('Insira um valor inteiro = '))
da = n%2
if da==0:
    print('Este valor é Par')
else:
    print('Este valor é Impar')


# # 22 - Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.




import math as ma
n = input('Insira um valor = ')

if ',' in n:
    print('Valor decimal')
elif '.' in n:
    print('Valor decimal')
else:
    print('Valor inteiro ')


# # 23 - Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
# 
par ou ímpar;
positivo ou negativo;
inteiro ou decimal.
#-------------------------------------------------------------------------------------------


n1 = float(input('insira o primeiro valor = '))
n2 = float(input('insira o primeiro valor = '))
op = input('Escolha a operação desejada ex(soma, subtracao, multiplicacao e divisao) = ')

#Multiplicação
Multiplicacao = n1*n2
p_i=Multiplicacao%2
mult = str(Multiplicacao)
#Divisão
Divisao = n1/n2
d_i=Divisao%2
div = str(Divisao)
 #Soma
Soma = n1+n2
so_i=Soma%2
som = str(Soma)

#Subtração
Subtracao = n1-n2
su_i=Subtracao%2
sub = str(Subtracao)

if op=='multiplicacao':
    print('Resultado = ',Multiplicacao)
    if Multiplicacao>0:
        print('Valor Positivo')
    else:
        print('Valor Negativo')
    if p_i==0:
        print('Valor Par')
    else:
        print('Valor Ímpar')       
    if ',' in mult:
        print('Valor decimal')
    elif '.0' in mult:
        print('Valor inteiro')
    elif '.' in mult:
        print('Valor decimal')
    else:
        print('Valor inteiro ')   
elif op=='divisao':
    print('Resultado = ',Divisao)
    if Divisao>0:
        print('Valor Positivo')
    else:
        print('Valor Negativo')
    if d_i==0:
        print('Valor Par')
    else:
        print('Valor Ímpar')       
    if ',' in div:
        print('Valor decimal')
    elif '.0' in div:
        print('Valor inteiro')
    elif '.' in div:
        print('Valor decimal')
    else:
        print('Valor inteiro ') 
elif op=='soma':
    print('Resultado = ',Soma)
    if Divisao>0:
        print('Valor Positivo')
    else:
        print('Valor Negativo')
    if so_i==0:
        print('Valor Par')
    else:
        print('Valor Ímpar')       
    if ',' in som:
        print('Valor decimal')
    elif '.0' in som:
        print('Valor inteiro')
    elif '.' in som:
        print('Valor decimal')
    else:
        print('Valor inteiro ')
elif op=='subtracao':
    print('Resultado = ',Subtracao)
    if Divisao>0:
        print('Valor Positivo')
    else:
        print('Valor Negativo')
    if su_i==0:
        print('Valor Par')
    else:
        print('Valor Ímpar')       
    if ',' in sub:
        print('Valor decimal')
    elif '.0' in sub:
        print('Valor inteiro')
    elif '.' in sub:
        print('Valor decimal')
    else:
        print('Valor inteiro ')       
else:
    print('Operação inválida')


# # 24 - Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
1-"Telefonou para a vítima?"
2-"Esteve no local do crime?"
3-"Mora perto da vítima?"
4-"Devia para a vítima?"
5-"Já trabalhou com a vítima?"

O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
#-------------------------------------------------------------------------------------------


print('Responda as questões abaixo com sim ou não')
q1 = str(input("Telefonou para a vítima? = "))
q2 = str(input("Esteve no local do crime? = "))
q3 = str(input("Mora perto da vítima? = "))
q4 = str(input("Devia para a vítima? = "))
q5 = str(input("Já trabalhou com a vítima? = "))
q_dados = ([q1]+[q2]+[q3]+[q4]+[q5]).count('sim')

#condições--------------------------------------------------------
if q_dados==0:
    print('Inocente(a)')
elif q_dados==2:
    print('Suspeito(a)')
elif q_dados==3:
    print('Cúmplice(a)')
elif q_dados==4:
    print('Cúmplice(a)')
else:
    print('Assassino(a)')


# # 25 - Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool: até 20 litros, desconto de 3% por litro e acima de 20 litros, desconto de 5% por litro

Gasolina: até 20 litros, desconto de 4% por litro e acima de 20 litros, desconto de 6% por litro# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é RS 2,50 o preço do litro do álcool é RS 1,90.
#-------------------------------------------------------------------------------------------


l = float(input('Quantidade de litros usados = '))
tc = str(input('Tipo de combustível (ex: G-gasolina/ A-alcool) = '))
if tc == 'G':
    print('Gasolina')
    if l<=20:
        p_g=l*2.50
        des = p_g*0.03
        ptg = p_g-des      
        print('Desconto de 3% aplicado, Valor a ser pago = ',ptg, 'reais')
    else:
        p_g1=l*2.50
        des1 = p_g1*0.05
        ptg1 = p_g1-des1      
        print('Desconto de 5% aplicado, Valor a ser pago = ',ptg1, 'reais')
if tc == 'A':
    print('Álcool')
    if l<=20:
        p_a=l*2.50
        des = p_a*0.04
        pta = p_a-des      
        print('Desconto de 4% aplicado, Valor a ser pago = ',pta, 'reais')
    else:
        p_a1=l*2.50
        des1 = p_a1*0.06
        pta1 = p_a1-des1      
        print('Desconto de 6% aplicado, Valor a ser pago = ',pta1, 'reais')


# # 26 - Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg

Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por KgSe o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
#-------------------------------------------------------------------------------------------


mor = float(input('Insira o ṇ° kilos de morango = '))
mac = float(input('Insira o ṇ° kilos de maçã = '))

if mor<=5:
    p_mor=mor*2.50
else:
    p_mor = mor*2.20

if mac<=5:
    p_mac=mac*1.80
else:
    p_mac = mac*1.50

pes_t = mor+mac    
pre_t = p_mac+p_mor

if ((pes_t>8) or (pre_t>25)):
    pre_t = pre_t*0.10
    
print('Quantidade de morango (KG) = ',mor, ',quantidade de maçã = ',mac)
print('Valor a ser pago = ', pre_t,'Reais')


# # 27 - O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                     Até 5 Kg           Acima de 5 Kg

File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por KgPara atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
#-------------------------------------------------------------------------------------------


kg = float(input('Quantidade de carne em Kg = '))
t_c = str(input('Carne desejada (ex: File duplo, Alcatra e Picanha) = '))
f_p = str(input('Será pago no Cartão Tabajara (ex:Sim/Não) = '))

if t_c == 'File duplo':
    print('Cupom Fiscal------------------------------------------------------')
    print('Carne escolhida = File Duplo')
    print('Quantidade (Kg) = ',kg)
    print('Uso do Cartão Tabajara = ',f_p)
    if kg<=5:
        pf = kg*4.90
        print('Preço total = ',pf)
    else:
        pf = kg*5.80
        print('Preço total = ',pf)

        if f_p == 'Sim':
            pdf = pf*0.05
            pr_T = pf-pdf
            print('Valor do desconto = ',pdf)
            print('Valor a pagar = ',pr_T)
            

if t_c == 'Alcatra':
    print('Cupom Fiscal------------------------------------------------------')
    print('Carne escolhida = Alcatra')
    print('Quantidade (Kg) = ',kg)
    print('Uso do Cartão Tabajara = ',f_p)
    if kg<=5:
        pa = kg*5.90
        print('Preço total = ',pa)
    else:
        pa = kg*6.80
        print('Preço total = ',pa)
        if f_p == 'sim':
            pda = pa*0.05
            pra_T = pa-pda
            print('Valor do desconto = ',pda)
            print('Valor a pagar = ',pra_T)
       
        
        
if t_c == 'Picanha':
    print('Cupom Fiscal------------------------------------------------------')
    print('Carne escolhida = Picanha')
    print('Quantidade (Kg) = ',kg)
    print('Uso do Cartão Tabajara = ',f_p)
    if kg<=5:
        pp = kg*6.90
        print('Preço total = ',pp)

    else:
        pp = kg*7.80
        print('Preço total = ',pp)
        if f_p == 'sim':
            pdp = pp*0.05
            prp_T = pp-pdp
            print('Valor do desconto = ',pdp)
            print('Valor a pagar = ',prp_T)       

