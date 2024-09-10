#DESCRIÇÃO: RESOLUÇÃO DA QUESTÃO 2 DA LISTA DE EXERCÍCIOS SOBRE AJUSTE LINEAR USANDO INTERPOLAÇÃO
#POLINOMIAL USANDO O POLINÔMIO DE LAGRANGE:
import numpy as np
import matplotlib.pyplot as plt

lamb = np.array([0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1])
n_lamb = []
#Equação dos três termos de Sellmeier:

n_lamb1 = np.sqrt(1 + (0.73454395*(lamb)**2)/(lamb**2 - 0.007564986) + (0.42710828*(lamb)**2)/(lamb**2 - 0.01253323) + (0.82103399*(lamb)**2)/(lamb**2 - 117.64743))

n_lamb.append(n_lamb1)
for k in n_lamb:
  y1 = np.log((1/k)-0.5)

coeficientes = np.polyfit(lamb, y1, 1)
b = coeficientes[0]
a = coeficientes[1]

print(f'Valor de a:{a:.6f}\nValor de b:{b:.6f}')

x_real = np.linspace(0.5, 1.1, 1000)
n_lamb_ajustado = 1/(0.5 + np.exp(a+b*x_real))

n_lamb_real = np.sqrt(1 + (0.73454395*(x_real)**2)/(x_real**2 - 0.007564986) + (0.42710828*(x_real)**2)/(x_real**2 - 0.01253323) + (0.82103399*(x_real)**2)/(x_real**2 - 117.64743))

#calculo do erro relativo:
erro_relativo = 0.98
erro_real = np.sqrt(1 + (0.73454395*(erro_relativo)**2)/(erro_relativo**2 - 0.007564986) + (0.42710828*(erro_relativo)**2)/(erro_relativo**2 - 0.01253323) + (0.82103399*(erro_relativo)**2)/(erro_relativo**2 - 117.64743))
erro_ajustado = 1/(0.5 + np.exp(a+b*erro_relativo))

resultado_erro = (erro_real - erro_ajustado)/erro_real
print(f'Erro relativo para λ = 0.98: {resultado_erro}')

plt.plot(x_real, n_lamb_real, color='green', label='Curva Real')
plt.plot(x_real,n_lamb_ajustado, color='blue', label='Curva Ajustada')
plt.xlabel('λ')
plt.ylabel('n(λ)')
plt.legend()
plt.grid(True)
plt.show()
