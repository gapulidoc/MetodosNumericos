import numpy as np
import matplotlib.pyplot as plt
from lmfit import Model

M=12.57*10**(-7)
epsilon=8.8541878*10**(-12)
c=1/(epsilon*M)
z=np.sqrt(M/epsilon)
angulo=(np.linspace(0,360,200))
cte=0.000001
P=1
sin=(np.sin(np.deg2rad(angulo)))**(2)
dP=(c*z*cte*P*sin)/(32*np.pi**2)

figure=plt.subplot(111, polar=True)
figure.plot(np.deg2rad(angulo),dP,label='', color ='green')
plt.legend()
plt.xlabel('')
plt.ylabel('')
plt.title('distribución angular de la potencia radiada por un dipolo eléctrico')
plt.grid()
plt.show()