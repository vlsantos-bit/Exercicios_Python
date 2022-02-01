#!/usr/bin/env python
# coding: utf-8

# # 1-Faça um Programa que mostre a mensagem "Alo mundo" na tela. -- https://wiki.python.org.br/EstruturaSequencial

# In[12]:


print('alo mundo')


# # 2-Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].

# In[14]:


x=input('Insira um numero =')
print('O número informado foi = ', x)


# # 3-Faça um Programa que peça dois números e imprima a soma.

# In[15]:


a = []
for i in range(0,2,1):
    xd = input("Insira dois numeros e obtenha a soma =")
    a.append(float(xd))

som=sum(a)
print('Soma = ',som)


# # 4-Faça um Programa que peça as 4 notas bimestrais e mostre a média.

# In[16]:


bi = []
for i in range(0,4,1):
    xd = input("Notas Bimestrais =")
    bi.append(float(xd))
bi = sum(bi)/len(bi)
print('Média =', bi)


# # 5 - Faça um Programa que converta metros para centímetros.

# In[17]:


da = input("Conversor de metros para centimetros =")
da = float(da)*100
print('Conversão centimetros', da)


# # 6 -Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

# In[18]:


R = input("Insira o raio do circulo = ")
#Area de um circulo
a = 3.14*float(R)**2
print("Área do circulo",a)


# # 7 - Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
# 

# In[19]:


L = input("Insira a medida do lado do quadrado =")
L = float(L)**2
DL = 2*L
print("Dobro da área", DL)


# # 8 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

# In[22]:


s = input("Valor da hora trabalhada R$ = ")
d = input("Numero de dias trabalhados = ")
s = float(s)
d = float(d)
h = d*8
 
da = s*h
print("Salário total recebido =", da)


# # 9 - Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

# In[24]:


F = input('Insira valor de temperatura °F = ')
C = 5 * ((float(F)-32) / 9)
print("Valor em °C", C)
print(C)


# # 10 - Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

# In[25]:


C = input("Insira valor de temperatura °C = ")
F = ((9*float(C))/5)+32
print("Valor em °F", F)


# # 11 - Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# 
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

# In[26]:


i1 = input("Insira um numero inteiro =")
i2 = input("Insira um numero inteiro =")
r3 = input("Insira um numero real =")
i1 = int(i1)
i2 = int(i2)
r3 = float(r3)

res1 = (i1*2)+(i2/2)
print("O produto do dobro do primeiro com metade do segundo =", res1)
res2 = (i1*3)+r3
print('A soma do triplo do primeiro com o terceiro =',res2)
res3 = r3**3
print('O terceiro elevado ao cubo =', res3)


# # 12 - Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: 
# 
# (72.7*altura) - 58
# 

# In[28]:


alt = input("Insira a altura =")
ide = (72.7*float(alt))-58
print('Peso ideal =',ide)


# # 13 - Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58 ***********
# Para mulheres: (62.1*h) - 44.7

# In[29]:


alt = input('Insira a altura = ')
sex = input('Insira o sexo (ex: Homem/Mulher =')

alt = float(alt)

if sex=='Homem':
    res1 = (72.7*alt)-58
    print('Peso ideal =',res1)
elif sex=='Mulher':
    res2 = (62.1*alt)-44.7
    print('Peso ideal =',res2)
else:
    print("Sexo não indentificado") 


# # 14 - João Papo-de-Pescador, homem de bem, 
# comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

# In[99]:


pp = input('Insira o peso do peixe = ')
pp = float(pp)

print("Peso do peixe Kg = ",pp)
e = (pp-50.0)
print('Excesso estabelecido pelo regulamento de pesca SP Kg = ',e)

if pp>50.0:
    da=4*e
    print("Valor da multa a ser paga R$ = ",da)
else:
    print("Dentro do estabelecido")


# # 15 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# 
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato.
# Obs.: Salário Bruto - Descontos = Salário Líquido.
# 

# In[8]:


s = input("Insira valor do salário = ")
h = input('Número de horas trabalhadas =')
s = float(s)
h = float(h)
da = s*h
des =  (da*0.11)+(da*0.08)+(da*0.05)
real = da - des
print("Salário bruto = ", da)
print("Descontos =",des)
print("Total Liquído = ",real)


# # 16 - Faça um programa para uma loja de tintas. 
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

# In[39]:


import math as ma
l = input('Insira o tamanho em m² do local = ')
l = float(l)
vl = 80
ll = 18
li = (l/3)
la = ma.ceil(li/ll)
if la==0:
    print('N°de Latas = 1 lata')
else:
    print('N°de Latas', la)
pre = la*vl
if pre==0:
    print('Valor a ser pago R$ = 80')
else:
    print('Valor a ser pago RS =', pre)


# # 17-Faça um Programa para uma loja de tintas. 
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

# In[78]:


import math as ma
l = float(input('Insira o tamanho em m² do local = '))
t = l*0.10
l = l+t
vl = 80
ll = 18
li = (l/6)
print('Litros necessários', li)

#Latas ------------------------------------------------------------------------------------
la = ma.ceil(li/ll)
if la==0:
    print('N°de Latas = 1 lata')
else:
    print('N°de Latas =', la)
pre = la*vl
if pre==0:
    print('Valor a ser pago R$ = 80')
else:
    print('Valor a ser pago na lata RS =', pre)

#Galões -----------------------------------------------------------------------------------
ga = 3.6
prg = 25
g = ma.ceil(li/ga)
if g==0:
    print('N°de Galões = 1 galão')
else:
    print('N° de Galões =', g)
gp = g*prg
if gp==0:
    print('Valor a ser pago R$ = 25')
else:
    print('Valor a ser pago no galão RS =', gp)

#Misturar ambos com (Otimização) (floor = arredonda para baixo)----------------------------
o = ma.floor(li/ll)
vo = o*vl
#aplicando função de resto %
res = li%ll
ug = ma.ceil(res/ga)
pg = ug*prg

pt = pg+vo
print('n° de Latas =', o, ' n° de galões=', ug, ' Valor a ser pago R$ =',pt)


# In[72]:


res


# In[60]:


desl = (la*ll)-li
desg = (g*ga)-li
print(desl)
print(desg)

l2 = li-desl
print(l2)


# In[65]:





# # Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
# 

# In[11]:


inp = input('Tamanho de um arquivo - MB =')
vel = input('Velocidade de um link de internet Mbps =')

down_s = (float(inp))/(float(vel)/8)
down_m = down_s/60

print('Tempo aproximado de downloado em minutos =', down_m)


# In[ ]:




