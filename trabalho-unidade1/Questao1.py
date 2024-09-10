import matplotlib.pyplot as plt
import numpy as np


x = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0])
y = np.array([100.0, 25.0, 11.1, 6.3, 4.0, 2.8, 2.0, 1.6, 1.2, 1.0])

log_x = np.log(x)
log_y = np.log(y)

coeficientes = np.polyfit(log_x, log_y, 1)
b = coeficientes[0]
a = np.exp(coeficientes[1])

x1 = np.linspace(1.0,10,1000)
y1 = a*(x1**b)

print(f'Valor de a: {a:.6f}')
print(f'Valor de b: {b:.6f}')


plt.plot(x1,y1, color='green', label=f'Ajuste: y = {a:.2f} * x^{b:.2f}')
plt.scatter(x, y, label='Dados de amostra',color = 'blue')
plt.scatter(x,y)
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
