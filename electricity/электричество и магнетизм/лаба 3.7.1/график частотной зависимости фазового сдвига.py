import numpy as np
import matplotlib.pyplot as plt
import math

T = [2.6, 2.2, 2, 1.8, 1.6, 1.5, 1.4, 1.1, 0.9, 0.7, 0.6, 0.52, 0.48, 0.42, 0.38, 0.36, 0.36, 0.28, 0.24, 0.2, 0.165, 0.136, 0.115, 0.09, 0.076, 0.064, 0.056, 0.048, 0.044, 0.036, 0.033, 0.007]
nu = np.array([140, 170, 200, 230, 260, 280, 290, 410, 540, 670, 800, 930, 1060, 1180, 1320, 1415, 1415, 1769, 2211, 2764, 3455, 4318, 5398, 6747, 8434, 10542, 13178, 16473, 20590, 25739, 32173, 40217]) * 10**(-3)

psi = (np.array(T)*10**(-3) + 3.14/2) * 3.14 * 2 * np.array(nu)

y = psi - 3.14/4
x = np.array(nu)**0.5

fig, ax = plt.subplots()
t = np.polyfit(y, nu, 1)
f = np.poly1d(t)
print('k = ', f)

sigma = t[0]**2/(3.14 * ((45/2)*10**(-3))**2)
print('sigma = ', sigma)

plt.plot(x, np.polyval(np.polyfit(x, y, 1), x), color='orange')
ax.scatter(x, y, s=4, c='red', marker='o', zorder = 1)
plt.errorbar(x, y, xerr=0.05, yerr=10, linestyle='none', color='black')
plt.ylabel('psi - pi/4')
plt.xlabel('nu^0.5, Гц')
plt.title('psi - pi/4(nu^0.5)')
plt.grid(linewidth = 0.3)
plt.savefig('график частотной зависимости фазового сдвига.png')
plt.show()
