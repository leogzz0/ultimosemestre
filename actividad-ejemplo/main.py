import numpy as np
import matplotlib.pyplot as plt

probabilidades = [1/3, 1/3, 1/4, 1-(1/3 + 1/3 + 1/4)]
valores = [0, 1, 2, 3]

suma_probabilidades = sum(probabilidades)

n_simulaciones = 100000000
x_simuladas = np.random.choice(valores, size=n_simulaciones, p=probabilidades)

plt.hist(x_simuladas, bins=np.arange(-0.5, 4.5, 1), density=True, rwidth=0.8, alpha=0.7)
plt.xticks(valores)
plt.grid(True)
plt.show()

suma_probabilidades, probabilidades
