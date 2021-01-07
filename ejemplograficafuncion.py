import numpy as np
import matplotlib.pyplot as plt
from lmfit import Model


x = np.linspace(0.01,15,num=500)
f = -80*(np.exp(-0.8*x))/x * (np.sin(0.54*x))**2
plt.plot(x,f,label='Gráfico a integrar', color ='salmon')
plt.legend()
plt.xlabel('r(fm)')
plt.ylabel('Integrando')
plt.title('')
plt.grid()
plt.show()
