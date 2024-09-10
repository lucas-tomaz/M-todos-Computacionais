#DESCRIÇÃO: RESOLUÇÃO DA QUESTÃO 3 DA LISTA DE EXERCÍCIOS SOBRE AJUSTE LINEAR USANDO INTERPOLAÇÃO
# POLINOMIAL USANDO O POLINÔMIO DE LAGRANGE:

import numpy as np

x = np.array([2.8, 3.0, 3.2])
y = np.array([16.44, 20.08, 24.53])

x1 = ([3.0, 3.2, 3.4])
y1 = ([20.08, 24.53, 29.96])


#calcular os valores dos termos Li do polinômio do primeiro intervalo de valores:
k1 = x[0]-x[1]
k2 = x[0]-x[2]
k3 = x[1]-x[0]
k4 = x[1]-x[2]
k5 = x[2]-x[1]
k6 = x[2]-x[0]

#calcular os valores dos termos Li do polinômio do segundo intervalo de valores:
k_1 = x1[0]-x1[1]
k_2 = x1[0]-x1[2]
k_3 = x1[1]-x1[0]
k_4 = x1[1]-x1[2]
k_5 = x1[2]-x1[1]
k_6 = x1[2]-x1[0]

#para o primeiro intervalo de dados:
# Método L0:
#((x-x[1])/x[0]-x[1])*((x-x[2])/x[0]-x[2])
#print(f'O valor da expressão para L_0:(x-{x[1]})*(x-{x[2]})*{y[0]/(k1*k2):.2f}')

# Método L1:
#((x-x[0])/x[1]-x[0])*((x-x[2])/x[1]-x[2])
#print(f'O valor da expressão para L_1:(x-{x[0]})*(x-{x[2]})*{y[1]/(k3*k4):.2f}')

# Método L2:
#((x-x[1])/x[2]-x[1])*((x-x[0])/x[2]-x[0])
#print(f'O valor da expressão para L_2:(x-{x[1]})*(x-{x[0]})*{y[2]/(k5*k6):.2f}')

#determinação do polinômio e os coeficientes para o primeiro intervalo de valores:
a = (y[0]/(k1*k2)+y[1]/(k3*k4)+y[2]/(k5*k6))
b = (-x[2]-x[1])*(y[0]/(k1*k2))+(-x[2]-x[0])*(y[1]/(k3*k4))+(-x[0]-x[1])*(y[2]/(k5*k6))
c = x[2]*x[1]*(y[0]/(k1*k2))+x[2]*x[0]*(y[1]/(k3*k4))+x[0]*x[1]*(y[2]/(k5*k6))

#determinação do polinômio e os coeficientes para o segundo intervalo de valores:
a1 = (y1[0]/(k_1*k_2)+y1[1]/(k_3*k_4)+y1[2]/(k_5*k_6))
b1 = (-x[2]-x[1])*(y1[0]/(k_1*k_2))+(-x[2]-x[0])*(y1[1]/(k_3*k_4))+(-x[0]-x[1])*(y1[2]/(k_5*k_6))
c1 = x[2]*x[1]*(y1[0]/(k_1*k_2))+x[2]*x[0]*(y1[1]/(k_3*k_4))+x[0]*x[1]*(y1[2]/(k_5*k_6))

#polinomio:
k = 3.1
aproximado1 = a*k**2+b*k+c
aproximado2 = a1*k**2+b1*k+c1

print("PRIMEIRO INTERVALO:\n")
print(f'Coeficientes do polinômio: aX^2 + bX + c\n a = {a:.2f}\n b = {b:.2f}\n c = {c:.2f}')
print(f'Resultado para o valor de e^3.1 para o primeiro caso: {aproximado1:.3f}\n')

print("SEGUNDO INTERVALO:\n")
print(f'Coeficientes do polinômio: a1X^2 + b1X + c1\n a = {a1:.2f}\n b = {b1:.2f}\n c = {c1:.2f}')
print(f'Resultado para o valor de e^3.1 para o segundo caso: {aproximado2:.3f}\n')
print(f'Erro relativo1: {abs((np.exp(3.1) - aproximado1)/(np.exp(3.1)))}\n')
print(f'Erro relativo2: {abs((np.exp(3.1) - aproximado2)/(np.exp(3.1)))}\n')
