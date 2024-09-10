#DESCRIÇÃO: RESOLUÇÃO DA QUESTÃO 4 DA LISTA DE EXERCÍCIOS SOBRE AJUSTE LINEAR USANDO INTERPOLAÇÃO
#POLINOMIAL USANDO O POLINÔMIO DE LAGRANGE:

import numpy as np

x = np.array([1.0, 3.0, 5.0])
y = np.array([1.5708,  1.5719, 1.5738])


#calcular os valores dos termos Li do polinômio do primeiro intervalo de valores:
k1 = x[0]-x[1]
k2 = x[0]-x[2]
k3 = x[1]-x[0]
k4 = x[1]-x[2]
k5 = x[2]-x[1]
k6 = x[2]-x[0]


#determinação do polinômio e os coeficientes para o primeiro intervalo de valores:
a = (y[0]/(k1*k2)+y[1]/(k3*k4)+y[2]/(k5*k6))
b = (-x[2]-x[1])*(y[0]/(k1*k2))+(-x[2]-x[0])*(y[1]/(k3*k4))+(-x[0]-x[1])*(y[2]/(k5*k6))
c = x[2]*x[1]*(y[0]/(k1*k2))+x[2]*x[0]*(y[1]/(k3*k4))+x[0]*x[1]*(y[2]/(k5*k6))

#polinomio:
k = 3.5
f = a*k**2+b*k+c

print(f'Coeficientes do polinômio: aX^2 + bX + c\na = {a:.6f}\nb = {b:.6f}\nc = {c:.6f}\nf(k) = {f:.6f}')
