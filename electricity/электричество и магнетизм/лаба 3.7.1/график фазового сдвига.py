import numpy as np
import matplotlib.pyplot as plt
import math

nu = [170, 200, 280, 410, 540, 670, 800, 930, 1060, 1320, 1415]
T = np.array([2.2, 2.0, 1.5, 1.1, 0.9, 0.7, 0.6, 0.52, 0.48, 0.38, 0.36]) * 10**(-3)

psi = (np.array(T) - 3.14/2) * 3.14 * 2 * np.array(nu)
y = [math.tan(psi[i]) for i in range(len(T))]
print(y)

fig, ax = plt.subplots()
t = np.polyfit(y, nu, 1)
f = np.poly1d(t)
print('k = ', f)

sigma = t[0]/(3.14 * (45/2)*10**(-3) * 1.5*10**(-3))
print('sigma = ', sigma)

plt.plot(nu, np.polyval(np.polyfit(nu, y, 1), nu), color='orange')
ax.scatter(nu, y, s=4, c='red', marker='o', zorder = 1)
plt.errorbar(nu, y, xerr=50, yerr=0.02, linestyle='none', color='black')
plt.ylabel('tg(psi)')
plt.xlabel('nu, Гц')
plt.title('tg(psi)(nu)')
plt.grid(linewidth = 0.3)
plt.savefig('график зависимости фазового сдвига.png')
plt.show()