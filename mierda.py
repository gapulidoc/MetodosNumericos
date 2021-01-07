import numpy as np
import matplotlib.pyplot as plt
from lmfit import Model


x = np.linspace(0.01,(np.pi)/2,num=500)
f = 100-100*(((-1.33*np.cos(x)+(1/1.33)*((1.33**2-np.sin(x)*np.sin(x))**(1/2)))/(1.33*np.cos(x)+(1/1.33)*((1.33**2-np.sin(x)*np.sin(x))**(1/2))))**2)
plt.plot(x,f,label='Coeficiente t para na polarización paralelea al plano', color ='green')
plt.legend()
plt.xlabel('')
plt.ylabel('')
plt.title('Coeficiente t para na polarización paralelea al plano')
plt.grid()
plt.show()
