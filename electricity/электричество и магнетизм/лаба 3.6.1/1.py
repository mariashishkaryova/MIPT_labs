import numpy as np
import matplotlib.pyplot as plt

tau = [20, 22.2, 22.5, 28.6, 33.3, 40, 50, 66.7, 100, 200] #mks
delta_nu = [50, 45.2, 40.2, 35, 30, 25, 20, 15, 10, 5] #kHz

fig, ax = plt.subplots()
t = np.polyfit(1/np.array(tau), delta_nu, 1)
f = np.poly1d(t)

plt.plot(1/np.array(tau), np.polyval(np.polyfit(1/np.array(tau), delta_nu, 1), 1/np.array(tau)), color='c')
plt.title('delta_nu(1/tau)')
plt.xlabel('1/tau, кГц')
plt.ylabel('delta_nu, кГц')
plt.grid(linewidth = 1)
plt.savefig('1.png')
plt.show()